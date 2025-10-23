import pandas as pd
import plotly.express as px

# 1. How many rows and columns does df_apps have?
df_app = pd.read_csv("data/apps.csv")
# print("Number of rows and columns:\n", df_app.shape, "\n")

# 2. What are the column names?
# print("Column names:\n", df_app.columns, "\n")

# 3. What does the data look like? Look at a random sample of 5 different rows with .sample()
# print("Sample Data:\n", df_app.sample(5), "\n")

# 4. Remove the columns called Last_Updated and Android_Version from the DataFrame. Columns not used.
df_app = df_app.drop(columns=["Last_Updated", "Android_Ver"])

# 5. How many rows have a NaN value in the Rating column? Create df_apps_clean that does not include these rows.
df_apps_clean = df_app.dropna(subset=["Rating"])
# print("Missing values in ratings:\n", df_app.shape[0] - df_apps_clean.shape[0])

# 6. Are there any duplicates in data? Check for duplicates using the .duplicated() function
# print("\nNumber of duplicates:\n", df_apps_clean.duplicated().sum())

# 7. Use .drop_duplicates() to remove any duplicates from df_apps_clean
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
# print(df_apps_clean.shape[0])

# 8. Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
# print(df_apps_clean.sort_values(by=["Rating"], ascending=False))

# 9. What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data, do you think there could be a limit in place or can developers make apps as large as they please?
# print(df_apps_clean.sort_values(by=["Size_MBs"], ascending=False))

# 10. Which apps have the highest number of reviews? Are there any paid apps among the top 50?
# print(df_apps_clean.sort_values(by=["Reviews"], ascending=False).head(50))


# 11. Count the number of occurrences of each rating with
ratings = df_apps_clean.Content_Rating.value_counts()

# 12. Create a pie chart plot with plotly
# fig = px.pie(
#     labels=ratings.index,
#     values=ratings.values,
#     title="Content Rating",
#     names=ratings.index,
#     hole=0.6,
# )
# fig.update_traces(textposition="inside", textfont_size=15, textinfo="percent")

# fig.show()


# 13. How many apps had over 1 billion (that's right - BILLION) installations?
df_apps_clean["Installs"] = pd.to_numeric(
    df_apps_clean["Installs"].astype(str).str.replace(",", "")
)
# print(df_apps_clean[df_apps_clean["Installs"] >= 1000000000])
# 14. How many apps just had a single install?
# print(df_apps_clean[["App", "Installs"]].groupby("Installs").count())

# 15. Convert the price column to numeric data. Then investigate the top 20 most expensive apps in the dataset.
df_apps_clean["Price"] = pd.to_numeric(
    df_apps_clean["Price"].astype(str).str.replace("$", "")
)
# print(df_apps_clean.sort_values(by=["Price"], ascending=False).head(20))

# 16. Finding the most Expensive Apps and Filtering out the Junk
df_apps_clean = df_apps_clean[df_apps_clean["Price"] < 250]
# print(df_apps_clean.sort_values("Price", ascending=False).head(5))

df_apps_clean["Revenue_Estimate"] = df_apps_clean.Installs.mul(df_apps_clean.Price)
# print(df_apps_clean.sort_values("Revenue_Estimate", ascending=False)[:10])

# 17. Analyse with bar charts and scatter plots which categories are dominating the market
top10_category = df_apps_clean.Category.value_counts()[:10]
# bar_plot_top10_category = px.bar(
#     x=top10_category.index,  # index = category name
#     y=top10_category.values,
# )

# bar_plot_top10_category.show()

# 18. What matters is not just the total number of apps in the category but how often apps are downloaded in that category.
category_installs = df_apps_clean.groupby("Category").agg({"Installs": pd.Series.sum})
category_installs = category_installs.sort_values("Installs", ascending=True)

# 19. Create a horizontal bar chart
# h_bar = px.bar(
#     x=category_installs.Installs,
#     y=category_installs.index,
#     orientation="h",
#     title="Category Popularity",
# )

# h_bar.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")
# h_bar.show()

# 20. Do few apps have most of the downloads or are the downloads spread out over many apps?
cat_number = df_apps_clean.groupby("Category").agg({"App": pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on="Category", how="inner")
print(f"The dimensions of the DataFrame are: {cat_merged_df.shape}")
cat_merged_df.sort_values("Installs", ascending=False)

# Scatterplot
# scatter = px.scatter(
#     cat_merged_df,  # data
#     x="App",  # column name
#     y="Installs",
#     title="Category Concentration",
#     size="App",
#     hover_name=cat_merged_df.index,
#     color="Installs",
# )

# scatter.update_layout(
#     xaxis_title="Number of Apps (Lower=More installations are more concentrated in fewer apps)",
#     yaxis_title="Installs",
#     yaxis=dict(type="log"),
# )

# scatter.show()

# 21. How many different types of genres are there? We somehow need to separate the genre names to get a clear picture.
# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(";", expand=True).stack()
# print(f"We now have a single column with shape: {stack.shape}")
num_genres = stack.value_counts()
# print(f"Number of genres: {len(num_genres)}")

# bar = px.bar(
#     x=num_genres.index[:15],  # index = category name
#     y=num_genres.values[:15],  # count
#     title="Top Genres",
#     hover_name=num_genres.index[:15],
#     color=num_genres.values[:15],
#     color_continuous_scale="Agsunset",
# )

# bar.update_layout(
#     xaxis_title="Genre", yaxis_title="Number of Apps", coloraxis_showscale=False
# )

# bar.show()

# 22. Let’s see what the split is between free and paid apps
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg(
    {"App": pd.Series.count}
)

# g_bar = px.bar(
#     df_free_vs_paid,
#     x="Category",
#     y="App",
#     title="Free vs Paid Apps by Category",
#     color="Type",
#     barmode="group",
# )

# g_bar.update_layout(
#     xaxis_title="Category",
#     yaxis_title="Number of Apps",
#     xaxis={"categoryorder": "total descending"},
#     yaxis=dict(type="log"),
# )

# g_bar.show()

# 23. Create Box Plots for the Number of Installs
# box = px.box(
#     df_apps_clean,
#     y="Installs",
#     x="Type",
#     color="Type",
#     notched=True,
#     points="all",
#     title="How Many Downloads are Paid Apps Giving Up?",
# )

# box.update_layout(yaxis=dict(type="log"))

# box.show()

# 24. App Revenue by Category.
# So, if you were to list a paid app, how should you price it? To help you decide we can look at how your competitors in the same category price their apps.
df_paid_apps = df_apps_clean[df_apps_clean["Type"] == "Paid"]
# box = px.box(
#     df_paid_apps,
#     x="Category",
#     y="Revenue_Estimate",
#     title="How Much Can Paid Apps Earn?",
# )

# box.update_layout(
#     xaxis_title="Category",
#     yaxis_title="Paid App Ballpark Revenue",
#     xaxis={"categoryorder": "min ascending"},
#     yaxis=dict(type="log"),
# )


# box.show()

# 25. App Pricing by Category
box = px.box(df_paid_apps, x="Category", y="Price", title="Price per Category")

box.update_layout(
    xaxis_title="Category",
    yaxis_title="Paid App Price",
    xaxis={"categoryorder": "max descending"},
    yaxis=dict(type="log"),
)

box.show()
