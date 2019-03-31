#-*- coding: utf-8 -*-
#将加速度简单二次积分求位移，采用时域积分

import re

#文件路径S
orgdatapath = 'D:\pycharm\HC-Data\originaldata.txt'
shiftdatapath = 'D:\pycharm\HC-Data\shiftdata.txt'
locationdatapath = 'D:\pycharm\HC-Data\locationdata.txt'

interval = 0.105 #积分时间间隔近似为0.105s即105ms,串口发送间隔为100ms
gravity = 9.8 #重力加速度
coefficientofgravity = 0.9 #静止情况下z轴的重力加速度系数
velocity = [0, 0, 0]   #velocity[0]代表x轴速速度，velocity[1]代表y轴速度，velocity[2]代表z轴速度
location = [0, 0, 0]    #初始位置，坐标起点

#一次积分求速度，参数分别为当前速度，当前加速度
#计算公式v=v0 + a * t
def First_integral(velocity, acc):
    v = []

    v_x = velocity[0] + acc[0] * gravity * interval
    v_y = velocity[1] + acc[1] * gravity * interval
    v_z = velocity[2] + (acc[2] - coefficientofgravity) * gravity * interval
    v.append(v_x)
    v.append(v_y)
    v.append(v_z)

    return v

#二次积分求位移,调用一次积分函数,参数为当前速度和当前加速度
#计算公式s=v0 * t
def Second_integral(velocity, acc):
    shift = []
    v = First_integral(velocity, acc)

    s_x = v[0] * interval
    s_y = v[1] * interval
    s_z = v[2] * interval

    shift.append(s_x)
    shift.append(s_y)
    shift.append(s_z)

    return shift

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

def calculate_location():
    #打开文件
    file_shift = open(shiftdatapath, 'r', encoding='utf-8')
    file_location = open(locationdatapath, 'w', encoding = 'utf-8')


    temp = file_shift.readlines()
    for tempshift in temp:
        tempshift = re.sub('\n', '', tempshift)
        shift = re.split(' ', tempshift)
        shift = stof(shift)
        #计算位置
        location[0] += shift[0]
        location[1] += shift[1]
        location[2] += shift[2]

        templocation = ftos(location)
        locationdata = ' '.join(templocation)
        locationdata += '\n'
        file_location.write(locationdata)


    print('success\n')
    #关闭文件
    file_shift.close()
    file_location.close()

#calculate_location()