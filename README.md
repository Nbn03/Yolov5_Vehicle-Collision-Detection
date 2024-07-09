# Yolov5_Vehicle Collision Detection



https://github.com/Nbn03/Yolov5_Vehicle-Collision-Detection/assets/136473086/0658f999-6309-41d1-9784-eb08545bd04b



## Overview
This repository contains code for detecting vehicle collisions using Yolov5 and OpenCV. The model is trained to detect cars, forklifts, and collisions, alerting when a collision occurs in the video frames. The output video is saved locally with the detected collisions highlighted.

## Main Functionalities
- **Vehicle Collision Detection:** Uses Yolov5 to detect cars, forklifts, and collisions.
- **Alert Mechanism:** Alerts with a message and a bounding box when a collision occurs.
- **Video Saving:** Utilizes OpenCV's cv2.VideoWriter_fourcc(*'XVID') function to save the result video output.

## OpenCV Library
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It contains more than 2500 optimized algorithms, which can be used for various image processing and computer vision tasks, including:
- Image Processing: Manipulating image data to enhance or extract information.
- Video Analysis: Analyzing video frames for object detection, tracking, and recognition.
- Object Detection: Identifying and locating objects within images or videos.
  
In this project, OpenCV is used for drawing bounding boxes, displaying alert messages, and saving the output video.

## YOLO Models and Yolov5 Version
YOLO (You Only Look Once) models are a family of convolutional neural networks designed for real-time object detection. Yolov5, the version used in this project, is known for its high speed and accuracy, making it suitable for various object detection tasks.

## Model Training
The model is trained using the Yolov5 architecture with the following specifics:

- **Annotation:** Around 400 frames annotated with three classes: "Car," "Forklift," and "Collision".
- **Training:** 150 epochs using the LabelImg tool in Anaconda Prompt.

## Collision Detection Details
- **Classes:** "Car," "Forklift," and "Collision."
- **Alert Mechanism:** When a collision occurs between cars, forklifts, or between a forklift and a car, a collision bounding box appears, and an alert message is displayed on the video frames.
- **Video Saving:** The result video output is saved locally using cv2.VideoWriter_fourcc(*'XVID').

## Running the Code
### Points to Note
- Ensure all files in the repository are present in the folder where the main_collision.py file is running. If the video or weight file is in a different folder, provide the paths accordingly.
- Install the required dependencies using requirements.txt.
- This code can also run on the pre-trained Yolov5 weights by specifying the classes properly.

## Usage
1. Clone the repository:
```
git clone https://github.com/Nbn03/Yolov5_Vehicle-Collision-Detection.git
cd Yolov5_Vehicle-Collision-Detection
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the main script:
```
python main_collision.py 
```
