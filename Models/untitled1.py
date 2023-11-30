# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VaIYydefYsw8kUH1-AUTGuiZcNZ-HtFN
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import time
# Load YOLO model
net = cv2.dnn.readNet("/content/yolov3-spp.cfg", "/content/yolov3-spp.weights")
classes = []
with open("coco.names", "r") as f:
  classes = [line.strip() for line in f.readlines()]
outputlayers = net.getUnconnectedOutLayersNames()
# Define input image
image = cv2.imread("/content/671.jpg")

# Get image dimensions
(height, width) = image.shape[:2]

# Define the neural network input
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# Perform forward propagation
output_layer_name = net.getUnconnectedOutLayersNames()
output_layers = net.forward(output_layer_name)

# Initialize list of detected people
people = []

# Loop over the output layers
for output in output_layers:
    # Loop over the detections
    for detection in output:
        # Extract the class ID and confidence of the current detection
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        # Only keep detections with a high confidence and class_id corresponding to people
        if class_id == 0 and confidence > 0.25:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # Add the detection to the list of people
            people.append((x, y, w, h))

# Assuming you want to add the label "Person" to the image
label = "Le Person"

# Define the font type and color
font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 255, 255)  # White color

# Draw bounding boxes around the people
for (x, y, w, h) in people:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.putText(image, label, (x, y - 10), font, 1, color, 2)  # Adjust font size and thickness as needed

# Show the image using cv2_imshow
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()

net = cv2.dnn.readNet("/content/yolov3-spp.cfg", "/content/yolov3-spp.weights")
print(confidence,class_id)