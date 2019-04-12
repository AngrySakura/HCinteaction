'''
测试inteaction_system关于从串口读取数据的线程
'''
import serial
import re
import time

originaldata = []

def stof(list):
    result = []
    for element in list:
        result.append(float(element))
    return result


def get_serdata():
    # 串口参数设定
    comport = 'COM3'
    baudrate = 9600

    # 打开串口
    print('参数设置：串口=%s ，波特率=%d', comport, baudrate)
    ser = serial.Serial(comport, baudrate, timeout=0.5)
    # 默认串口被占用则手动选择串口
    if not ser.isOpen():
        comport = input('请输入串口：')
        print('参数设置：串口=%s ，波特率=%d', comport, baudrate)
        ser = serial.Serial(comport, baudrate, timeout=0.5)

    #循环获取串口数据并保存
    temp = ser.readline()   #第一次获取数据可能是不完整的，循环外空读一次数据略过
    temp = ser.readline()
    while 1 :
        temp = ser.readline()
        temp = temp.decode('ascii')
        temp = re.sub('\r\n', '', temp)   #除'\r'符
        acceleration = re.split(' ', temp)
        acceleration = stof(acceleration)
        print(time.time(),':',acceleration)    #输出测试
        print(type(temp))
        originaldata.append(acceleration)

    return 1

get_serdata()