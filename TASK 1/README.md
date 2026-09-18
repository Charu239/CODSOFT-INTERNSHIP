# CODSOFT Task 1 – Data Cleaning and Preprocessing

## 📌 Project Overview

This project was completed as part of my **CODSOFT Internship**.

The objective of this task was to import a dataset using **Python and Pandas**, inspect its structure, identify missing values and duplicate records, clean inconsistent data entries, correct data types, and prepare the dataset for further analysis.

The cleaned dataset was finally saved as a new CSV file.

---

## 🎯 Objectives

* Import the dataset using Python and Pandas
* Inspect the structure of the dataset
* Identify missing values
* Identify and remove duplicate records
* Clean inconsistent text entries
* Remove unnecessary symbols from numerical data
* Convert columns to appropriate data types
* Handle missing values
* Verify the cleaned dataset
* Save the cleaned dataset as a new CSV file

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **CSV**

---

## 📂 Project Files

| File                   | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `dataset1.csv`         | Original/raw dataset                                   |
| `cleaned_dataset1.csv` | Cleaned dataset generated after preprocessing          |
| `task1.py`             | Python script used for data cleaning and preprocessing |
| `README.md`            | Project documentation                                  |

---

## 🔄 Data Cleaning Process

### 1. Load and Inspect Dataset

The dataset was loaded using Pandas and the initial row count and missing values were checked.

```python
df = pd.read_csv('dataset1.csv')
```

The program also checks missing values using:

```python
df.isnull().sum()
```

---

### 2. Remove Duplicate Records

Duplicate rows were identified and removed using Pandas:

```python
df = df.drop_duplicates()
```

---

### 3. Clean Text Data

Extra spaces and inconsistent capitalization were cleaned from text columns such as:

* Name
* Department
* City
* Education Level
* Performance Rating
* Work Mode

The city values were also standardized using title case.

---

### 4. Convert Numerical Data

Symbols and text formatting were removed from numerical columns.

For example:

* `$` and `,` were removed from the **Salary** column.
* `%` was removed from the **Bonus_Percent** column.
* Numeric values were extracted from **Experience_Years**.

The cleaned values were then converted into appropriate numeric data types.

---

### 5. Handle Missing Values

Missing values in categorical columns were replaced with:

```text
Unknown
```

For numerical columns, missing values were filled using the **median value** of the respective column.

This was applied to columns such as:

* Salary
* Age
* Experience Years
* Projects Completed
* Bonus Percent

---

### 6. Verify and Save Cleaned Dataset

After cleaning, missing values were checked again to verify the preprocessing.

The final dataset was saved as:

```text
cleaned_dataset1.csv
```

using:

```python
df.to_csv('cleaned_dataset1.csv', index=False)
```

---

## 📊 Key Data Preparation Techniques

| Technique           | Purpose                              |
| ------------------- | ------------------------------------ |
| `drop_duplicates()` | Remove duplicate records             |
| `str.strip()`       | Remove extra spaces                  |
| `str.title()`       | Standardize text capitalization      |
| `str.replace()`     | Remove unwanted symbols              |
| `pd.to_numeric()`   | Convert values to numeric data types |
| `fillna()`          | Handle missing values                |
| `median()`          | Fill missing numerical values        |
| `to_csv()`          | Export cleaned dataset               |

---

## ✅ Outcome

The dataset was successfully:

* Inspected
* Cleaned
* De-duplicated
* Standardized
* Converted to appropriate data types
* Processed for missing values
* Verified after cleaning
* Exported as a new CSV file

This prepared the dataset for further **data analysis and visualization** using Python and Pandas.

---

## 👨‍💻 Internship

**Internship:** CODSOFT
**Task:** Task 1 – Data Cleaning and Preprocessing
**Tools:** Python, Pandas, CSV

---

## 📌 Conclusion

This task provided practical experience in **data cleaning and preprocessing using Pandas**. It demonstrated how raw data can be transformed into a cleaner and more structured dataset suitable for further analysis.

