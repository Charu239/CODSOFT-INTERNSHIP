import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# CODSOFT TASK 2 - EXPLORATORY DATA ANALYSIS
# ==========================================

# 1. Load the dataset
df = pd.read_csv("dataset2.csv")

# Convert date column to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 2. Examine dataset structure
print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

# 3. Descriptive statistics
print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe(include="all"))

# 4. Basic business metrics
total_sales = df["Sales"].sum()
average_order_value = df["Sales"].mean()
median_order_value = df["Sales"].median()
total_quantity = df["Quantity"].sum()
return_rate = (df["Returned"].eq("Yes").mean()) * 100

print("\n--- KEY METRICS ---")
print("Total Orders:", len(df))
print("Total Quantity Sold:", total_quantity)
print("Total Sales:", round(total_sales, 2))
print("Average Order Value:", round(average_order_value, 2))
print("Median Order Value:", round(median_order_value, 2))
print("Return Rate:", round(return_rate, 2), "%")

# 5. Sales by category
category_sales = df.groupby("Category")["Sales"].agg(
    Total_Sales="sum",
    Average_Sales="mean",
    Orders="count"
).sort_values("Total_Sales", ascending=False)

print("\n--- SALES BY CATEGORY ---")
print(category_sales)

# 6. Sales by region
region_sales = df.groupby("Region")["Sales"].agg(
    Total_Sales="sum",
    Average_Sales="mean",
    Orders="count"
).sort_values("Total_Sales", ascending=False)

print("\n--- SALES BY REGION ---")
print(region_sales)

# 7. Customer type analysis
customer_analysis = df.groupby("Customer_Type")["Sales"].agg(
    Total_Sales="sum",
    Average_Sales="mean",
    Orders="count"
).sort_values("Total_Sales", ascending=False)

print("\n--- CUSTOMER TYPE ANALYSIS ---")
print(customer_analysis)

# 8. Payment method analysis
payment_analysis = df.groupby("Payment_Method")["Sales"].agg(
    Total_Sales="sum",
    Average_Sales="mean",
    Orders="count"
).sort_values("Total_Sales", ascending=False)

print("\n--- PAYMENT METHOD ANALYSIS ---")
print(payment_analysis)

# 9. Monthly sales trend
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n--- MONTHLY SALES ---")
print(monthly_sales)

# 10. Correlation analysis
numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Sales"
]

correlation = df[numeric_columns].corr()

print("\n--- CORRELATION MATRIX ---")
print(correlation)

# 11. Outlier detection using IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_bound) |
    (df["Sales"] > upper_bound)
]

print("\n--- OUTLIER ANALYSIS ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of Outliers:", len(outliers))

print("\n--- OUTLIER RECORDS ---")
print(outliers[[
    "Order_ID",
    "Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Sales"
]].head(20))

# ==========================================
# 12. VISUAL ANALYSIS
# ==========================================

sns.set_theme(style="whitegrid")

# Chart 1: Sales by Category
plt.figure(figsize=(9, 5))
sns.barplot(
    data=df,
    x="Category",
    y="Sales",
    estimator="sum",
    errorbar=None
)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

# Chart 2: Monthly Sales Trend
plt.figure(figsize=(11, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    estimator="sum",
    errorbar=None
)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Chart 4: Sales Distribution
plt.figure(figsize=(9, 5))
sns.histplot(df["Sales"], bins=30, kde=True)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Chart 5: Quantity vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Quantity",
    y="Sales",
    hue="Category"
)
plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Chart 6: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 13. Save analysis outputs if required
category_sales.to_csv("category_sales_summary.csv")
region_sales.to_csv("region_sales_summary.csv")
monthly_sales.to_csv("monthly_sales_summary.csv")
outliers.to_csv("sales_outliers.csv", index=False)

print("\nEDA completed successfully.")