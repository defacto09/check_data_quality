import pandas as pd

df = pd.read_csv("data/retail_store_sales.csv")

valid_payments = ('Digital Wallet', 'Credit Card', 'Cash')

def check(label, mask):
    print(f'{label}: {mask.sum()}')

dupes = df["Transaction ID"].duplicated()
negative_pr = df["Price Per Unit"] < 0
bad_qty = df["Quantity"] <= 0
missing_item = df["Item"].isna()
missing_price = df["Price Per Unit"].isna()
invalid_payment = ~df["Payment Method"].isin(valid_payments)

check("Duplicated transactions ID", dupes)
check("Negative Price Per Unit", negative_pr)
check("Invalid Quantity", bad_qty)
check("Missing Item", missing_item)
check("Missing Price", missing_price)
check("Invalid Payment", invalid_payment)
