import pandas as pd

# Step 1: Create a dictionary
data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', None, None, None],
    'Salary': [100, 200, None, None]
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Print the initial 2 and last 2 values
print("Initial 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))

# Step 4: Check total number of null values
print("\nTotal null values:\n", df.isnull().sum().sum())

# Step 5: Print detailed information
print("\nDataFrame info:")
print(df.info())

# Step 6: Drop rows with null values
df_no_null_rows = df.dropna()
print("\nDataFrame after dropping rows with nulls:\n", df_no_null_rows)

# Step 7: Drop columns with null values
df_no_null_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with nulls:\n", df_no_null_cols)

# Step 8: Fill null values in Salary with 300
df_salary_filled = df.copy()
df_salary_filled['Salary'].fillna(300, inplace=True)
print("\nDataFrame after filling Salary nulls with 300:\n", df_salary_filled)

# Step 9: Fill null values in Role with 'CEO'
df_role_filled = df.copy()
df_role_filled['Role'].fillna('CEO', inplace=True)
print("\nDataFrame after filling Role nulls with 'CEO':\n", df_role_filled)
