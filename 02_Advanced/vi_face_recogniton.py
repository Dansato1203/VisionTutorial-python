#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened() is False:
  print("Can not open camera")
  sys.exit()

faceCascade = cv2.CascadeClassifier("cascade_file/haarcascade_frontalface_alt2.xml")

while True:
  ret, frame = cap.read()
  
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  face = faceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))

  if len(face) > 0:
       for rect in face:
         cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (255, 255, 255), thickness=2)

  cv2.imshow('face', frame)
  key = cv2.waitKey(1)
  if key != -1:
    break

cap.release()
cv2.destroyAllWindows()
