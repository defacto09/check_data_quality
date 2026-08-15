import pandas as pd

data = pd.read_csv("data/retail_store_sales.csv")

def check(label, mask):
    print(f'{label}: {mask.sum()}')

dupes = data["Transaction ID"].duplicated()
negative_pr = data["Price Per Unit"] < 0
bad_qty = data["Quantity"] <= 0
missing_item = data["Item"].isna()
missing_price = data["Price Per Unit"].isna()

check("Duplicated transactions ID", dupes)
check("Negative Price Per Unit", negative_pr)
check("Invalid Quantity", bad_qty)
check("Missing Item", missing_item)
check("Missing Price", missing_price)