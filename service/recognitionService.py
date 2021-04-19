#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/18 11:10 下午
# @Author : 狄仁杰666
# @Site : 
# @File : recognitionService.py
# @Software: PyCharm
import cv2

from service.imageService import read_image


def recognize_faces(image, model='../model/haarcascade_frontalface_default.xml'):
    detector = cv2.CascadeClassifier(model)
    # 图片进行灰度处理
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rectangles = detector.detectMultiScale(gray_image)
    for (x, y, w, h) in rectangles:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image


if __name__ == "__main__":
    image = read_image("../image/1.jpeg")
    recognize_faces(image)
