#!/usr/bin/env python3                                                      
# -*- coding: utf-8 -*-

import cv2
#import matplotlib.pyplot as plt

img = cv2.imread("images/image00003.jpg")

height, width, ch = img.shape

size = width * height

# 情報表示
print("画像の横幅: ", width)
print("画像の高さ: ", height)
print("チャンネル数: ", ch)
print("画素数: ", size)

cv2.imshow("title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
