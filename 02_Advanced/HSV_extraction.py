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

def red_extraction(img, hsv_img):
    
    hsv_min1 = np.array([0, 200, 50])
    hsv_max1 = np.array([30, 255, 255])
    
    img_mask1 = cv2.inRange(hsv_img, hsv_min1, hsv_max1)

    hsv_min2 = np.array([165, 200, 50])
    hsv_max2 = np.array([179, 255, 255])

    img_mask2 = cv2.inRange(hsv_img, hsv_min2, hsv_max2)

    img_mask = img_mask1 + img_mask2

    red_img = cv2.bitwise_and(img, img, mask = img_mask)

    return red_img

def main():

    img = cv2.imread("images/sample_rgb.jpg")

    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    green = green_extraction(img, hsv_img)
    blue = blue_extraction(img, hsv_img)
    red = red_extraction(img, hsv_img)

    cv2.imshow("origin", img)
    cv2.imshow("hsv", hsv_img)
    cv2.imshow("green", green)
    cv2.imshow("blue", blue)
    cv2.imshow("red", red)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

