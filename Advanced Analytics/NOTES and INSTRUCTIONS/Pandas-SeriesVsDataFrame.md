#Series vs DataFrame

Pandas Series and DataFrames are fundamental data structures in the Pandas library, but they represent data in different dimensions:

##Series:
- **One-dimensional**: A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.).
- **Single column**: It can be thought of as a single column of data, similar to a column in a spreadsheet or a SQL table.
- **Index**: Each element in a Series has an associated label, called its index, which can be custom-defined (e.g., strings, integers, dates).
- **Example**: A list of temperatures for a single city over several days would be well-represented as a Series, where the index could be the dates. 
###Pandas Series = NumPy Array+ Labelled Index + One data column

##DataFrame:
- **Two-dimensional**: A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It is essentially a tabular data structure, like a spreadsheet or a SQL table.
- **Collection of Series**: A DataFrame can be considered a collection of Series objects, where each column in the DataFrame is a distinct Series sharing the same index.
- **Rows and Columns**: It has both row and column labels, allowing for flexible indexing and selection of data.
- **Example**: Data for multiple cities, including temperature, humidity, and wind speed, would be stored in a DataFrame, with cities as rows and meteorological data as columns. 

---

Basic data structure: **Numpy array**

Add a labelled index and keep only one data column: **Pandas Series**

Allow multiple data columns: **Pandas DataFrame**

##NumPy array -> Pandas Series -> Pandas DataFrame


