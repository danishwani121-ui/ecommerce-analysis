# ==========================================
# 🛒 E-commerce Sales Analysis Project
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import os

print("🛒 E-commerce Sales Analysis Started\n")

# create folder to save charts
os.makedirs("charts", exist_ok=True)

# ------------------------------------------
# 1️⃣ Load Dataset
# ------------------------------------------
df = pd.read_csv("superstore.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# ------------------------------------------
# 2️⃣ Basic Data Info
# ------------------------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# 3️⃣ Total Sales & Profit
# ------------------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# ------------------------------------------
# 4️⃣ Sales by Category
# ------------------------------------------
sales_category = df.groupby("Category")["Sales"].sum()

plt.figure()
sales_category.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.savefig("charts/sales_by_category.png")
plt.show()

# ------------------------------------------
# 5️⃣ Profit by Category
# ------------------------------------------
profit_category = df.groupby("Category")["Profit"].sum()

plt.figure()
profit_category.plot(kind="bar")
plt.title("Profit by Category")
plt.ylabel("Total Profit")
plt.savefig("charts/profit_by_category.png")
plt.show()

# ------------------------------------------
# 6️⃣ Sales by Region
# ------------------------------------------
sales_region = df.groupby("Region")["Sales"].sum()

plt.figure()
sales_region.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.savefig("charts/sales_by_region.png")
plt.show()

# ------------------------------------------
# 7️⃣ Monthly Sales Trend
# ------------------------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.savefig("charts/monthly_sales.png")
plt.show()

# ------------------------------------------
# 8️⃣ Top 10 Products by Sales
# ------------------------------------------
top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.ylabel("Sales")
plt.savefig("charts/top_products.png")
plt.show()

print("\n✅ Analysis Completed Successfully!")
