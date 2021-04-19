#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/18 11:06 下午
# @Author : 狄仁杰666
# @Site : 
# @File : imageService.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt


def show_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()


def read_image(path):
    image = cv2.imread(path)
    return image


if __name__ == "__main__":
    no_color_image = read_image("../image/1.jpeg")
    show_image(no_color_image)
