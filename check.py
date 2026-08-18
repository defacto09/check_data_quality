import pandas as pd
import sys

df = pd.read_csv("data/retail_store_sales.csv")

valid_payments = ('Digital Wallet', 'Credit Card', 'Cash')
computed = df["Price Per Unit"] * df["Quantity"]

results = []

def status(count):
    if count == 0:
        return "PASS"
    else:
        return "FAIL"

def pct(count):
    p = len(df)
    return (count / p) * 100

def single_check(label, mask):
    count = mask.sum()
    print(f"{status(count)} - {label}: {count} | {pct(count).round(1)}%")
    if count > 0:  
        print(f"    rows: {failed_rows(mask)}")
    return count > 0 

def summary(results):
    failed_checks = sum(results)
    total = len(results)
    print(f"{failed_checks} of {total} checks failed")

def list_check():
    for label, mask in checks:
        results.append(single_check(label, mask))

def failed_rows(mask):
    return df[mask].index[:5].to_list()

dupes = df["Transaction ID"].duplicated()
negative_pr = df["Price Per Unit"] < 0
bad_qty = df["Quantity"] <= 0
missing_item = df["Item"].isna()
missing_price = df["Price Per Unit"].isna()
invalid_payment = ~df["Payment Method"].isin(valid_payments)
mismatch = (df["Total Spent"] - computed).abs() > 0.01

checks = [
    ("Duplicated transactions ID", dupes),
    ("Negative Price Per Unit", negative_pr),
    ("Invalid Quantity", bad_qty),
    ("Missing Price", missing_price),
    ("Missing Item", missing_item),
    ("Invalid Payment", invalid_payment),
    ("Value mismatch", mismatch) 
    ]

def main():
    list_check()
    summary(results)
    if any(results):
        sys.exit(1)

if __name__ == "__main__":
    main()