import pandas as pd
from typing import List, Tuple, TextIO


def read():
    purchase_detail = pd.read_csv("data/purchase_detail.csv")
    user_info = pd.read_csv("data/user_info.csv")
    login = pd.read_csv("data/login.csv")
    user_label = pd.read_csv("data/user_label_train.csv")
    submission = pd.read_csv("data/submission.csv")

    return purchase_detail, user_info, login, user_label, submission


def analyze(data) -> List[List[int]]:

    return results


def output(data: List[List[int]]):
    
    upload_cols = ["userid", "label"]
    upload_rows_len = 75325
    assert len(data) == upload_rows_len
    assert len(data[0]) == len(upload_cols)

    results = pd.DataFrame(data, columns=upload_cols)

    return results