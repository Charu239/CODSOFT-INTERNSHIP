# CODSOFT Task 2 – Exploratory Data Analysis (EDA)

## 📊 E-Commerce Sales Analysis

This project was completed as part of my **CODSOFT Data Analytics Internship**.

The objective of this task was to perform **Exploratory Data Analysis (EDA)** on an e-commerce sales dataset using Python. The analysis focuses on understanding sales performance, customer behavior, regional trends, payment methods, relationships between numerical variables, and unusual sales transactions.

---

## 🎯 Project Objectives

* Load and inspect the e-commerce dataset using Pandas
* Understand the structure and data types of the dataset
* Calculate descriptive statistics
* Analyze sales across different product categories
* Compare regional sales performance
* Analyze new vs. returning customers
* Examine monthly sales trends
* Analyze sales by payment method
* Identify relationships between numerical variables
* Detect potential sales outliers using the IQR method
* Create meaningful data visualizations
* Generate business-oriented insights from the analysis

---

## 📁 Dataset

The dataset contains **1,000 e-commerce orders recorded during 2025**.

It includes information about:

* Order details
* Customers
* Product categories
* Products
* Regions
* Customer types
* Quantity
* Unit price
* Discounts
* Sales
* Payment methods
* Return status

### Dataset Columns

| Column             | Description                    |
| ------------------ | ------------------------------ |
| `Order_ID`         | Unique order identifier        |
| `Order_Date`       | Date of order                  |
| `Customer_ID`      | Customer identifier            |
| `Category`         | Product category               |
| `Product`          | Product name                   |
| `Region`           | Customer/order region          |
| `Customer_Type`    | New or Returning customer      |
| `Quantity`         | Units purchased                |
| `Unit_Price`       | Price per unit                 |
| `Discount_Percent` | Discount applied               |
| `Sales`            | Net order sales value          |
| `Payment_Method`   | Payment method used            |
| `Returned`         | Whether the order was returned |

The dataset structure and column definitions are documented in the project report.

---

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Microsoft Word**

Pandas was used for data loading, processing, grouping, statistical analysis, correlation analysis, and outlier detection. Matplotlib and Seaborn were used for visual analysis.

---

## 🔍 Analysis Performed

### 1. Dataset Inspection

The dataset was inspected to understand:

* Number of rows and columns
* Column names
* Data types
* Missing values
* Duplicate records
* Descriptive statistics

The `Order_Date` column was converted into a proper datetime format before analysis.

### 2. Key Business Metrics

The following metrics were calculated:

* Total Orders
* Total Quantity Sold
* Total Sales
* Average Order Value
* Median Order Value
* Return Rate

### 3. Category Analysis

Sales were analyzed across different product categories to identify which categories generated the highest and lowest sales.

### 4. Regional Analysis

Sales performance was compared across:

* West
* Central
* South
* North
* East

### 5. Customer Analysis

The analysis compared:

* New Customers
* Returning Customers

using total sales, average order value, and number of orders.

### 6. Monthly Sales Trend

Monthly sales were calculated to identify changes in sales performance throughout 2025.

### 7. Payment Method Analysis

Sales performance was analyzed across different payment methods.

### 8. Correlation Analysis

Correlation was calculated between:

* Quantity
* Unit Price
* Discount Percentage
* Sales

The analysis identified the strength of relationships between numerical variables.

### 9. Outlier Detection

Potential sales outliers were identified using the **Interquartile Range (IQR)** method.

The project identified **120 potential sales outlier records**. These records were flagged for further investigation rather than automatically removed.

---

## 📈 Visualizations

The project includes the following visualizations:

1. **Total Sales by Category**
2. **Monthly Sales Trend**
3. **Total Sales by Region**
4. **Sales Distribution**
5. **Quantity vs Sales**
6. **Correlation Heatmap**

These visualizations were created using Matplotlib and Seaborn.

---

## 📊 Key Results

| Metric              |         Result |
| ------------------- | -------------: |
| Total Orders        |          1,000 |
| Total Quantity Sold |          2,010 |
| Total Sales         | ₹16,547,535.05 |
| Average Order Value |     ₹16,547.54 |
| Median Order Value  |      ₹4,783.20 |
| Return Rate         |          7.80% |
| Potential Outliers  |            120 |

### Important Findings

* Electronics generated the highest total sales at **₹12,117,124.98**.
* West recorded the highest regional sales.
* Returning customers generated **₹9,859,533.55** in sales.
* The highest monthly sales occurred in **January 2025**, at ₹1,999,394.09.
* Unit Price had the strongest numerical relationship with Sales based on absolute Pearson correlation.
* 120 records were identified as potential sales outliers using the IQR method.

---

## 📂 Project Files

```text
CODSOFT_TASK2/
│
├── dataset2.csv
├── task2.py
├── category_sales_summary.csv
├── region_sales_summary.csv
├── monthly_sales_summary.csv
├── sales_outliers.csv
├── Task2_Report.docx
└── README.md
```

### File Description

| File                         | Description                     |
| ---------------------------- | ------------------------------- |
| `dataset2.csv`               | Original e-commerce dataset     |
| `task2.py`                   | Python EDA analysis script      |
| `category_sales_summary.csv` | Category-wise sales summary     |
| `region_sales_summary.csv`   | Region-wise sales summary       |
| `monthly_sales_summary.csv`  | Monthly sales summary           |
| `sales_outliers.csv`         | Potential sales outlier records |
| `Task2_Report.docx`          | Detailed project report         |
| `README.md`                  | Project documentation           |

The Python script also exports the category, region, monthly sales, and outlier analysis results as CSV files.

---

## ▶️ How to Run the Project

### Step 1 – Install Python

Make sure Python is installed on your computer.

### Step 2 – Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 3 – Keep the Files in the Same Folder

Make sure the following files are in the project folder:

```text
dataset2.csv
task2.py
```

### Step 4 – Run the Python Script

```bash
python task2.py
```

The script will perform the EDA and generate the analysis outputs.

---

## 💡 Business Insights

The EDA provides an overview of e-commerce performance across products, categories, regions, customers, payment methods, and time.

The analysis shows where sales are concentrated and provides additional insight into numerical relationships and unusual transactions.

---

## 🎓 Internship

**Program:** CODSOFT Data Analytics Internship
**Task:** Task 2 – Exploratory Data Analysis
**Project:** E-Commerce Sales Analysis

This project demonstrates practical skills in:

* Data Analysis
* Exploratory Data Analysis
* Python
* Pandas
* NumPy
* Data Visualization
* Statistical Analysis
* Business Insights



⭐ If you find this project useful, feel free to explore the repository and review the analysis.

