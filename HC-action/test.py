import re

temp = b'Gyro (deg) X=-3.60 Y=0.43 Z=0.58 Accel (g) X=-0.12 Y=0.05 Z=-1.16\r\n'
temp = temp.decode('ascii')
temp = re.sub('\r\n','',temp)
