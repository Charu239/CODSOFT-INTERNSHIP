# CODSOFT Task 5 – Web Data Extraction & Analysis

## 📌 Project Overview

This project was completed as part of my **CODSOFT Data Analytics Internship – Task 5**.

The objective of this task was to collect publicly available data from a website using Python, extract structured information, clean and organize the collected data, and perform exploratory data analysis to identify trends and patterns.

For this project, I used **Books to Scrape**, a website designed for practicing web scraping.

---

## 🎯 Objectives

* Collect data from a publicly available website using Python.
* Extract structured information such as book titles, prices, ratings, and availability.
* Clean and organize the scraped data using Pandas.
* Save the extracted data into a CSV file.
* Perform exploratory data analysis.
* Identify pricing and rating patterns.
* Create visualizations to present the findings.

---

## 🌐 Data Source

**Website:** Books to Scrape

The scraper collected book information from **50 catalogue pages**, resulting in a dataset of **1,000 books**.

---

## 🛠️ Technologies Used

* **Python**
* **Requests** – for sending HTTP requests
* **BeautifulSoup** – for parsing HTML and extracting information
* **Pandas** – for data cleaning and analysis
* **Matplotlib** – for data visualization
* **Seaborn** – for statistical visualizations

---

## 📊 Dataset

The final dataset is saved as:

```text
dataset5.csv
```

### Dataset Columns

| Column         | Description                  |
| -------------- | ---------------------------- |
| `Title`        | Name of the book             |
| `Price`        | Book price in GBP            |
| `Rating`       | Book rating from One to Five |
| `Availability` | Stock availability           |
| `Product_URL`  | Product page URL             |

### Dataset Summary

* **Total Records:** 1,000
* **Total Columns:** 5
* **Missing Values:** 0
* **Duplicate Records:** 0
* **Average Book Price:** £35.07

---

## 🔎 Web Scraping Process

The project follows these steps:

1. Send HTTP requests to the website using `Requests`.
2. Parse the HTML using `BeautifulSoup`.
3. Locate individual book elements.
4. Extract:

   * Book title
   * Price
   * Rating
   * Availability
   * Product URL
5. Repeat the process across 50 pages.
6. Store the extracted information in a Pandas DataFrame.
7. Clean the price and text fields.
8. Export the final dataset to CSV.

---

## 🧹 Data Cleaning

The following cleaning operations were performed:

* Removed unnecessary spaces from text fields.
* Converted price values from text to numeric format.
* Checked for missing values.
* Checked for duplicate records.
* Verified data types.
* Prepared the dataset for further analysis.

---

## 📈 Exploratory Data Analysis

The following analyses were performed:

### Price Analysis

* Average book price
* Median book price
* Minimum book price
* Maximum book price
* Top 10 most expensive books
* Top 10 cheapest books

### Rating Analysis

* Rating distribution
* Number of books for each rating
* Average price by rating

### Availability Analysis

* Distribution of book availability
* Number of books in each availability category

---

## 📊 Visualizations

The project includes the following visualizations:

* **Book Rating Distribution**
* **Book Price Distribution**
* **Average Book Price by Rating**
* **Book Availability**
* **Price Distribution by Rating**

---

## 📁 Project Files

```text
Task5/
│
├── task5_scraping.py
├── task5_eda.py
├── dataset5.csv
├── rating_summary.csv
├── rating_price_summary.csv
├── top_10_expensive_books.csv
├── top_10_cheap_books.csv
└── CODSOFT_Task_5_Web_Data_Extraction_Report.docx
```

---

## ▶️ How to Run the Project

### 1. Install required libraries

```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
```

### 2. Run the web scraper

```bash
python task5_scraping.py
```

This will scrape the website and create:

```text
dataset5.csv
```

### 3. Run the EDA program

```bash
python task5_eda.py
```

This will perform the analysis and generate the visualizations and summary files.

---

## 💡 Key Findings

* The web scraper successfully collected **1,000 book records**.
* The dataset contained **no missing values**.
* The dataset contained **no duplicate records**.
* The average book price was **£35.07**.
* Book prices varied considerably across the scraped catalogue.
* Rating distribution was analyzed to understand how books were distributed across rating levels.
* Price differences across rating groups were examined using grouped analysis and visualizations.

---

## 📌 Conclusion

This project demonstrates an end-to-end **Web Data Extraction and Analysis** workflow using Python.

The project covers data collection through web scraping, HTML parsing, data cleaning, CSV creation, exploratory analysis, and visualization. It provided practical experience in working with real-world web data and preparing it for analytical use.


