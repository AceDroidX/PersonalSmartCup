import Main
from pcduino import adc


def getT():
    return adc.analog_read(Main.pinList['t'])


def getP():
    return adc.analog_read(Main.pinList['p'])


