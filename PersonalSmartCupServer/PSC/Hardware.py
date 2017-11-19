from pcduino.myserial import *

weight = 0
temp1 = 0
temp2 = 0


def startSerial():
    serial = Serial()
    serial.__init__()
    temp = ""
    while True:
        temp += serial.read_all()
        cmd = temp.split("\n")
        temp = cmd[len(cmd) - 1]
        for i in cmd:
            global weight
            global temp1
            global temp2
            t = i.split(":")
            if t[0] == "weight":
                weight = t[1]
            elif t[0] == "temp1":
                temp1 = t[1]
            elif t[0] == "temp2":
                temp2 = t[1]


if __name__ == '__main__':
    startSerial()
    while True:
        print('weight:?', weight)
        print('temp1:?', temp1)
        print('temp2:?', temp2)
