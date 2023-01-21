import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# print(model)
img=cv2.imread('data/table.jpg')
results = model(img)
results.print()
print(results.xyxy)
cv2.imshow('YOLO COCO', np.squeeze(results.render()))
cv2.waitKey(0)

