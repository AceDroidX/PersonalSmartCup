import sqlite3

import os
import time

path = os.path.split(os.path.realpath(__file__))[0]
datafile = path + '/data.db'


def addDrinkRecords(waterVolume):
    reg = sqlite3.connect(datafile)
    reg.execute('''CREATE TABLE IF NOT EXISTS drinkRecords 
           (time INTEGER PRIMARY KEY      NOT NULL,
           volume           INTEGER          NOT NULL);''')
    insertcursor = reg.execute("INSERT INTO drinkRecords VALUES (?);", (time.time(), waterVolume))


def readAllDrinkRecords():
    reg = sqlite3.connect(datafile)
    reg.execute('''CREATE TABLE IF NOT EXISTS drinkRecords 
               (time INTEGER PRIMARY KEY      NOT NULL,
               volume           INTEGER          NOT NULL);''')
    return reg.execute("SELECT * FROM drinkRecords;").fetchall()
