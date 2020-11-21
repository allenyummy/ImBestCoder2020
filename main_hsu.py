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

gender_dummies = pd.get_dummies(merge_data.gender, columns=[])
seller_dummies = pd.get_dummies(merge_data.is_seller)
month_dummies = pd.get_dummies(merge_data.month)
label_dummies = pd.get_dummies(merge_data.label)

gender_dummies.columns = ['gender_%i'%i for i in range(gender_dummies.shape[1])]
seller_dummies.columns = ['seller_%i'%i for i in range(seller_dummies.shape[1])]
month_dummies.columns = ['month_%i'%i for i in range(month_dummies.shape[1])]
label_dummies.columns = ['label_%i'%i for i in range(label_dummies.shape[1])]

selected_cols = ['userid', 'order_count', 'total_amount']
final_data = pd.concat([gender_dummies, seller_dummies, month_dummies, merge_data[selected_cols]], axis=1)
