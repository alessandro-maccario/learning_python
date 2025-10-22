import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# read the datasets in
df_tesla = pd.read_csv(
    "data/Google Trends Data Viz (start)/TESLA Search Trend vs Price.csv"
)
df_unemployment = pd.read_csv(
    "data/Google Trends Data Viz (start)/UE Benefits Search vs UE Rate 2004-20.csv"
)
df_daily_bitcoin = pd.read_csv(
    "data/Google Trends Data Viz (start)/Daily Bitcoin Price.csv"
)
df_bitcoin_trend = pd.read_csv(
    "data/Google Trends Data Viz (start)/Bitcoin Search Trend.csv"
)

# # 1. What are the shapes of the DataFrames?
# print("Tesla df:", df_tesla.shape)
# print("Unemployment df:", df_unemployment.shape)

# # 2. What are the column names?
# print("Tesla df:", df_tesla.columns)
# print("Unemployment df:", df_unemployment.columns)

# # 3. What is the largest number in the search data column? Try using the .describe() function.
# print("Tesla df:", df_tesla.describe())
# print("Unemployment df:", df_unemployment.describe())

# 4. What is the periodicity of the time series data (daily, weekly, monthly)?
# > Monthly


# 5. Investigate all 4 DataFrames and find if there are any missing values
# print("####### MISSINGS\n")
# print("TESLA: Are there any missing values?\n", df_tesla.isnull().sum(), "\n")
# print(
#     "UNEMPLOYMENT: Are there any missing values?\n",
#     df_unemployment.isnull().sum(),
#     "\n",
# )
# print(
#     "DAILY BITCOIN: Are there any missing values?\n",
#     df_daily_bitcoin.isnull().sum(),
#     "\n",
# )
# print(
#     "BITCOIN TREND: Are there any missing values?\n",
#     df_bitcoin_trend.isnull().sum(),
#     "\n",
# )

# 6. Drop missing values
df_tesla.dropna(inplace=True)
df_unemployment.dropna(inplace=True)
df_daily_bitcoin.dropna(inplace=True)
df_bitcoin_trend.dropna(inplace=True)

# print("\n######### Data Type\n")
# print("TESLA DTYPE:", df_tesla.dtypes, "\n")
# print("UNEMPLOYMENT DTYPE:", df_unemployment.dtypes, "\n")
# print("DAILY BITCOIN DTYPE:", df_daily_bitcoin.dtypes, "\n")
# print("BITCOIN TREND DTYPE:", df_bitcoin_trend.dtypes, "\n")

# Convert date string column to date
df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"])
df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"])
df_daily_bitcoin["DATE"] = pd.to_datetime(df_daily_bitcoin["DATE"])
# resampling daily data to monthly data
df_monthly_bitcoin = (
    df_daily_bitcoin.resample("ME", on="DATE").last().reset_index(names=["MONTH"])
)
df_bitcoin_trend["MONTH"] = pd.to_datetime(df_bitcoin_trend["MONTH"])
print(df_monthly_bitcoin)


# 7.a Add date locator
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")


# # 7. Plot: Tesla
# # define the figure boundaries
# plt.figure(figsize=(14, 8))
# plt.title("Tesla Web Search vs Price", fontsize=18)

# # Increase the size and rotate the labels on the x-axis
# plt.xticks(fontsize=14, rotation=45)

# ax1 = plt.gca()  # get current axis
# ax2 = ax1.twinx()

# # Also, increase fontsize and linewidth for larger charts
# ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontsize=14)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=14)

# # Set the minimum and maximum values on the axes
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# # format the ticks on the axis with Locators
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# # Displays chart explicitly
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#FD9A9F")
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue")
# plt.show()


# 8. Plot: Bitcoin
# define the figure boundaries
plt.figure(figsize=(14, 8))
plt.title("Bitcoin News Search vs Resampled Price", fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()  # get current axis
ax2 = ax1.twinx()

# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel("BTC Price", color="#E6232E", fontsize=14)
ax2.set_ylabel("Search Trend", color="skyblue", fontsize=14)

# Set the minimum and maximum values on the axes
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# format the ticks on the axis with Locators
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# Displays chart explicitly
ax1.plot(df_monthly_bitcoin.MONTH, df_monthly_bitcoin.CLOSE, color="#FD9A9F")
ax2.plot(df_bitcoin_trend.MONTH, df_bitcoin_trend.BTC_NEWS_SEARCH, color="skyblue")
plt.show()
