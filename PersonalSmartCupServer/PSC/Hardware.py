#!/usr/bin/python3
# coding=utf-8
import threading

from pcduino.myserial import *
import SQLite
import time

cupWeight = 10

weight = 0
tmpWeight = [0, 0, 0, 0, 0]
tmpWeight2 = 0
waterWeight = 0
tmpWater = [0, 0, 0, 0, 0]
temp1 = 0  # 杯温
temp2 = 0  # 水温
# cupState = False  # false 水杯在上面  true 水杯不在上面

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
    stableWater(weight)


def stableWater(volume):
    global tmpWeight
    global tmpWeight2
    del tmpWeight[0]
    tmpWeight.append(volume)
    if max(tmpWeight) - mix(tmpWeight) < 10:
        tmpWeight2 = average(tmpWeight)
        calculateWater()
    pass


def calculateWater():
    global waterWeight
    global weight
    global cupWeight
    global tmpWater
    global tmpWeight2
    waterWeight = tmpWeight2 - cupWeight
    if waterWeight < -5:
        print('水杯已拿走')
        return
    elif 5 > waterWeight >= -5:
        waterWeight = 0
    changeWeight = tmpWater - waterWeight
    # do something
    if changeWeight > 10:
        SQLite.addDrinkRecords(changeWeight)
        print('add water ?',changeWeight)
    tmpWater = waterWeight


def average(seq):
    return float(sum(seq)) / len(seq)


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
