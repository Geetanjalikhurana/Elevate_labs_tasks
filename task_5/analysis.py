import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure charts directory exists
os.makedirs("charts", exist_ok=True)

# Set visual style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_theme(style="whitegrid", palette="muted")

print("="*60)
print(" ELEVATE LABS - TASK 5: DATA ANALYSIS ON CSV FILES ")
print("="*60)

# Step 1: Load CSV using Pandas
df = pd.read_csv("sales_data.csv")

# Step 2: Basic Dataset Inspection
print("\n--- 1. First 5 Rows (.head()) ---")
print(df.head())

print("\n--- 2. Shape of DataFrame (.shape) ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- 3. Dataset Info & Missing Values ---")
print(df.info())
print("\nMissing Values Count per Column:")
print(df.isnull().sum())

# Step 3: Data Cleaning & Type Conversion
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# Step 4: Filtering Data using loc[] and iloc[]
print("\n--- 4. Data Filtering Examples ---")
print("\na) Filter Electronics category using loc[]:")
electronics_df = df.loc[df['Category'] == 'Electronics', ['Date', 'Product', 'Region', 'Total_Sales']]
print(electronics_df.head())

print("\nb) Accessing specific rows & columns using iloc[] (First 3 rows, columns 1 to 5):")
print(df.iloc[0:3, 1:6])

# Step 5: Aggregations using groupby() and sum()
print("\n--- 5. Aggregations using groupby() ---")

print("\na) Total Sales by Category:")
category_sales = df.groupby('Category')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)
print(category_sales)

print("\nb) Total Sales by Region:")
region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)
print(region_sales)

print("\nc) Monthly Sales Trend:")
monthly_sales = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Total_Sales'].sum().reset_index()
monthly_sales.columns = ['Month', 'Total_Sales']
print(monthly_sales)

print("\nd) Top 5 Selling Products by Revenue:")
top_products = df.groupby('Product')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)
print(top_products)

# Step 6: Data Visualizations & Exporting Charts
print("\n--- 6. Generating & Exporting Visualizations ---")

# Chart 1: Total Sales by Category (Bar Chart)
plt.figure(figsize=(8, 5))
ax = sns.barplot(data=category_sales, x='Category', y='Total_Sales', palette='viridis')
plt.title('Total Sales Revenue by Category', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
for p in ax.patches:
    ax.annotate(f'${p.get_height():,.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/sales_by_category.png', dpi=300)
plt.close()
print("Saved charts/sales_by_category.png")

# Chart 2: Total Sales by Region (Bar Chart)
plt.figure(figsize=(8, 5))
ax = sns.barplot(data=region_sales, x='Region', y='Total_Sales', palette='magma')
plt.title('Total Sales Revenue by Region', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
for p in ax.patches:
    ax.annotate(f'${p.get_height():,.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/sales_by_region.png', dpi=300)
plt.close()
print("Saved charts/sales_by_region.png")

# Chart 3: Monthly Sales Trend (Line Chart)
plt.figure(figsize=(9, 5))
sns.lineplot(data=monthly_sales, x='Month', y='Total_Sales', marker='o', linewidth=2.5, color='#2b5c8f', markersize=8)
plt.title('Monthly Sales Revenue Trend (2024)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
for i, row in monthly_sales.iterrows():
    plt.annotate(f'${row["Total_Sales"]:,.0f}', (row['Month'], row['Total_Sales']),
                 xytext=(0, 10), textcoords='offset points', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('charts/monthly_sales_trend.png', dpi=300)
plt.close()
print("Saved charts/monthly_sales_trend.png")

# Chart 4: Top Products by Revenue (Horizontal Bar Chart)
plt.figure(figsize=(9, 5))
ax = sns.barplot(data=top_products, y='Product', x='Total_Sales', palette='coolwarm')
plt.title('Top Selling Products by Revenue', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Total Sales ($)', fontsize=12)
plt.ylabel('Product', fontsize=12)
for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'${width:,.2f}', 
                (width, p.get_y() + p.get_height() / 2.), 
                ha='left', va='center', xytext=(8, 0), textcoords='offset points', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('charts/top_products.png', dpi=300)
plt.close()
print("Saved charts/top_products.png")

print("\nAnalysis completed successfully!")
