import requests
from bs4 import BeautifulSoup
import pandas as pd

# Starting URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# List to store all book data
books_data = []

# Scrape all 50 pages
for page in range(1, 51):

    print(f"Scraping page {page}...")

    url = base_url.format(page)

    # Send request
    response = requests.get(url)

    # Check successful response
    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # Extract information
    for book in books:

        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find(
            "p", class_="price_color"
        ).text.strip()

        # Rating
        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        # Availability
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        # Product URL
        product_url = book.h3.a["href"]

        # Store information
        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })


# Convert to DataFrame
df = pd.DataFrame(books_data)


# ==========================================
# DATA CLEANING
# ==========================================

# Remove extra spaces
df["Title"] = df["Title"].str.strip()
df["Price"] = df["Price"].str.strip()
df["Rating"] = df["Rating"].str.strip()
df["Availability"] = df["Availability"].str.strip()


# Convert Price from text to numeric
df["Price"] = (
    df["Price"]
    .str.replace(r"[^\d.]", "", regex=True)
    .astype(float)
)


# ==========================================
# DATA INSPECTION
# ==========================================

print("\n================================")
print("SCRAPING COMPLETED")
print("================================")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 10 Records:")
print(df.head(10))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())


# ==========================================
# BASIC ANALYSIS
# ==========================================

print("\n================================")
print("BASIC ANALYSIS")
print("================================")

print("\nAverage Book Price:")
print("£", round(df["Price"].mean(), 2))

print("\nMinimum Book Price:")
print("£", round(df["Price"].min(), 2))

print("\nMaximum Book Price:")
print("£", round(df["Price"].max(), 2))

print("\nNumber of Books:")
print(len(df))

print("\nRating Distribution:")
print(df["Rating"].value_counts())


# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv("dataset5.csv", index=False)

print("\n================================")
print("DATASET SAVED")
print("================================")

print("File created: dataset5.csv")