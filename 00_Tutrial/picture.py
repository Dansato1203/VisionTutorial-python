#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread("images/image00001.jpg")
cv2.imshow("title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

