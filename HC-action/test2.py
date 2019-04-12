'''
测试inteaction_system关于加速度处理和控制鼠标的线程
'''

from pynput import mouse
import time

originaldata = []
velocity = [0, 0, 0]    #初始速度为0
positon = [0, 0, 0]     #保存位移，提高精度，减少在长度到像素点转换过程中的精度损耗
interval = 0.105 #积分时间间隔近似为0.105s即105ms,串口发送间隔为100ms
gravity = 9.8 #重力加速度
coefficientofgravity = 0.85 #静止情况下z轴测量到的的重力加速度系数
boundary = [1536, 864]  #1920*1080分辨率下屏幕像素点边界（比例经过放缩）
'''
screen_length = 0.34528
screen_width = 0.19422
'''
pixel_density = 4448.56    #像素密度，代表每米屏幕有多少个像素点,数值= 1536/0.34528
pixle_pos = []  #鼠标位置，第一次获取鼠标句柄时初始化

#list物理长度转像素点数
def mtopixel(list):
    result = []

    for i in range(3):
        list[i] += positon[i]

    for elem in list:
        result.append(int(elem * pixel_density))

    for i in range(3):
        positon[i] = list[i] - result[i] / pixel_density

    return result

#线程2从originaldata中获取加速度，进一步计算得到位移
def calculate_velocity():
    acceleration = originaldata[0]

    velocity[0] -= acceleration[0] * interval   #设备-y轴对应屏幕x轴，设备-z轴对应屏幕y轴，所以用-=
    velocity[1] -= acceleration[1] * interval
    velocity[2] -= acceleration[2] * interval

    originaldata.pop(0) #使用完后删除该加速度

    return 1

#计算位移
def calculate_positon():
    re_position = []    #每次的相对位移,单位m

    calculate_velocity()    #计算获得最新速度
    p_x = velocity[0] * interval
    p_y = velocity[1] * interval
    p_z = velocity[2] * interval
    re_position.append(p_x)
    re_position.append(p_y)
    re_position.append(p_z)

    return re_position

#边界检查函数，如果位移超出了屏幕边界，那么便把鼠标指在超出的边界上，防止越界
def positon_check(movement):
    result = movement
    if pixle_pos[0] + movement[0] < 0:
        result[0] = - pixle_pos[0]
    elif pixle_pos[0] + movement[0] > boundary[0]:
        result[0] = boundary[0] - pixle_pos[0]

    if pixle_pos[1] + movement[1] < 0:
        result[1] = - pixle_pos[1]
    elif pixle_pos[1] + movement[1] > boundary[1]:
        result[1] = boundary[1] - pixle_pos[1]

    return result

#获取每次移动的相对位置，单位是像素点个数
def get_pixel():
    temp = calculate_positon()
    movement = mtopixel(temp)
    result = positon_check(movement)
    return result

#控制鼠标函数
def control_mouse():
    mouse_c = mouse.Controller()    #鼠标控制句柄
    temp = mouse_c.position    #鼠标初始位置
    pixle_pos.append(temp[0])
    pixle_pos.append(temp[1])

    while 1 :
        if len(originaldata):
            movement = get_pixel()
            mouse_c.move(movement[1], movement[2])
            print(movement[1], movement[2])
        else:
            time.sleep(0.1)

    return 1

if __name__ == '__main__':
    for i in range(200):
        originaldata.append([0.02, 0.05, 0.04])
    control_mouse()