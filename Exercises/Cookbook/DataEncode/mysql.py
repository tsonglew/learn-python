# -*- coding: utf-8 -*-


import sqlite3
db = sqlite3.connect('database.db')

d = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)

min_price = 100
for row ini db.execute('select * from portfolio where price >= ?', (min_price, )):
    print(row)
