import pandas as pd
from typing import List, Tuple, TextIO


def read(datafile: TextIO):

    return data


def analyze(data) -> List[List[int]]:

    return results


def output(data: List[List[int]]):
    
    upload_cols = ["A", "B", "C"]
    upload_rows_len = 2
    assert len(data) == upload_rows_len
    assert len(data[0]) == len(upload_cols)

    results = pd.DataFrame(data, columns=upload_cols)

    return results