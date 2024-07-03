import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')

cap = cv2.VideoCapture('collision_video.mp4')

#  For saving the output video to local folder
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output_collision1.avi', fourcc, 20.0, (1020, 500))

def points(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', points)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    list = []
    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        nm = str(row['name'])
        list.append([x1, y1, x2, y2, nm])

    text_position = (54, 91)
    for val in list:
        x, y, w, h, nm = val

        if nm == 'collision':
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 3)

            cv2.rectangle(frame, (38, 28), (684, 110), (0, 0, 0), -1)
            cv2.putText(frame, 'Collision occurred!', text_position, cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 4)

        if nm == 'forklift':
            cv2.rectangle(frame, (x, y), (w, h), (144, 238, 144), 3)

            cv2.rectangle(frame, (x, y-40), (x+185, y), (144, 238, 144), -1)
            cv2.putText(frame, 'Forklift', (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)

        if nm == 'car':
            cv2.rectangle(frame, (x, y), (w, h), (255, 144, 144), 3)

            cv2.rectangle(frame, (x, y - 40), (x + 90, y), (255, 144, 144), -1)
            cv2.putText(frame, 'Car', (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)

    frame = cv2.resize(frame, (1020, 500))
    # out.write(frame)
    cv2.imshow('FRAME', frame)
    count = 0

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()




    
    
