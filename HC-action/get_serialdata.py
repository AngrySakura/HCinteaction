#-*- coding: utf-8 -*-

#获取串口的传感器数据,并存放在初始数据文件中

import serial
import re
import time

def Save_originaldata():
    #串口参数设定
    comport = 'COM3'
    baudrate = 9600
    bytesize = 8
    #原始数据文件路径
    orgdatapath = 'D:\pycharm\HC-Data\originaldata.txt'
    #时间戳设置，超过10s则停止读取
    timelimit = 10
    starttime = time.time()

    #打开串口
    print('参数设置：串口=%s ，波特率=%d', comport, baudrate)
    ser = serial.Serial(comport, baudrate, timeout=0.5)
    #默认串口被占用则手动选择串口
    if not ser.isOpen():
        comport = input('请输入串口：')
        print('参数设置：串口=%s ，波特率=%d', comport, baudrate)
        ser = serial.Serial(comport, baudrate, timeout=0.5)
    #打开文件
    file = open(orgdatapath, 'w', encoding = 'utf-8')

    #循环获取串口数据并保存
    temp = ser.readline()   #第一次获取数据可能是不完整的，循环外空读一次数据提升效率
    while ((time.time() - starttime) < timelimit):
        temp = ser.readline()
        temp = temp.decode('ascii')
        temp = re.sub('\r', '', temp)   #除'\r'符
        print(time.time(),':',temp)    #输出测试
        file.write(temp)

    file.close()

def Get_accelerationdata():

    return 1

Save_originaldata()