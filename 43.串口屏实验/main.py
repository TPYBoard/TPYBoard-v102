from pyb import LED
from pyb import UART

END_CMD = b'\xFF\xFF\xFF' #����������ָ��Ľ����������ɸ���
txt = 't1.txt="{}"'       #�ı��ı������ֵ�����

uart = UART(2,9600,timeout=50) #������ͨ�Ų�����Ĭ��9600
#ͨ�����ذ�ť���ư���LED4����LED4Ĭ�������Ϊ��
#�ǳ���һ��ʼ�Ͱ��ı���Ϊ��
CMD = txt.format('��').encode() + END_CMD
uart.write(CMD)

while True:
    if uart.any() > 0:
        data = uart.read()
        print('revFromHMI:',data)
        #����65 00 03 01 FF FF FF �������ťʱ ���ǴӴ��ڶ�ȡ����ʮ����������
        #��: 65 00 04 01 FF FF FF ����ذ�ťʱ ���ǴӴ��ڶ�ȡ����ʮ����������
        #��Ҫע��һ��micropython�Ӵ��ڶ�ȡ����ʱ���ص���bytes���͵����ݣ������һЩ16��������תΪ��Ӧ��ascii�ַ�
        #Ҳ����˵�����ڳ�����ʵ�ʽ��յ��Ŀ���ť�������������ģ�b'e\x00\x03\x01\xff\xff\xff'
        if data[:2] == b'e\x00' and data[4:] == END_CMD:
            if data[2] == 3: #bytes��ͨ��������ȡԪ��ֵʱ��Ĭ��תΪʮ������
                CMD = txt.format('��').encode() + END_CMD
                uart.write(CMD)
                print('sendToHMI:',CMD)
                pyb.LED(4).on()
            elif data[2] == 4:
                CMD = txt.format('��').encode() + END_CMD
                uart.write(CMD)
                print('sendToHMI:',CMD)
                pyb.LED(4).off()
            else:
                print('Error:',data)