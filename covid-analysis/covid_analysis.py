import pandas as pd

# Load the dataset
df = pd.read_csv("covid_data.csv")

print("===== RAW DATA =====")
print(df, "\n")

# -----------------------------
# 1. CHECK FOR NULL VALUES
# -----------------------------
print("===== Missing Values =====")
print(df.isnull().sum(), "\n")

# -----------------------------
# 2. HANDLE MISSING VALUES
# -----------------------------
df['new_cases'].fillna(df['new_cases'].mean(), inplace=True)
df['new_deaths'].fillna(0, inplace=True)
df['total_cases'].fillna(method='ffill', inplace=True)
df['total_deaths'].fillna(method='ffill', inplace=True)

print("===== After Filling Missing Values =====")
print(df, "\n")

# -----------------------------
# 3. CONVERT DATA TYPES
# -----------------------------
df['date'] = pd.to_datetime(df['date'])

print("===== Data Types After Conversion =====")
print(df.dtypes, "\n")

# -----------------------------
# 4. BASIC ANALYSIS
# -----------------------------

# Total new cases by country
cases_by_country = df.groupby("country")["new_cases"].sum()
print("===== Total New Cases by Country =====")
print(cases_by_country, "\n")

# Total deaths by country
deaths_by_country = df.groupby("country")["new_deaths"].sum()
print("===== Total New Deaths by Country =====")
print(deaths_by_country, "\n")

# Highest one-day infection count
max_cases = df.loc[df["new_cases"].idxmax()]
print("===== Highest One-Day Case Count =====")
print(max_cases, "\n")

# -----------------------------
# 5. SAVE CLEANED DATA
# -----------------------------
df.to_csv("cleaned_covid_data.csv", index=False)
print("Cleaned dataset saved as 'cleaned_covid_data.csv'")
