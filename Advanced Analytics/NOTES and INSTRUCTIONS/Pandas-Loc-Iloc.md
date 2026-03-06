#Loc-Iloc

In Pandas, .loc and .iloc are used for selecting data from a DataFrame, but they differ in their indexing method:

##.loc (Label-based indexing):

- Selects data based on the labels of rows and columns.
- Takes row labels and column labels as arguments.
- When slicing with labels, the end label is inclusive.
- Can be used with Boolean arrays for conditional selection. 
Example:
Python

import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}

df = pd.DataFrame(data, index=['rowA', 'rowB', 'rowC'])

### Select a single cell by label
value = df.loc['rowB', 'col2']

print(f"Value at 'rowB', 'col2': {value}")

### Select a row by label
row = df.loc['rowA']

print(f"\nRow 'rowA':\n{row}")

## Select multiple rows and columns by label slicing (inclusive)

subset = df.loc['rowA':'rowB', 'col1':'col2']

print(f"\nSubset using .loc slicing:\n{subset}")

##.iloc (Integer-location based indexing):

- Selects data based on the integer positions of rows and columns (0-based indexing).

- Takes integer indices for rows and columns as arguments.

- When slicing with integers, the end index is exclusive (standard Python slicing behavior). 

Example:
Python

import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}

df = pd.DataFrame(data, index=['rowA', 'rowB', 'rowC'])

### Select a single cell by integer position
value = df.iloc[1, 1] # row index 1, column index 1

print(f"Value at index 1, 1: {value}")

### Select a row by integer position
row = df.iloc[0] # first row

print(f"\nFirst row using .iloc:\n{row}")

### Select multiple rows and columns by integer slicing (exclusive)

subset = df.iloc[0:2, 0:2] # rows 0 and 1, columns 0 and 1

print(f"\nSubset using .iloc slicing:\n{subset}")

##Key Differences Summarized:
1. Indexing Method: .loc uses labels, .iloc uses integer positions.
- Slicing Inclusivity: .loc slicing is inclusive of the end label; .iloc slicing is exclusive of the end integer position.
- Flexibility: .loc is more flexible with custom or non-integer indices, while .iloc strictly adheres to integer positions.