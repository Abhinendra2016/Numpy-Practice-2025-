import csv
import numpy as np
from collections import defaultdict
from datetime import datetime

# Step 1: Load CSV data
def load_sales_data(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

# Step 2: Convert values and structure data
def preprocess_data(data):
    for row in data:
        row['Date'] = datetime.strptime(row['Date'], '%Y-%m-%d')
        row['Units Sold'] = int(row['Units Sold'])
        row['Unit Price'] = float(row['Unit Price'])
        row['Revenue'] = row['Units Sold'] * row['Unit Price']
    return data

# Step 3: Monthly Revenue Growth
def calculate_monthly_revenue(data):
    monthly_revenue = defaultdict(float)
    for row in data:
        key = row['Date'].strftime('%Y-%m')
        monthly_revenue[key] += row['Revenue']
    months = sorted(monthly_revenue.keys())
    growth = []
    for i in range(1, len(months)):
        prev = monthly_revenue[months[i-1]]
        curr = monthly_revenue[months[i]]
        growth_rate = ((curr - prev) / prev) * 100 if prev else 0
        growth.append((months[i], growth_rate))
    return monthly_revenue, growth

# Step 4: Mean Sales Per Product
def mean_sales_per_product(data):
    product_sales = defaultdict(list)
    for row in data:
        product_sales[row['Product']].append(row['Units Sold'])
    mean_sales = {prod: np.mean(sales) for prod, sales in product_sales.items()}
    return mean_sales

# Step 5: Seasonal Trends (Average Sales per Month)
def seasonal_trends(data):
    monthly_units = defaultdict(list)
    for row in data:
        month = row['Date'].strftime('%m')
        monthly_units[month].append(row['Units Sold'])
    avg_sales = {month: np.mean(sales) for month, sales in monthly_units.items()}
    return avg_sales

# Step 6: Best & Worst Selling Products
def best_and_worst_selling(data):
    total_sales = defaultdict(int)
    for row in data:
        total_sales[row['Product']] += row['Units Sold']
    sorted_sales = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)
    return sorted_sales[0], sorted_sales[-1]

# Driver
if __name__ == "__main__":
    file_path = 'sales_data.csv'
    raw_data = load_sales_data(file_path)
    clean_data = preprocess_data(raw_data)

    print("\n📈 Monthly Revenue & Growth:")
    monthly_revenue, growth = calculate_monthly_revenue(clean_data)
    for month, revenue in monthly_revenue.items():
        print(f"{month}: ${revenue:.2f}")
    print("\n📊 Revenue Growth Rate:")
    for month, rate in growth:
        print(f"{month}: {rate:.2f}%")

    print("\n📦 Mean Sales per Product:")
    mean_sales = mean_sales_per_product(clean_data)
    for prod, avg in mean_sales.items():
        print(f"{prod}: {avg:.2f} units")

    print("\n🌦️ Seasonal Trends (Avg Sales by Month):")
    seasonal = seasonal_trends(clean_data)
    for month, avg in sorted(seasonal.items()):
        print(f"Month {month}: {avg:.2f} units")

    best, worst = best_and_worst_selling(clean_data)
    print("\n🏆 Best-Selling Product:", best)
    print("😞 Worst-Selling Product:", worst)
