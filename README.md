# Retail Sales EDA Using Pandas

This project explores generated sample retail sales data using Python, Pandas and Matplotlib.

## Dataset

`retail_sales.csv` contains 174 sample orders for January–December 2025. Each row has an order ID, month, region, category, units, unit price, revenue and payment method.

**The data is generated for this class project. It does not represent a real shop or company.**

## Analysis

The Python script groups the data and creates six charts: monthly revenue, category revenue, regional revenue, units by category, payment method and order revenue distribution.

## Sample findings

- Total sample revenue: ₹3,144,429
- November has the highest monthly revenue: ₹439,022
- Electronics has the highest category revenue: ₹2,169,914
- South has the highest regional revenue: ₹950,725
- Home & Kitchen has the most units sold: 164

These findings describe only the generated sample.

## Run the analysis

Install the required packages:

`python -m pip install pandas matplotlib`

Then run:

`python retail_sales_eda.py`

The script saves the dataset as `retail_sales.csv` and the six chart images in a `charts` folder.
