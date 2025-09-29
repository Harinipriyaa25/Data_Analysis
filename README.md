Amazon Sales Data Analysis

This mini project analyzes Amazon sales data using Python (Pandas & Matplotlib).
The goal is to get basic insights from the dataset like sales, ratings, and popularity across product categories.

🛠 Tools & Libraries

Python

Pandas – for data cleaning & analysis

Matplotlib – for data visualization

📂 Dataset

The dataset was downloaded from Kaggle (Amazon Dataset).

It contains product details like:

Product ID, Product Name

Category

Discounted Price, Actual Price, Discount %

Rating, Rating Count

Reviews and Metadata

📌 Steps in the Project

Load the CSV file using Pandas.

Clean the data – remove symbols (₹, %, ,) and convert columns to numeric.

Simplify categories – keep only the first category name for clarity.

Group & analyze using:

groupby()

sum()

mean()

plot()

Visualize results with bar charts.

📈 Insights

We generated 3 charts for the top 10 categories:

Total Discounted Sales :

  Shows which categories bring the highest revenue.

Average Rating :

  Shows which categories are rated best by users.

Popularity (Rating Count) :

  Shows which categories have the most customer engagement.

  How to Run:

Install Python (>=3.10 recommended).

Install dependencies:

  pip install pandas matplotlib

Run the script:

  python amazon_analysis.py

This will display the 3 charts and print basic insights in the terminal.
