import MAX7219 #导入模块

#CLK -> X1,CS -> X2,DIN -> X3
#num级联的模块数量
led = MAX7219.Lattice('X1','X2','X3',num=1)
#要显示的内容,显示的内容根据字库文件而定，见font_max7219.py。
#大家也可以自定义图案添加上。
msg = 'LOVE大小'

while True:
    #显示
    led.display(msg)
    
# import MAX7219 #导入模块
# from pyb import UART
# #初始化串口参数，使用串口6 波特率9600 超时时间50毫秒
# #串口6 TX->Y1 RX->Y2 
# #其他串口对应的引脚编号详见针脚图：http://old.tpyboard.com/document/documents/10x/TPYBoardv10xPCBpng.pdf
# uart = UART(6,9600,timeout=50)

# #CLK -> X1,CS -> X2,DIN -> X3
# #num级联的模块数量
# led = MAX7219.Lattice('X1','X2','X3',num=1)
# led.display('大')                   #默认显示大心图案
# while True:
    # if uart.any() > 0:              #any()返回串口缓存区的数据长度，返回值大于0即表示有数据
        # DATA = uart.read().decode() #读取缓存区全部数据，返回值为bytes，decode()转为字符串
        # led.display(DATA)           #进行显示