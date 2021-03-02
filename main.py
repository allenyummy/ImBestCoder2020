import pandas as pd
import os
import sys

from sklearn.ensemble import GradientBoostingClassifier
from utils import *
import sqlite3

import logging

LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y%m%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, filename='output/myLog.log',
                    format=LOGGING_FORMAT, datefmt=DATE_FORMAT)
logger = logging.getLogger(__name__)


if os.path.exists("shopee.db"):
    logger.debug('db exists!')
    pass
else:
    logger.debug('cannot find db; hence, return!')
    sys.exit()

con = sqlite3.connect('shopee.db')
cursor = con.cursor()
query = """
    create view if not exists purchase_detail_label
    as
    select userid_1.order_count, userid_1.total_amount, userid_1.category_encoded, user_label_train.label
    from 
    (select * from purchase_detail group by userid) as userid_1
    inner join user_label_train
    on userid_1.userid==user_label_train.userid;
    """

cursor.execute(query)
logger.debug('Finish CRUD temp view!')

query = """
    select * from purchase_detail_label;
"""
cursor.execute(query)
query_result = cursor.fetchall()
# print(len(df))
logger.debug('Finish join purchase detail and training label!')

X, Y = [], []
for i in query_result:
    X.append(list(i)[:-1])
    Y.append(list(i)[-1])

data_split_ratio = int(len(X)*0.9)
X_train = X[:data_split_ratio]
X_test = X[data_split_ratio:]
Y_train = Y[:data_split_ratio]
Y_test = Y[data_split_ratio:]

# X, y = make_hastie_10_2(random_state=0)
# X_train, X_test = X[:2000], X[2000:]
# y_train, y_test = y[:2000], y[2000:]
logger.debug('Finish data spliting')

clf = GradientBoostingClassifier(n_estimators=10, learning_rate=0.1,
                                 max_depth=3, random_state=0).fit(X_train, Y_train)
test_acc = clf.score(X_test, Y_test)
# print(test_acc)
logger.debug('Finish training with validation acc {}'.format(test_acc))


submission_x = []
submission_detail = query_submission_detail(cursor)
for i in submission_detail:
    submission_x.append(list(i)[1:])

logger.debug('Finish test data loading')

submission_y = clf.predict_proba(submission_x)
# print(submission_y[:5,1])
results = pd.read_csv('data/submission.csv')
results['label'] = submission_y[:, 1]
logger.debug('Finish concat id and predicting results')
# print(results.head())
results.to_csv("output/demo.csv", index=False)
logger.debug('Finish output to csv format and return this program')
