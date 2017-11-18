import sqlite3

import os

path = os.path.split(os.path.realpath(__file__))[0]
accountsfile = path + '/Accounts.db'


def regAccounts(name, password):
    reg = sqlite3.connect(accountsfile)
    reg.execute('''CREATE TABLE IF NOT EXISTS users 
           (id INTEGER PRIMARY KEY      NOT NULL,
           name           TEXT          NOT NULL UNIQUE,
           password       TEXT          NOT NULL);''')
    idcursor = reg.execute("SELECT id FROM users ORDER BY id DESC;")
    insertcursor = reg.execute("INSERT INTO users VALUES (" + idcursor[0] + ");")
