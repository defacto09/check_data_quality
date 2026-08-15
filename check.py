import pandas as pd
import sys

df = pd.read_csv("data/retail_store_sales.csv")

valid_payments = ('Digital Wallet', 'Credit Card', 'Cash')
computed = df["Price Per Unit"] * df["Quantity"]

def status(count):
    if count == 0:
        return "PASS"
    else:
        return "FAIL"

def pct(count):
    p = len(df)
    return (count / p) * 100

def check(label, mask):
    count = mask.sum()
    print(f"{status(count)} - {label}: {count} ; {pct(count).round(1)}%")
    return count > 0

dupes = df["Transaction ID"].duplicated()
negative_pr = df["Price Per Unit"] < 0
bad_qty = df["Quantity"] <= 0
missing_item = df["Item"].isna()
missing_price = df["Price Per Unit"].isna()
invalid_payment = ~df["Payment Method"].isin(valid_payments)
mismatch = (df["Total Spent"] - computed).abs() > 0.01

results = [
    check("Duplicated transactions ID", dupes),
    check("Negative Price Per Unit", negative_pr),
    check("Invalid Quantity", bad_qty),
    check("Missing Item", missing_item),
    check("Missing Price", missing_price),
    check("Invalid Payment", invalid_payment),
    check("Value mismatch", mismatch)
]

if any(results):
    sys.exit(1)

