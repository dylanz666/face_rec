#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/18 11:26 下午
# @Author : 狄仁杰666
# @Site : 
# @File : main.py
# @Software: PyCharm
import cv2

from service.imageService import read_image
from service.recognitionService import recognize_faces
from service.videoService import open_video_capture


def recognize_in_file(image_path):
    image = read_image(image_path)
    image = recognize_faces(image, './model/haarcascade_frontalface_default.xml')
    while True:
        cv2.imshow('Face Recognition Demo 1', image)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cv2.destroyAllWindows()
    return


def recognize_in_video():
    cap = open_video_capture()
    if not cap:
        return
    while True:
        ret, frame = cap.read()
        image = recognize_faces(frame, './model/haarcascade_frontalface_default.xml')
        cv2.imshow('Face Recognition Demo 2', image)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    recognize_in_file("image/1.jpeg")
    # recognize_in_video()
