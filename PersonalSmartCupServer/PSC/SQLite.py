import sqlite3

import os
import time

path = os.path.split(os.path.realpath(__file__))[0]
datafile = path + '/data.db'


def addDrinkRecords(waterVolume):
    reg = sqlite3.connect(datafile)
    reg.execute('''CREATE TABLE IF NOT EXISTS drinkRecords 
           (time NUMERIC PRIMARY KEY      NOT NULL,
           volume           INTEGER          NOT NULL);''')
    insertcursor = reg.execute("INSERT INTO drinkRecords VALUES (?,?);", (time.time(), waterVolume))
    reg.commit()
    reg.close()


def readAllDrinkRecords():
    reg = sqlite3.connect(datafile)
    reg.execute('''CREATE TABLE IF NOT EXISTS drinkRecords 
               (time NUMERIC PRIMARY KEY      NOT NULL,
               volume           INTEGER          NOT NULL);''')
    t = reg.execute("SELECT * FROM drinkRecords;").fetchall()
    reg.commit()
    reg.close()
    return t

if __name__ == '__main__':
    addDrinkRecords(1000)
    addDrinkRecords(2000)
    addDrinkRecords(3000)
    addDrinkRecords(100)
    print(readAllDrinkRecords())
