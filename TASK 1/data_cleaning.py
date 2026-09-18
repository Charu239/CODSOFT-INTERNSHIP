import pandas as pd

# ----------------------------------------------------
# STEP 1: LOAD THE DATASET & INSPECT
# ----------------------------------------------------
df = pd.read_csv('dataset1.csv')

print("Initial row count:", len(df))
print("\nMissing values before cleaning:")
print(df.isnull().sum())


# ----------------------------------------------------
# STEP 2: REMOVE DUPLICATE ROWS
# ----------------------------------------------------
df = df.drop_duplicates()
print("\nRow count after removing duplicates:", len(df))


# ----------------------------------------------------
# STEP 3: CLEAN EXTRA SPACES FROM TEXT COLUMNS
# ----------------------------------------------------
df['Name'] = df['Name'].str.strip()
df['Department'] = df['Department'].str.strip()
df['City'] = df['City'].str.strip()
df['City'] = df['City'].str.title()  # Fixes uppercase/lowercase (e.g., 'new york' -> 'New York')
df['Education_Level'] = df['Education_Level'].str.strip()
df['Performance_Rating'] = df['Performance_Rating'].str.strip()
df['Work_Mode'] = df['Work_Mode'].str.strip()


# ----------------------------------------------------
# STEP 4: CLEAN SYMBOLS & CONVERT TO NUMBERS
# ----------------------------------------------------
# Remove '$' and ',' from Salary
df['Salary'] = df['Salary'].str.replace('$', '', regex=False)
df['Salary'] = df['Salary'].str.replace(',', '', regex=False)
df['Salary'] = pd.to_numeric(df['Salary'])

# Remove '%' from Bonus_Percent
df['Bonus_Percent'] = df['Bonus_Percent'].str.replace('%', '', regex=False)
df['Bonus_Percent'] = pd.to_numeric(df['Bonus_Percent'])

# Extract numbers from Experience_Years (e.g., "5 years" -> 5)
df['Experience_Years'] = df['Experience_Years'].astype(str).str.extract('(\d+)')
df['Experience_Years'] = pd.to_numeric(df['Experience_Years'])


# ----------------------------------------------------
# STEP 5: FILL MISSING VALUES (EMPTY CELLS)
# ----------------------------------------------------
# Fill empty text columns with 'Unknown'
df['Department'] = df['Department'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')
df['Education_Level'] = df['Education_Level'].fillna('Unknown')
df['Performance_Rating'] = df['Performance_Rating'].fillna('Unknown')
df['Work_Mode'] = df['Work_Mode'].fillna('Unknown')

# Fill empty number columns with the median (middle) value
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Experience_Years'] = df['Experience_Years'].fillna(df['Experience_Years'].median())
df['Projects_Completed'] = df['Projects_Completed'].fillna(df['Projects_Completed'].median())
df['Bonus_Percent'] = df['Bonus_Percent'].fillna(df['Bonus_Percent'].median())

# Convert numbers from float decimals to whole integers
df['Age'] = df['Age'].astype(int)
df['Projects_Completed'] = df['Projects_Completed'].astype(int)


# ----------------------------------------------------
# STEP 6: VERIFY & SAVE CLEANED DATASET
# ----------------------------------------------------
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save to a new CSV file
df.to_csv('cleaned_dataset1.csv', index=False)
print("\nCleaned dataset saved successfully as 'cleaned_dataset1.csv'!")