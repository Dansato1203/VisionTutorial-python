#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np

img = cv2.imread("images/lena.jpeg")

faceCascade = cv2.CascadeClassifier("cascade_file/haarcascade_frontalface_alt2.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = faceCascade.detectMultiScale(gray, 1.1, 3, minSize=(100,100))

if len(face) > 0:
    for rect in face:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)

half_img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.imshow('face', half_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
