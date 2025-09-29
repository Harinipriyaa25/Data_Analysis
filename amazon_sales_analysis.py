# amazon_analysis.py
# Mini Project: Data Analysis on CSV Files (Amazon Dataset)

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv(r"C:\\Users\\shari\\Downloads\\archive.zip")

# 2. Data Cleaning (convert prices/ratings to numbers)
def clean_price(x):
    return float(x.replace("₹", "").replace(",", "").strip()) if isinstance(x, str) else x

def clean_percentage(x):
    return float(x.replace("%", "").strip()) if isinstance(x, str) else x

def clean_rating(x):
    try:
        return float(x)
    except:
        return None

def clean_rating_count(x):
    try:
        return int(x.replace(",", ""))
    except:
        return 0

df["discounted_price"] = df["discounted_price"].apply(clean_price)
df["actual_price"] = df["actual_price"].apply(clean_price)
df["discount_percentage"] = df["discount_percentage"].apply(clean_percentage)
df["rating"] = df["rating"].apply(clean_rating)
df["rating_count"] = df["rating_count"].apply(clean_rating_count)

# 3. Simplify category (use only the first part before '|')
df["main_category"] = df["category"].apply(lambda x: x.split("|")[0])

# 4. Groupby Analysis
sales_by_category = df.groupby("main_category")["discounted_price"].sum().sort_values(ascending=False)
avg_rating_by_category = df.groupby("main_category")["rating"].mean().sort_values(ascending=False)
popularity_by_category = df.groupby("main_category")["rating_count"].sum().sort_values(ascending=False)

# 5. Visualization (Top 10 categories only for clarity)

# Chart 1: Total Discounted Sales
plt.figure(figsize=(10,6))
sales_by_category.head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Categories - Total Discounted Sales")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Average Rating
plt.figure(figsize=(10,6))
avg_rating_by_category.head(10).plot(kind="bar", color="orange")
plt.title("Top 10 Categories - Average Rating")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Popularity (Rating Count)
plt.figure(figsize=(10,6))
popularity_by_category.head(10).plot(kind="bar", color="green")
plt.title("Top 10 Categories - Popularity (Rating Count)")
plt.ylabel("Rating Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Print insights
print("\n=== Data Insights ===")
print("Top 5 categories by sales:\n", sales_by_category.head())
print("\nTop 5 categories by average rating:\n", avg_rating_by_category.head())
print("\nTop 5 categories by popularity (rating count):\n", popularity_by_category.head())
