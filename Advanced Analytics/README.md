# Advanced-Analytics

Tips- Always Experiment, but Stick to one syntax practically.
import pandas as pd

# Load the dataset
df = pd.read_csv('titanic.csv')

# Q1: Import the dataset and print top 15 rows for columns
# 'gender' (substituted for 'Name'), 'Age', 'Pclass', 'Embarked', and 'Survived' with no missing data.

# Columns to check for missing data: 'age', 'pclass', 'embarked', 'survived'
columns_to_filter = ['age', 'pclass', 'embarked', 'survived']

# Filter rows with no missing data in the specified columns
df_q1 = df.dropna(subset=columns_to_filter)

# Select the top 15 rows and the specified columns
columns_to_display = ['gender', 'age', 'pclass', 'embarked', 'survived']
top_15_rows = df_q1[columns_to_display].head(15)

# Convert the result to a CSV file to display
top_15_rows.to_csv('q1_top_15_rows.csv', index=False)

print("\nTop 15 rows after filtering (using 'gender' instead of 'Name'):")
print(top_15_rows)