import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

# 1. Look at the first 5 rows of the dataframe
print(df.head())

# 2. How many rows and columns the dataframe has?
print("Number of Rows:", df.shape[0], "|", "Number of columns:", df.shape[1])

# 3. Count the number of entries in each column.
print("Count the number of entries in each column:\n", df.count())

# 4. Count the number of posts per language
print(
    "Count the number of posts per language:\n",
    df.groupby("TAG").sum().sort_values("POSTS"),
)

# 5. Convert the DATE column from string to datetime
df["DATE"] = pd.to_datetime(df["DATE"])

# 6. Pivot the DataFrame so that each row is a date and each column is a programming language? Store the result under a variable called reshaped_df
pivoted_df = df.pivot(index="DATE", columns="TAG", values="POSTS").fillna(0)
print(
    "PIVOTED:\n",
    pivoted_df,
    "\n",
    "Number of rows:",
    pivoted_df.shape[0],
    "Number of columns:",
    pivoted_df.shape[1],
)


# 7. Show a line chart for the popularity of a programming, by taking the rolling mean of a fixed window
# The window is number of observations that are averaged
roll_df = pivoted_df.rolling(window=6).mean()

# defin the figure boundaries
plt.figure(figsize=(16, 10))
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)

# define x and y-axis
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.legend(fontsize=16)
# set lower and upper limit for the plot
plt.ylim(0, 35000)
# display the plot
plt.show()
