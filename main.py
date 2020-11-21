import pandas as pd
from utils import read, output


data = [[1,2,3], [1,2,3]]
results = output(data)
results.to_csv("output/demo.csv", index=False)