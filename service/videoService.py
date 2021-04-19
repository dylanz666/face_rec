#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/18 11:15 下午
# @Author : diren@gaoding.com
# @Site : 
# @File : videoService.py
# @Software: PyCharm
import time

import cv2


def open_video_capture(count=10):
    cap = cv2.VideoCapture(0)
    while not cap.isOpened():
        time.sleep(1)
        count -= 1
        if count <= 0:
            return
        cap = cv2.VideoCapture(0)
    else:
        return cap


if __name__ == "__main__":
    capture = open_video_capture()
    assert (capture is not None)
