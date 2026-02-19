import pandas as pd

df = pd.read_csv("data/website_traffic.csv")

print("Rows:", len(df))
print(df.head())

print("\nFriday vs Saturday comparison:")
print(df[df["date"] == "2025-01-03"])
print(df[df["date"] == "2025-01-04"])

print("\nJanuary vs December comparison (Organic):")
print(df[(df["date"] == "2025-01-05") & (df["channel"] == "Organic")])
print(df[(df["date"] == "2025-12-05") & (df["channel"] == "Organic")])
