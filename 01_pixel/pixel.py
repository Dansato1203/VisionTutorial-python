#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("images/image00003.jpg")

height, width, ch = img.shape

empty_img = np.zeros((height, width, 3), np.uint8)

cv2.imshow("img", img)
cv2.imshow("empty", empty_img)
cv2.waitKey(0)

height = int(height)
width = int(width)


for y in range(height):
  for x in range(width):
    (b, g, r) = img[y, x]
    empty_img[y, x] = (b, g, r)
    cv2.imshow("empty", empty_img)
    cv2.waitKey(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
