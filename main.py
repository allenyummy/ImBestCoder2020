import pandas as pd
import os
from metadata.tables import ShopeeDB
from utils import read, output
import sqlite3
from peewee import *



# detail, info, login, label, sub = read()
# print (detail.head())

if os.path.exists("shopee.db"):
    pass
else:
    detail = read()
    conn = sqlite3.connect('shopee.db')
    detail.to_sql('ShopeeDB', conn, if_exists='replace',index = False)

con = sqlite3.connect('shopee.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM ShopeeDB WHERE userid IN ( SELECT userid FROM ShopeeDB GROUP BY userid HAVING COUNT(*) > 1) ORDER BY userid limit 5;")
# cursor.execute("SELECT * FROM shopeeDB limit 10;")
print(type(cursor.fetchall()))
# names = [description[0] for description in cursor.description]
# print(names)
# results.to_csv("output/demo.csv", index=False)