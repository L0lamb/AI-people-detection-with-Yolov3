# AI-people-detection-with-YOLOv3
# People detection using the YOLOv3 algorithm
YOLOv3 is a real-time object detection algorithm. The following model uses it to differentiate people from other object
# Overview of YOLOv3's network architecture
![Imgur](https://i.stack.imgur.com/eZkfj.png)
#Requirement
- The AI requires you to have [coco.name](http://mscoco.org/dataset/#overview) as a database or you can use the coco.name has provided in here
- Opencv:
1. Easy integration with an OpenCV application: If your application already uses OpenCV and you want to use YOLOv3, you don’t have to worry about compiling and building the extra Darknet code.
2. OpenCV CPU version is 9x faster: OpenCV’s CPU implementation of the DNN module is astonishingly fast. For example, Darknet, when used with OpenMP takes about 2 seconds on a CPU for inference on a single image. In contrast, OpenCV’s implementation runs in a mere 0.22 seconds! Check out the table below.
3. Python support: Darknet is written in C and does not officially support Python. In contrast, OpenCV does. There are Python ports available for Darknet, though.
- The Yolov3 module as provided for no reason at all (or maybe use on [this](https://pjreddie.com/darknet/yolo/) and change the confident of the code with the class id)
#Prerequisites
* opencv-python
* opencv-contrib-python
* Numpy
#Instruction:
1. Download the [config](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3-spp.cfg) with the [weight](https://pjreddie.com/media/files/yolov3-spp.weights) of YOLOv3 spp.
2. Change the directory in the 6 lines of the code into the path on your computer so it matches the path of the YOLOv3

![Screenshot 2023-11-30 011510.png](https://github.com/L0lamb/AI-people-detection-with-Yolov3/blob/main/Images/Screenshot%202023-11-30%20011510.png)

3. Change the path of the image you want to detect
[![Screenshot](Screenshot 2023-11-30 013528.png)](https://github.com/L0lamb/AI-people-detection-with-Yolov3/blob/main/Images/Screenshot%202023-11-30%20013528.png)

#Notes:
* As of right now, there is a problem with the A.I or the database that caused the result to overlap and give out multiple outlines for 1 result which I can only guess the AI mistook many layers for 1 result.
