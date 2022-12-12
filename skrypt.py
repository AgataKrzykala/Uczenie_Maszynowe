# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:08:49 2022

@author: agata
"""


import cv2
import numpy as np

cap = cv2.VideoCapture('kolory.MP4')

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video_output = cv2.VideoWriter('outputstatic2.mp4', fourcc, 50.0, (1920, 1080))
fgbg = cv2.createBackgroundSubtractorMOG2()

# kernel_o = np.ones((27,27),np.uint8)
# kernel_c = np.ones((36,36),np.uint8)

while (1):

    # Take each frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    lower_red1 = np.array([170, 150, 50])
    upper_red1 = np.array([180, 255, 255])

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red = np.array([0, 150, 50])
    upper_red = np.array([5, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask_blue + mask_red + mask_red1

    fgmask = fgbg.apply(frame)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame,
                          mask=((mask_blue | mask_red | mask_red1) & fgmask))

    # rgb_frame = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

    # removing noise from the frame using morphology
    # cleanedup_frame = cv2.morphologyEx(cv2.morphologyEx(
    # rgb_frame, cv2.MORPH_OPEN, kernel_o),
    # cv2.MORPH_CLOSE, kernel_c)

    video_output.write(res)

    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
video_output.release()

cv2.destroyAllWindows()
