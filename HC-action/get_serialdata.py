#-*- coding: utf-8 -*-

#获取串口的传感器数据,并存放在初始数据文件中

import serial
import re

def Save_originaldata():
    #串口参数设定
    comport = input('输入串口号：')
    baudrate = 9600
    bytesize = 8
    #原始数据文件路径
    orgdatapath = 'D:\pycharm\HC-Data\originaldata.txt'

    #打开串口
    print('参数设置：串口=%s ，波特率=%d', comport, baudrate)
    ser = serial.Serial(comport, baudrate, timeout=0.5)
    #打开文件
    file = open(orgdatapath, 'w', encoding = 'utf-8')

    #循环获取串口数据并保存
    while 1:
        temp = ser.readline()
        temp = temp.decode('ascii')
        temp = re.sub('\r', '', temp)   #除去制表符
        file.write(temp)

        #print(temp)

    file.close()

def Get_accelerationdata():

    return 1

#Save_originaldata()