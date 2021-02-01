#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import cv2
import numpy as np

def green_extraction(img, hsv_img):
    
    hsv_min = np.array([30, 64, 0])
    hsv_max = np.array([90, 255, 255])

    img_mask = cv2.inRange(hsv_img, hsv_min, hsv_max)

    green_img = cv2.bitwise_and(img, img, mask = img_mask)

    return green_img

def blue_extraction(img, hsv_img):
    
    hsv_min = np.array([90, 0, 0])
    hsv_max = np.array([150, 255, 255])

    img_mask = cv2.inRange(hsv_img, hsv_min, hsv_max)

    blue_img = cv2.bitwise_and(img, img, mask = img_mask)

    return blue_img

def main():

    img = cv2.imread("images/sea.jpg")

    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    green = green_extraction(img, hsv_img)
    blue = blue_extraction(img, hsv_img)

    cv2.imshow("origin", img)
    cv2.imshow("hsv", hsv_img)
    cv2.imshow("green", green)
    cv2.imshow("blue", blue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

