import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('train.csv', encoding='latin1')

# 2. Clean Columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

# 3. Data Formatting
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
df['year'] = df['order_date'].dt.year
df['month_name'] = df['order_date'].dt.month_name()

print("✅ Data Cleaning Completed. Analyzing Sales and Orders...")

# --- Setting the style ---
sns.set_theme(style="whitegrid")

# 📊 Plot 1: Total Sales by Category
plt.figure(figsize=(10, 6))
cat_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)
sns.barplot(x=cat_sales.index, y=cat_sales.values, palette='viridis')
plt.title('Total Sales Value by Category', fontsize=15)
plt.ylabel('Total Sales ($)')
plt.show()

# 📊 Plot 2: Top 5 Cities by Order Count
plt.figure(figsize=(10, 6))
top_cities = df['city'].value_counts().head(5)
sns.barplot(x=top_cities.values, y=top_cities.index, palette='coolwarm')
plt.title('Top 5 Cities by Number of Orders', fontsize=15)
plt.xlabel('Number of Orders')
plt.show()

# 📊 Plot 3: Sales Distribution by Region
plt.figure(figsize=(8, 8))
region_sales = df.groupby('region')['sales'].sum()
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Sales Distribution by Region', fontsize=15)
plt.show()

# 📊 Plot 4: Sales Trend Over the Years
plt.figure(figsize=(12, 6))
yearly_trend = df.groupby('year')['sales'].sum()
yearly_trend.plot(kind='line', marker='o', color='darkorange', linewidth=3)
plt.title('Annual Sales Growth Trend', fontsize=15)
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.show()