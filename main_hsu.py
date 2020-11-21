import pandas as pd
from utils import read, output

detail, info, login, label, sub = read()

# results.to_csv("output/demo.csv", index=False)

detail['weekday'] = pd.to_datetime(detail.grass_date).dt.dayofweek
detail['month'] = pd.to_datetime(detail.grass_date).dt.month
detail['amount_per_order'] = detail['total_amount'] / detail['order_count']

select_cols = ['month', 'userid', 'order_count', 'total_amount']
detail_group = detail.groupby(['month', 'userid'], as_index=False).sum()[select_cols]

merge_data = pd.merge(detail_group, info, on='userid')
merge_data = pd.merge(merge_data, label)

merge_data.head()
