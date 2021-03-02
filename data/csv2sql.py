import pandas as pd
import sqlite3
import os

if os.path.exists("shopee.db"):
    pass
else:
    conn = sqlite3.connect('shopee.db')

    login = pd.read_csv('data/login.csv')
    print(login.head())
    purchase_detail = pd.read_csv('data/purchase_detail.csv')
    user_info = pd.read_csv('data/user_info.csv')
    user_label_train = pd.read_csv('data/user_label_train.csv')
    submission = pd.read_csv('data/submission.csv')

    login.to_sql('login', conn, if_exists='replace',index = True)
    purchase_detail.to_sql('purchase_detail', conn, if_exists='replace',index = False)
    user_info.to_sql('user_info', conn, if_exists='replace',index = False)
    user_label_train.to_sql('user_label_train', conn, if_exists='replace', index=False)
    submission.to_sql('submission',conn,if_exists='replace', index=False)
