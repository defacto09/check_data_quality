import pandas as pd

data = pd.read_csv("data/retail_store_sales.csv")

dupes = data["Transaction ID"].duplicated()
negative_pr = data["Price Per Unit"] < 0
bad_qty = data["Quantity"] <= 0
missing_item = data["Item"].isna()
missing_price = data["Price Per Unit"].isna()

print(f"Duplicated transactions ID: {dupes.sum()}")
print(f"Negative Price Per Unit: {negative_pr.sum()}")
print(f"Bad Quantity: {bad_qty.sum()}")
print(f"Missing items: {missing_item.sum()}")
print(f"Missing price: {missing_price.sum()}")