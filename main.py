import pandas as pd
from utils import read, output

detail, info, login, label, sub = read()

print (detail.head())


# results.to_csv("output/demo.csv", index=False)