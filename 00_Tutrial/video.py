#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  cv2.imshow('image', frame)
  key = cv2.waitKey(1)
  if key != -1:
    break

cap.release()
cv2.destroyAllWindows()

