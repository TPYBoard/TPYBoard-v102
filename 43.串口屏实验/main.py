from pyb import LED
from pyb import UART

END_CMD = b'\xFF\xFF\xFF' #发给串口屏指令的结束符，不可更改
txt = 't1.txt="{}"'       #改变文本框文字的命令

uart = UART(2,9600,timeout=50) #串口屏通信波特率默认9600
#通过开关按钮控制板载LED4亮灭，LED4默认情况下为灭
#那程序一开始就把文本改为关
CMD = txt.format('关').encode() + END_CMD
uart.write(CMD)

while True:
    if uart.any() > 0:
        data = uart.read()
        print('revFromHMI:',data)
        #开：65 00 03 01 FF FF FF 点击开按钮时 我们从串口读取到的十六进制数据
        #关: 65 00 04 01 FF FF FF 点击关按钮时 我们从串口读取到的十六进制数据
        #需要注意一点micropython从串口读取数据时返回的是bytes类型的数据，它会把一些16进制数据转为相应的ascii字符
        #也就是说我们在程序中实际接收到的开按钮的数据是这样的，b'e\x00\x03\x01\xff\xff\xff'
        if data[:2] == b'e\x00' and data[4:] == END_CMD:
            if data[2] == 3: #bytes在通过索引获取元素值时会默认转为十进制数
                CMD = txt.format('开').encode() + END_CMD
                uart.write(CMD)
                print('sendToHMI:',CMD)
                pyb.LED(4).on()
            elif data[2] == 4:
                CMD = txt.format('关').encode() + END_CMD
                uart.write(CMD)
                print('sendToHMI:',CMD)
                pyb.LED(4).off()
            else:
                print('Error:',data)