# I'm the best coder! Challenge 2020


# Feature Engineering
Invert .csv to .db for SQL usage.  
``` python
if os.path.exists("shopee.db"):
    pass
else:
    detail = pd.read_csv('path')
    conn = sqlite3.connect('shopee.db')
    detail.to_sql('ShopeeDB', conn, if_exists='replace',index = False)
```

Select duplicate userid and insert them to another table.  
``` sql
CREATE TABLE duplicate_userid AS SELECT * FROM ShopeeDB WHERE userid IN ( SELECT userid FROM ShopeeDB GROUP BY userid HAVING COUNT(*) > 1) ORDER BY userid; 

CREATE TABLE unique_userid AS SELECT * FROM ShopeeDB WHERE userid not IN ( SELECT userid FROM duplicate_userid) ORDER BY userid;
```

Count for duplicate_userid is 7774099, which is interesting since the origin table has 7792956. This indicates most of users has multiple shopping records. Only 18857 users has only one shopping record.  

``` sql
select count(*) from duplicate_userid;
select count(*) from unique_userid; 
select count(*) from shopeedb;
```

