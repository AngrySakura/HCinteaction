#-*- coding: utf-8 -*-
#简单绘图，画出真实数据和测试数据的路径，估算偏差

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time_integral import *

locationdatapath = 'D:\pycharm\HC-Data\locationdata.txt'    #位置数据地址

def Get_data():
    result = []

    file_location = open(locationdatapath, 'r', encoding='utf-8')
    temp = file_location.readlines()

    for elem in temp:
        elem = re.sub('\n', '', elem)
        location = re.split(' ', elem)
        location = stof(location)
        result.append(location)

    file_location.close()
    return result

def Get_x(data):
    result = []
    for elem in data:
        result.append(elem[0])

    return result

def Get_y(data):
    result = []
    for elem in data:
        result.append(elem[1])

    return result

def Get_z(data):
    result = []
    for elem in data:
        result.append(elem[2])

    return result

def draw():
    fig = plt.figure()
    ax = Axes3D(fig)

    location = Get_data()
    x = Get_x(location)
    y = Get_y(location)
    z = Get_z(location)

    ax.scatter3D(x, y, z, cmap = 'Blue')
    ax.plot3D(x, y, z, 'gray')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

    return 1

draw()