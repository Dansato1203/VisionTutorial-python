#!/usr/bin/env python3                                                      
# -*- coding: utf-8 -*-

import cv2
#import matplotlib.pyplot as plt

img = cv2.imread("images/image00003.jpg")

print('画像のy座標: ', end=' ')
num1 = int(input())
print('画像のx座標: ', end=' ')
num2 = int(input())

print(img[num1,num2])
