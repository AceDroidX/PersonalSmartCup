from pcduino.myserial import *

weight = 0
temp1 = 0
temp2 = 0

def startSerial():
    serial = Serial()
    serial.__init__()
    temp = ""
    cmd = ""
    while True:
        temp += serial.read_all()
        cmd = temp.split("\n")
        temp = cmd[len(cmd) - 1]
        for i in cmd:
            t = i.split(":")
            if t[0] == "weight":
                weight = t[1]
            elif t[0] == "temp1":
                temp1 = t[1]
            elif t[0] == "temp2":
                temp2 = t[1]

