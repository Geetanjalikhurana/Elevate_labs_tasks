# Data Analysis with Pandas - Interview Questions & Answers

This document provides clear, concise, and technical answers to the 10 core Pandas and Data Analysis interview questions included in Elevate Labs Task 5.

---

### 1. What is Pandas used for?
**Answer:**
Pandas is an open-source Python data analysis and manipulation library. It is widely used for:
- Loading, reading, and writing structured data across various file formats (CSV, Excel, JSON, SQL, Parquet).
- Data cleaning, pre-processing, handling missing values (`NaN`), deduplication, and type conversion.
- Data manipulation, indexing, slicing, reshaping, joining, merging, and pivoting.
- Exploratory Data Analysis (EDA), statistical summary computation (`describe()`, `mean()`, `median()`), and aggregation with `groupby()`.
- Data visualization integration with Matplotlib and Seaborn.

---

### 2. What’s a DataFrame?
**Answer:**
A **DataFrame** is a 2-dimensional, size-mutable, tabular data structure in Pandas with labeled axes (rows and columns).
- **Rows** are indexed by index labels (or default numeric positions `0, 1, 2, ...`).
- **Columns** are series objects that can hold different data types (integer, float, string, datetime, boolean).
- It can be thought of as a spreadsheet, SQL table, or dictionary of Series objects.

```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Product': ['Laptop', 'Smartphone', 'Desk'],
    'Price': [1200, 800, 350],
    'In_Stock': [True, True, False]
}
df = pd.DataFrame(data)
print(df)
```

---

### 3. How do you read a CSV file?
**Answer:**
You read a CSV file in Pandas using the `pd.read_csv()` function:

```python
import pandas as pd

# Reading CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')

# Optional parameters for customized reading:
# df = pd.read_csv('sales_data.csv', parse_dates=['Date'], index_col='OrderID')
```

---

### 4. What is groupby()?
**Answer:**
`groupby()` is a powerful Pandas method used to split data into groups based on criteria, apply a function (e.g., `sum()`, `mean()`, `count()`, `agg()`), and combine the results into a new Data Structure (known as the **Split-Apply-Combine** pattern).

```python
# Group by Category and compute sum of Total_Sales
category_sales = df.groupby('Category')['Total_Sales'].sum()

# Group by multiple columns (Region and Category) with multiple aggregations
detailed_summary = df.groupby(['Region', 'Category']).agg({
    'Total_Sales': 'sum',
    'Units_Sold': 'mean'
})
```

---

### 5. How do you filter rows?
**Answer:**
Rows in Pandas can be filtered using boolean indexing, `query()`, or `loc[]`:

```python
# 1. Boolean Indexing
electronics = df[df['Category'] == 'Electronics']

# 2. Multiple Conditions (using & for AND, | for OR)
high_sales = df[(df['Category'] == 'Electronics') & (df['Total_Sales'] > 5000)]

# 3. Using .loc[]
furniture_north = df.loc[(df['Category'] == 'Furniture') & (df['Region'] == 'North')]

# 4. Using query()
high_units = df.query("Units_Sold > 20")
```

---

### 6. Difference between `loc[]` and `iloc[]`?
**Answer:**
Both `.loc[]` and `.iloc[]` are used for selecting rows and columns from a DataFrame, but they differ in indexing mechanisms:

| Feature | `.loc[]` | `.iloc[]` |
| :--- | :--- | :--- |
| **Indexing Type** | **Label-based** indexing | **Integer position-based** indexing |
| **Row Selection** | Uses row index labels or boolean arrays | Uses zero-based integer index positions (`0` to `len-1`) |
| **Column Selection**| Uses column names (e.g., `'Category'`) | Uses column integer position (e.g., `2`) |
| **Slicing Behavior**| **Inclusive** of start and stop labels (`'A':'C'`) | **Exclusive** of the stop index (`0:3` gets 0, 1, 2) |

```python
# loc example (Label-based)
df.loc[0:4, ['Product', 'Total_Sales']]

# iloc example (Integer position-based)
df.iloc[0:4, 4:8]  # selects rows 0..3 and columns 4..7
```

---

### 7. What does `.head()` do?
**Answer:**
`.head(n)` returns the first `n` rows of a DataFrame (default is `n=5`). It is commonly used during initial data exploration to inspect column names, sample data values, and layout.

```python
# View top 5 rows
print(df.head())

# View top 10 rows
print(df.head(10))
```

---

### 8. How can you create a bar chart?
**Answer:**
Bar charts can be created using Pandas directly (`.plot(kind='bar')`) or using plotting libraries like Matplotlib / Seaborn:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Using Pandas plot
df.groupby('Category')['Total_Sales'].sum().plot(kind='bar', color='skyblue')
plt.ylabel('Total Sales ($)')
plt.show()

# 2. Using Seaborn (Recommended for styling)
sns.barplot(data=df, x='Category', y='Total_Sales', estimator=sum, errorbar=None)
plt.title('Total Sales by Category')
plt.show()
```

---

### 9. What’s the shape of a DataFrame?
**Answer:**
The `.shape` attribute returns a tuple representing the dimensions of the DataFrame as `(number_of_rows, number_of_columns)`.

```python
# Check DataFrame dimensions
dimensions = df.shape
print(f"Rows: {dimensions[0]}, Columns: {dimensions[1]}")
# Example Output: Rows: 30, Columns: 9
```

---

### 10. What is NaN?
**Answer:**
`NaN` stands for **Not a Number**. It is a special floating-point value defined by standard IEEE 754 used in Pandas and NumPy to represent missing, undefined, or unrecorded data.

**Key functions for handling `NaN` in Pandas:**
- `df.isnull()` or `df.isna()`: Identifies missing values.
- `df.isnull().sum()`: Counts missing values per column.
- `df.dropna()`: Drops rows or columns containing missing values.
- `df.fillna(value)`: Replaces `NaN` with a specific value or statistic (mean, median, mode).

```python
# Check for NaNs
print(df.isnull().sum())

# Fill NaN with 0 or mean
df['Total_Sales'].fillna(df['Total_Sales'].mean(), inplace=True)
```
