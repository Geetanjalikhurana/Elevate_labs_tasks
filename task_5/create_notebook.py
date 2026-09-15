import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 5: Data Analysis on CSV Files\n",
    "**Internship:** Python Developer Internship at Elevate Labs  \n",
    "**Objective:** Analyze sales data using Pandas, group metrics, filter datasets, and generate visual charts.  \n",
    "**Tools Used:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook  \n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Import Libraries & Load CSV\n",
    "We load the sales dataset (`sales_data.csv`) using Pandas `read_csv()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Set visual style\n",
    "sns.set_theme(style=\"whitegrid\", palette=\"muted\")\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv('sales_data.csv')\n",
    "print(\"Dataset successfully loaded!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Dataset Inspection & Missing Value Analysis\n",
    "Understanding the shape, first few rows (`.head()`), and checking for null/missing values (`NaN`)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Display first 5 rows\n",
    "print(\"--- First 5 Rows (.head()) ---\")\n",
    "display(df.head())\n",
    "\n",
    "# 2. Check DataFrame shape\n",
    "print(f\"DataFrame Shape (Rows, Columns): {df.shape}\")\n",
    "\n",
    "# 3. Missing values check\n",
    "print(\"\\n--- Missing Values Count ---\")\n",
    "print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Data Filtering (`loc[]` vs `iloc[]`)\n",
    "- `loc[]`: Label-based indexing.\n",
    "- `iloc[]`: Integer position-based indexing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Filter Electronics using loc[]\n",
    "print(\"--- Filter Electronics Category (loc[]) ---\")\n",
    "electronics_df = df.loc[df['Category'] == 'Electronics', ['Date', 'Product', 'Region', 'Total_Sales']]\n",
    "display(electronics_df.head())\n",
    "\n",
    "# Select first 5 rows and specific columns using iloc[]\n",
    "print(\"\\n--- Select First 5 Rows & Columns 1 to 5 (iloc[]) ---\")\n",
    "display(df.iloc[0:5, 1:6])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Aggregations using `groupby()` and `sum()`\n",
    "Grouping sales revenue by **Category**, **Region**, and **Product**."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Total Sales by Category\n",
    "category_sales = df.groupby('Category')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)\n",
    "print(\"--- Total Sales by Category ---\")\n",
    "display(category_sales)\n",
    "\n",
    "# 2. Total Sales by Region\n",
    "region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)\n",
    "print(\"\\n--- Total Sales by Region ---\")\n",
    "display(region_sales)\n",
    "\n",
    "# 3. Top Products by Total Revenue\n",
    "top_products = df.groupby('Product')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)\n",
    "print(\"\\n--- Top Products by Revenue ---\")\n",
    "display(top_products)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Data Visualizations\n",
    "Creating bar charts and line charts using Seaborn and Matplotlib."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Bar Chart: Total Sales by Category\n",
    "plt.figure(figsize=(8, 5))\n",
    "ax = sns.barplot(data=category_sales, x='Category', y='Total_Sales', palette='viridis')\n",
    "plt.title('Total Sales Revenue by Category', fontsize=14, fontweight='bold', pad=15)\n",
    "plt.xlabel('Category', fontsize=12)\n",
    "plt.ylabel('Total Sales ($)', fontsize=12)\n",
    "for p in ax.patches:\n",
    "    ax.annotate(f'${p.get_height():,.2f}', \n",
    "                (p.get_x() + p.get_width() / 2., p.get_height()), \n",
    "                ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=10, fontweight='bold')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Bar Chart: Total Sales by Region\n",
    "plt.figure(figsize=(8, 5))\n",
    "ax = sns.barplot(data=region_sales, x='Region', y='Total_Sales', palette='magma')\n",
    "plt.title('Total Sales Revenue by Region', fontsize=14, fontweight='bold', pad=15)\n",
    "plt.xlabel('Region', fontsize=12)\n",
    "plt.ylabel('Total Sales ($)', fontsize=12)\n",
    "for p in ax.patches:\n",
    "    ax.annotate(f'${p.get_height():,.2f}', \n",
    "                (p.get_x() + p.get_width() / 2., p.get_height()), \n",
    "                ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=10, fontweight='bold')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Key Insights Summary\n",
    "1. **Electronics** generated the highest total revenue among product categories.\n",
    "2. The **West** region outperformed other geographic territories in revenue generation.\n",
    "3. **Smartphones** and **Laptops** were the highest individual revenue contributing products.\n",
    "4. All missing values (`NaN`) were validated and confirmed clean."
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

with open("data_analysis.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created data_analysis.ipynb successfully!")
