# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 18:58:05 2026

@author: pavitra
"""

'SWIGGY SALES ANALYSIS'

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Import Data
df = pd.read_excel(r"C:\Users\pavitra\Desktop\Swiggy Sales Analysis  python\swiggy_data.xlsx")
df

df.head()
df.tail()

# Metadata

df.shape
df.info()
df.columns


# Data types
df.dtypes
df.describe()


# Data Cleaning

# Strip extra spaces from column names
df.columns = df.columns.str.strip()

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Convert price & rating to numeric
df["Price (INR)"] = pd.to_numeric(df["Price (INR)"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Drop null important rows
df = df.dropna(subset=["Order Date", "Price (INR)"])


# KPI'S

'Total Sales'

total_sales = df["Price (INR)"].sum()
print("Total sales(INR):", round(total_sales,2))


'Average Rating'

average_rating = df["Rating"].mean()
print("Average Rating:", round(average_rating,2))


'Average Order Value'

avg_order_value = df["Price (INR)"].mean()
print("Average Order Value:", round(avg_order_value,2))


'Ratings Count'

ratings_count = df["Rating Count"].sum()
print("Ratings Count:", round(ratings_count))


'Total Orders'

total_orders = len(df)
print("Total Orders:", total_orders)




'CHARTS DESIGN'

'Monthly Revenue Trend'

df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_revenue = (
    df.groupby("YearMonth")["Price (INR)"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(12,5))
plt.plot(monthly_revenue["YearMonth"], monthly_revenue["Price (INR)"])
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.show()



'Daily Revenue Trend (Mon–Sun)'


df["DayName"] = df["Order Date"].dt.day_name()

daily_revenue = (
    df.groupby("DayName")["Price (INR)"]
    .sum()
    .reindex(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
)

plt.figure(figsize=(8,5))
plt.bar(daily_revenue.index, daily_revenue.values)
plt.title("Daily Revenue Trend")
plt.xlabel("Day")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=30)
plt.show()




'Total Sales by Food Type (Veg vs Non-Veg)'

non_veg_keywords = [
    "chicken","egg","fish","mutton",
    "prawn","biryani","kabab","kebab",
    "non-veg","non veg"
]

df["Dish Name"] = df["Dish Name"].astype(str)

df["Food Category"] = np.where(
    df["Dish Name"].str.lower().str.contains("|".join(non_veg_keywords), na=False),
    "Non-Veg",
    "Veg"
)

food_revenue = (
    df.groupby("Food Category")["Price (INR)"]
    .sum()
)

plt.figure(figsize=(6,6))
plt.pie(
    food_revenue,
    labels=food_revenue.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Total Sales by Food Type (Veg vs Non-Veg)")
plt.show()




'Revenue by State (Horizontal Bar)'


state_revenue = (
    df.groupby("State")["Price (INR)"]
    .sum()
    .sort_values()
)

plt.figure(figsize=(10,8))
plt.barh(state_revenue.index, state_revenue.values)
plt.title("Revenue by State")
plt.xlabel("Revenue (INR)")
plt.ylabel("State")
plt.show()





'Quarterly Summary (Sales, Rating, Orders)'

df["Quarter"] = df["Order Date"].dt.to_period("Q").astype(str)

quarterly_summary = (
    df.groupby("Quarter")
    .agg(
        Total_Sales=("Price (INR)", "sum"),
        Avg_Rating=("Rating", "mean"),
        Total_Orders=("Order Date", "count")
    )
    .reset_index()
    .sort_values("Quarter")
)

quarterly_summary["Total_Sales"] = quarterly_summary["Total_Sales"].round(0)
quarterly_summary["Avg_Rating"] = quarterly_summary["Avg_Rating"].round(2)

quarterly_summary



'Top 5 Cities by Sales'

top_5_cities = (
    df.groupby("City")["Price (INR)"]
    .sum()
    .nlargest(5)
    .sort_values()
)

plt.figure(figsize=(8,5))
plt.barh(top_5_cities.index, top_5_cities.values)
plt.title("Top 5 Cities by Sales")
plt.xlabel("Revenue (INR)")
plt.ylabel("City")
plt.show()



'Weekly Revenue Trend Analysis'

# Create Year-Week column
df["YearWeek"] = df["Order Date"].dt.to_period("W").astype(str)

# Calculate weekly revenue
weekly_revenue = (
    df.groupby("YearWeek")["Price (INR)"]
    .sum()
    .reset_index()
)

# Plot weekly revenue trend
plt.figure(figsize=(12,5))
plt.plot(weekly_revenue["YearWeek"], weekly_revenue["Price (INR)"])
plt.xticks(rotation=90)
plt.title("Weekly Revenue Trend")
plt.xlabel("Week")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.show()




