import cv2
import numpy as np

img = cv2.imread('data/table.jpg')
ltop = (124, 307)
rtbm = (533, 554)
img_cap = img[ltop[1]:rtbm[1], ltop[0]: rtbm[0]]
cv2.imshow('data/table.jpg', img_cap)
cv2.waitKey(0)
cv2.imwrite('output.jpg', img_cap)
