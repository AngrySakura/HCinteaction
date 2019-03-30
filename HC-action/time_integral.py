#-*- coding: utf-8 -*-
#将加速度简单二次积分求位移，采用时域积分

interval = 0.105 #积分时间间隔近似为0.105s即105ms,串口发送间隔为100ms
gravity = 9.8 #重力加速度
coefficientofgravity = 0.9 #静止情况下z轴的重力加速度系数
#velocity = [0, 0, 0]   #velocity[0]代表x轴速速度，velocity[1]代表y轴速度，velocity[2]代表z轴速度

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