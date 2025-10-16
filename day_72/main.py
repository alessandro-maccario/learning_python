import pandas as pd


# import the salary data
data_salaries = pd.read_csv("data/salaries_by_college_major.csv")

# have a peek at the data
# print(data_salaries.head())

# Questions to answer
# 1. How many rows does our dataframe have?
print("How many rows?\n", data_salaries.shape[0], "\n")

# 2. How many columns does it have?
print("How many columns?\n", data_salaries.shape[1], "\n")

# 3. What are the labels for the columns? Do the columns have names?
print("Whare the column names?\n", data_salaries.columns, "\n")

# 4. Are there any missing values in our dataframe? Does our dataframe contain any bad data?
print("Are there any missing values?\n", data_salaries.isnull().sum(), "\n")
# print("Are there any missing values?", data_salaries[data_salaries.isna().any(axis=1)])

# 5. Clean the dataframe from NaN values
data_salaries = data_salaries.dropna()
# print("Clean dataframe, without NaN\n", data_salaries)

# 6. Find the index of the College Major with Highest Starting Salaries
index_highest_data_salaries_starting_salary = data_salaries[
    "Starting Median Salary"
].idxmax()

# 7.find the corresponding College Major that shows the Highest Starting Salaries
highest_college_major_salary = data_salaries.loc[
    index_highest_data_salaries_starting_salary
]
print(
    "College Major with Highest Starting Salaries\n", highest_college_major_salary, "\n"
)


# 8.    What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
index_highest_data_salary_mid_career = data_salaries[
    "Mid-Career Median Salary"
].idxmax()
highest_data_salary_mid_career = data_salaries.loc[index_highest_data_salary_mid_career]
print(
    "College Major with Highest Mid-Career Salary\n",
    highest_data_salary_mid_career,
    "\n",
)

# 9.    Which college major has the lowest starting salary and how much do graduates earn after university?
index_lowest_data_salary_starting_career = data_salaries[
    "Starting Median Salary"
].idxmin()
lowest_data_salary_starting_career = data_salaries.loc[
    index_lowest_data_salary_starting_career
]
print(
    "College Major with Lowest Starting Career Salary\n",
    lowest_data_salary_starting_career,
    "\n",
)


# 10.   Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
index_lowest_data_salary_mid_career = data_salaries["Mid-Career Median Salary"].idxmin()
lowest_data_salary_mid_career = data_salaries.loc[index_lowest_data_salary_mid_career]
print(
    "College Major with Lowest Mid-Career Salary\n",
    lowest_data_salary_mid_career,
    "\n",
)


# 11. Add column Lowest Risk Majors information: a low-risk major is a degree where there is a small difference between the lowest and highest salaries. In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small, then you can be more certain about your salary after you graduate.
spread_col = (
    data_salaries["Mid-Career 90th Percentile Salary"]
    - data_salaries["Mid-Career 10th Percentile Salary"]
)
data_salaries.insert(1, "Spread", spread_col)
print(data_salaries.head())

# 12. Sorting by the Lowest Spread
low_risk = data_salaries.sort_values("Spread")
print(low_risk[["Undergraduate Major", "Spread"]].head())


# 13. Using the .sort_values() method, find the top 5 degrees with the highest values in the 90th percentile
highest_90th_percentile = data_salaries.sort_values(
    "Mid-Career 90th Percentile Salary", ascending=False
)
print(
    highest_90th_percentile[
        ["Undergraduate Major", "Mid-Career 90th Percentile Salary"]
    ].head()
)

# 14. Find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation?
highest_spread = data_salaries.sort_values("Spread", ascending=False)
print(highest_spread[["Undergraduate Major", "Spread"]].head())

# 15. Which College Majors have the highest Mid-Career median Salary? Find the top 5 degrees.
highest_mid_career_median_salary = data_salaries.sort_values(
    "Mid-Career Median Salary", ascending=False
)
print(
    highest_mid_career_median_salary[
        ["Undergraduate Major", "Mid-Career Median Salary"]
    ].head()
)
