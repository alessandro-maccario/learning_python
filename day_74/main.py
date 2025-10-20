# 1. Let's find out how many different colour LEGO bricks are actually in production.
# Read the colors.csv file from the data folder and find the total number of unique colours.
# There's a number of different ways you can accomplish this. Maybe try using the .nunique() from Pandas.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/colors.csv")
# How many unique colors of lego do you have in the data?
# print("Unique colors: ", df["name"].nunique())
# print("####################################")

# 2. Figure out how many of the LEGO colours are transparent compared to how many colours are opaque.
# See if you can Google your way to finding at least two different ways of arriving at the answer.
# print(df.groupby(by="is_trans").count()["id"])
# print("####################################")


# 3. Exploring the sets.csv
# 3a. In which year were the first LEGO sets released and what were these sets called?
df_sets = pd.read_csv("data/sets.csv")
# print(df_sets.sort_values(by="year").head(1))
# print("####################################")

# 3b. How many different products did the LEGO company sell in their first year of operation?
# print(
#     "How many different products did the LEGO company sell in their first year of operation? -> ",
#     df_sets[df_sets["year"] == 1949].groupby(by="name").nunique().shape[0],
# )
# print("####################################")

# 3c. What are the top 5 LEGO sets with the most number of parts?
# print(df_sets.sort_values("num_parts", ascending=False).head(5))
# print("####################################")

# 4. Create a new Series called sets_by_year which has the years as the index and the number of sets as the value
sets_by_year = df_sets.groupby("year").count()
# print("Sets by Year:", sets_by_year.sort_values(by=["year"])["set_num"].head())

# 5. display the values using a line chart

# defin the figure boundaries
# plt.figure(figsize=(16, 10))
# for column in sets_by_year.columns:
#     plt.plot(
#         sets_by_year.index[:-2],
#         sets_by_year[column][:-2],
#         label=sets_by_year[column].name,
#     )

# # define x and y-axis
# plt.xlabel("Date", fontsize=14)
# plt.ylabel("Number of Posts", fontsize=14)
# display the plot
# plt.show()

# 6. Calculate the themes by year
themes_by_year = df_sets.groupby("year").agg({"theme_id": pd.Series.nunique})
# print("Themes by Year:", themes_by_year)


# # define the figure boundaries
# plt.figure(figsize=(16, 10))
# for column in themes_by_year.columns:
#     plt.plot(
#         themes_by_year.index[:-2],
#         themes_by_year[column][:-2],
#         label=themes_by_year[column].name,
#     )

# # define x and y-axis
# plt.xlabel("Date", fontsize=14)
# plt.ylabel("Number of Themes", fontsize=14)
# # display the plot
# plt.show()


# 7. Have LEGO sets become larger and more complex over time?
parts_per_set = df_sets.groupby("year").agg({"num_parts": pd.Series.mean})
# print(parts_per_set)


# # define the figure boundaries
# plt.figure(figsize=(16, 10))
# for column in themes_by_year.columns:
#     plt.scatter(
#         themes_by_year.index[:-2],
#         themes_by_year[column][:-2],
#         label=themes_by_year[column].name,
#     )

# # define x and y-axis
# plt.xlabel("Date", fontsize=14)
# plt.ylabel("Number of Parts", fontsize=14)
# # display the plot
# plt.show()


# 8. Read in the themes.csv
df_themes = pd.read_csv("data/themes.csv")
print(list(df_themes[df_themes["name"] == "Star Wars"]["id"]))

print(df_sets[df_sets["theme_id"] == 18])
