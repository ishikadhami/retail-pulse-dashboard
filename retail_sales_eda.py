import random
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Repeatable sample data for this class project
random.seed(25)
output_folder = Path("charts")
output_folder.mkdir(exist_ok=True)

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
categories = ["Electronics", "Home & Kitchen", "Clothing"]
regions = ["North", "South", "East", "West"]
payments = ["Cash", "Card", "UPI"]

# Approximate product prices in Indian rupees
price_ranges = {
    "Electronics": (4000, 25000),
    "Home & Kitchen": (500, 8000),
    "Clothing": (400, 4000),
}

rows = []
order_number = 1

for month_number, month in enumerate(months, start=1):
    # More sample orders later in the year to demonstrate a seasonal pattern
    orders_this_month = 8 + month_number

    for _ in range(orders_this_month):
        category = random.choice(categories)
        low_price, high_price = price_ranges[category]
        unit_price = random.randint(low_price, high_price)
        units = random.randint(1, 4)

        # Gradually increase sample quantities toward year end
        if month_number >= 10 and random.random() < 0.5:
            units += 1

        rows.append({
            "Order_ID": f"ORD{order_number:03}",
            "Month": month,
            "Region": random.choice(regions),
            "Category": category,
            "Units": units,
            "Unit_Price_INR": unit_price,
            "Revenue_INR": units * unit_price,
            "Payment_Method": random.choice(payments),
            "Data_Note": "Generated sample data"
        })
        order_number += 1

# Save the dataset
df = pd.DataFrame(rows)
df.to_csv("retail_sales.csv", index=False)

# Summaries for the charts
month_revenue = df.groupby("Month")["Revenue_INR"].sum().reindex(months)
category_revenue = df.groupby("Category")["Revenue_INR"].sum().sort_values(ascending=False)
region_revenue = df.groupby("Region")["Revenue_INR"].sum().sort_values(ascending=False)
category_units = df.groupby("Category")["Units"].sum().sort_values(ascending=False)
payment_orders = df["Payment_Method"].value_counts()

plt.style.use("ggplot")

# Chart 1: Revenue by month
plt.figure(figsize=(9, 5))
month_revenue.plot(marker="o", color="#3559e0")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "01_monthly_revenue.png", dpi=150)
plt.close()

# Chart 2: Revenue by category
plt.figure(figsize=(8, 5))
category_revenue.plot(kind="bar", color="#3559e0")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(output_folder / "02_category_revenue.png", dpi=150)
plt.close()

# Chart 3: Revenue by region
plt.figure(figsize=(8, 5))
region_revenue.plot(kind="bar", color="#19a89a")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig(output_folder / "03_region_revenue.png", dpi=150)
plt.close()

# Chart 4: Units sold by category
plt.figure(figsize=(8, 5))
category_units.plot(kind="bar", color="#f29a4a")
plt.title("Units Sold by Product Category")
plt.xlabel("Category")
plt.ylabel("Units Sold")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(output_folder / "04_category_units.png", dpi=150)
plt.close()

# Chart 5: Orders by payment method
plt.figure(figsize=(7, 5))
payment_orders.plot(
    kind="pie",
    autopct="%1.0f%%",
    startangle=90,
    colors=["#3559e0", "#19a89a", "#f29a4a"]
)
plt.title("Orders by Payment Method")
plt.ylabel("")
plt.tight_layout()
plt.savefig(output_folder / "05_payment_methods.png", dpi=150)
plt.close()

# Chart 6: Order revenue distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Revenue_INR"], bins=12, color="#8c6be8", edgecolor="white")
plt.title("Distribution of Revenue per Order")
plt.xlabel("Revenue per Order (INR)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(output_folder / "06_order_revenue_distribution.png", dpi=150)
plt.close()

print("Dataset saved as retail_sales.csv")
print("Six charts saved in the charts folder")
print(f"Number of sample orders: {len(df)}")
print(f"Total sample revenue: ₹{df['Revenue_INR'].sum():,}")
print(f"Top month: {month_revenue.idxmax()}")
print(f"Top category: {category_revenue.idxmax()}")
print(f"Top region: {region_revenue.idxmax()}")
print("Note: These are generated sample results, not real business data.")