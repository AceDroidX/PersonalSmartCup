# coding=utf-8
import threading

from pcduino.myserial import *
import time

weight = 0
temp1 = 0  # 杯温
temp2 = 0  # 水温

serial = None


def startSerial():
    global serial
    serial = Serial()
    serial.__init__()
    while True:
        cmd = serial.read_all().decode()
        if not cmd == "":
            t = cmd.split(" ")
            # print(t)
            for i in t:
                global weight
                global temp1
                global temp2
                t1 = i.split(":")
                # print(t1)
                if t1[0] == "weight":
                    weight = t1[1]
                    print(weight)
                elif t1[0] == "temp1":
                    temp1 = t1[1]
                    print(temp1)
                elif t1[0] == "temp2":
                    temp2 = t1[1]
                    print(temp2)
                detectHardware()


def detectHardware():
    if temp1 > 40:
        serial.write_string('temp1high')
    else:
        serial.write_string('temp1ok')
    if temp2 > 60:  # 需要修改 尽量烫
        serial.write_string('temp2ok')
    else:
        serial.write_string('temp2low')


def startHardware():
    startSerial()


if __name__ == '__main__':
    #    s = Serial()
    #    s.__init__()
    #    while True:
    #        print(s.read_all())
    #        time.sleep(0.5)
    serialThread = threading.Thread(target=startSerial())
    serialThread.start()
