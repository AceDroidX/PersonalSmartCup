import threading

from pcduino.myserial import *
import time

weight = 0
temp1 = 0
temp2 = 0


def startSerial():
    serial = Serial()
    serial.__init__()
    temp = ""
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
    pass

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
