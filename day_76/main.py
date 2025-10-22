import pandas as pd

# 1. How many rows and columns does df_apps have?
df_app = pd.read_csv("data/apps.csv")
print("Number of rows and columns:\n", df_app.shape, "\n")

# 2. What are the column names?
print("Column names:\n", df_app.columns, "\n")

# 3. What does the data look like? Look at a random sample of 5 different rows with .sample()
print("Sample Data:\n", df_app.sample(5), "\n")

# 4. Remove the columns called Last_Updated and Android_Version from the DataFrame. Columns not used.
df_app = df_app.drop(columns=["Last_Updated", "Android_Ver"])

# 5. How many rows have a NaN value in the Rating column? Create df_apps_clean that does not include these rows.
df_apps_clean = df_app.dropna(subset=["Rating"])
print("Missing values in ratings:\n", df_app.shape[0] - df_apps_clean.shape[0])

# 6. Are there any duplicates in data? Check for duplicates using the .duplicated() function
print("\nNumber of duplicates:\n", df_apps_clean.duplicated().sum())

# 7. Use .drop_duplicates() to remove any duplicates from df_apps_clean
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
print(df_apps_clean.shape[0])
