#-*- coding: utf-8 -*-
#简单绘图，画出真实数据和测试数据的路径，估算偏差

import numpy as np
import matplotlib.pyplot as plt
import re
from time_integral import *

velocity = [0, 0, 0]   #velocity[0]代表x轴速速度，velocity[1]代表y轴速度，velocity[2]代表z轴速度
'''
interval = 0.105 #积分时间间隔近似为0.105s即105ms,串口发送间隔为100ms
gravity = 9.8 #重力加速度
coefficientofgravity = 0.9 #静止情况下z轴的重力加速度系数
'''

#文件路径S
orgdatapath = 'D:\pycharm\HC-Data\originaldata.txt'
shiftdatapath = 'D:\pycharm\HC-Data\shiftdata.txt'

#list字符串转浮点数
def stof(list):
    result = []
    for element in list:
        result.append(float(element))
    return result

#list浮点数转字符串
def ftos(list):
    result = []
    for element in list:
        result.append(str(element))
    return result

def calculate_shift():
    #打开文件
    file_org = open(orgdatapath, 'r', encoding = 'utf-8')
    file_shift = open(shiftdatapath, 'w', encoding = 'utf-8')

    #提取加速度
    temp = file_org.readlines()
    for tempacceleration in temp:
        #数据预处理，字符串转float
        tempacceleration = re.sub('\n', '', tempacceleration)
        acceleration = re.split(' ', tempacceleration)
        acceleration = stof(acceleration)

        shift = Second_integral(velocity, acceleration)

        #数据存储预处理，float转字符串
        shift = ftos(shift)
        shiftdata = ' '.join(shift)
        shiftdata += '\n'
        file_shift.write(shiftdata)

    #关闭文件
    file_org.close()
    file_shift.close()

calculate_shift()