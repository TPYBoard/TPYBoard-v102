from pyb import UART,Servo

#舵机信号线接X1，可以创建4个Servo，分别是1~4，对应的引脚是X1~X4
s1 = Servo(1)
#调整舵机转动到0角度的位置
s1.angle(0)

uart = UART(3,9600,timeout=10)

def setServoTurn(flag):
    turn_angle = s1.angle()
    if flag:
        #逆时针 值递增 最大值90度
        turn_angle += 15 #每按一次转15度
        if turn_angle <= 90:
            s1.angle(turn_angle)
    else:
        #顺时针 值递减 最小值-90度
        turn_angle -= 15
        if turn_angle >= -90:
            s1.angle(turn_angle)
while True:
    if uart.any() > 0:
        val = uart.read()[-1]
        if val == 68:
            setServoTurn(True)
        elif val == 64:
            setServoTurn(False)