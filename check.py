import pandas as pd

data = pd.read_csv("data/retail_store_sales.csv")

total = len(data)
missing = data.isna().sum()

percentage = ((missing/total)*100).round(1)
print(percentage)