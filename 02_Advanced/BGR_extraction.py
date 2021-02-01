#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import cv2
import numpy as np

def green_extraction(img):
    
    BGR_min = np.array([0, 0, 0])
    BGR_max = np.array([60, 255, 128])

    img_mask = cv2.inRange(img, BGR_min, BGR_max)

    green_img = cv2.bitwise_and(img, img, mask = img_mask)

    return green_img

def blue_extraction(img):
    
    BGR_min = np.array([140, 0, 0])
    BGR_max = np.array([255, 255, 150])

    img_mask = cv2.inRange(img, BGR_min, BGR_max)

    blue_img = cv2.bitwise_and(img, img, mask = img_mask)

    return blue_img

def main():

    img = cv2.imread("images/sea.jpg")

    green = green_extraction(img)
    blue = blue_extraction(img)

    cv2.imshow("origin", img)
    cv2.imshow("green", green)
    cv2.imshow("blue", blue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
