import datetime
import os
from peewee import *
from utils import read

db = SqliteDatabase('shopee.db')

class ShopeeDB(Model):
    id = AutoField()
    userid = IntegerField(verbose_name="消費者id")
    grass_date = DateTimeField(verbose_name="購買日")
    category_encoded = IntegerField(verbose_name="品項編碼")
    order_count = IntegerField(verbose_name="訂單數量")
    total_amount = IntegerField(verbose_name="購買項目數量")
    training = BooleanField(default=0)
    testing = BooleanField(default=0)

    class Meta:
        database = db

def checkDB():
    if os.path.exists("shopee.db"):
        pass
    else:
        detail, info, login, label, sub = read()
        # print(detail.shape)
        ShopeeDB.create_table()
        for i in range(len(detail)):
            print(i/len(detail)*100)
            instance = {
                "userid" : detail.iloc[i,0],
                "grass_date" : detail.iloc[i,1],
                "order_count" : detail.iloc[i,2],
                "total_amount" : detail.iloc[i,3],
                "category_encoded" : detail.iloc[i,4],
            }
            ShopeeDB.create(**instance)