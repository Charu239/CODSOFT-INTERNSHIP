import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# TASK 5 - WEB DATA EXTRACTION & ANALYSIS
# ==========================================

# Load scraped dataset
df = pd.read_csv("dataset5.csv")

print("====================================")
print("WEB DATA EXTRACTION & ANALYSIS")
print("====================================")

# ------------------------------------------
# 1. Dataset Overview
# ------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 10 Records:")
print(df.head(10))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# ------------------------------------------
# 2. Missing Values
# ------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# 3. Duplicate Records
# ------------------------------------------

print("\nDuplicate Records:")
print(df.duplicated().sum())

# ------------------------------------------
# 4. Descriptive Statistics
# ------------------------------------------

print("\nDescriptive Statistics:")
print(df.describe())

# ------------------------------------------
# 5. Price Analysis
# ------------------------------------------

print("\n====================================")
print("PRICE ANALYSIS")
print("====================================")

print("Average Price:")
print("£", round(df["Price"].mean(), 2))

print("\nMinimum Price:")
print("£", round(df["Price"].min(), 2))

print("\nMaximum Price:")
print("£", round(df["Price"].max(), 2))

print("\nMedian Price:")
print("£", round(df["Price"].median(), 2))

# ------------------------------------------
# 6. Rating Analysis
# ------------------------------------------

print("\n====================================")
print("RATING ANALYSIS")
print("====================================")

rating_counts = df["Rating"].value_counts()

print(rating_counts)

# ------------------------------------------
# 7. Average Price by Rating
# ------------------------------------------

print("\nAverage Price by Rating:")

rating_price = df.groupby("Rating")["Price"].mean().sort_values(
    ascending=False
)

print(rating_price)

# ------------------------------------------
# 8. Availability Analysis
# ------------------------------------------

print("\n====================================")
print("AVAILABILITY ANALYSIS")
print("====================================")

print(df["Availability"].value_counts())

# ------------------------------------------
# 9. Most Expensive Books
# ------------------------------------------

print("\n====================================")
print("TOP 10 MOST EXPENSIVE BOOKS")
print("====================================")

expensive_books = df.sort_values(
    "Price",
    ascending=False
).head(10)

print(
    expensive_books[
        ["Title", "Price", "Rating", "Availability"]
    ]
)

# ------------------------------------------
# 10. Cheapest Books
# ------------------------------------------

print("\n====================================")
print("TOP 10 CHEAPEST BOOKS")
print("====================================")

cheap_books = df.sort_values(
    "Price",
    ascending=True
).head(10)

print(
    cheap_books[
        ["Title", "Price", "Rating", "Availability"]
    ]
)

# ==========================================
# VISUALIZATIONS
# ==========================================

sns.set_theme(style="whitegrid")

# ------------------------------------------
# Chart 1 - Rating Distribution
# ------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Rating"
)

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 2 - Price Distribution
# ------------------------------------------

plt.figure(figsize=(9, 5))

sns.histplot(
    df["Price"],
    bins=30,
    kde=True
)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 3 - Average Price by Rating
# ------------------------------------------

plt.figure(figsize=(8, 5))

rating_price.plot(
    kind="bar"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 4 - Availability
# ------------------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Availability"
)

plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Chart 5 - Price vs Rating
# ------------------------------------------

rating_order = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five"
]

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=df,
    x="Rating",
    y="Price",
    order=rating_order
)

plt.title("Price Distribution by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Save analysis summaries
# ------------------------------------------

rating_counts.to_csv("rating_summary.csv")

rating_price.to_csv("rating_price_summary.csv")

expensive_books.to_csv(
    "top_10_expensive_books.csv",
    index=False
)

cheap_books.to_csv(
    "top_10_cheap_books.csv",
    index=False
)

print("\n====================================")
print("EDA COMPLETED SUCCESSFULLY")
print("====================================")