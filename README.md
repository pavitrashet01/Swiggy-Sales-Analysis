# Swiggy-Sales-Analysis

1. Project Overview
This project analyzes Swiggy food delivery sales data using Python to extract business insights, track KPIs, and visualize revenue trends.
The objective is to understand sales performance, customer ratings, food preferences (Veg vs Non-Veg), geographic performance, and time-based revenue patterns.


Tools & Technologies Used
•	Python
•	Pandas
•	NumPy
•	Matplotlib
•	Seaborn
•	Plotly
•	Excel Dataset

 3. Dataset Description
The dataset contains order-level data including:
•	Order Date
•	Dish Name
•	City
•	State
•	Price (INR)
•	Rating
•	Rating Count


4. Step-by-Step Process
Step 1: Import Libraries
Imported required libraries for data manipulation and visualization.

Step 2: Load Dataset
Loaded the Excel dataset using Pandas.

Step 3: Data Understanding
•	Checked shape of dataset
•	Reviewed column names
•	Analyzed data types
•	Generated summary statistics

Step 4: Data Cleaning
•	Removed extra spaces from column names
•	Converted Order Date to datetime format
•	Converted Price (INR) and Rating to numeric
•	Removed rows with missing important values

Step 5: Feature Engineering
Created new columns for time-based analysis:
•	Year-Month (Monthly analysis)
•	Day Name (Daily trend)
•	Quarter (Quarterly summary)
•	Year-Week (Weekly trend)
Created a new column:
•	Food Category (Veg / Non-Veg) using keyword detection


📊 5. KPI Calculation
Calculated key business metrics:
•	Total Sales (INR)
•	Average Rating
•	Average Order Value
•	Total Ratings Count
•	Total Orders


 6. Data Visualization & Analysis
 Time-Based Analysis
•	Monthly Revenue Trend (Line Chart)
•	Weekly Revenue Trend (Line Chart)
•	Daily Revenue (Bar Chart)
•	Quarterly Summary (Sales, Ratings, Orders)
 Product Analysis
•	Veg vs Non-Veg Sales Distribution (Pie Chart)
 Geographic Analysis
•	Revenue by State (Horizontal Bar Chart)
•	Top 5 Cities by Sales


 7. Key Insights
•	Identified peak revenue months and weeks
•	Analyzed highest revenue-generating days
•	Compared Veg vs Non-Veg revenue contribution
•	Determined top-performing states and cities
•	Evaluated customer satisfaction using average ratings


 8. Project Outcome
This project demonstrates:
•	End-to-end data cleaning
•	KPI tracking
•	Time-series sales analysis
•	Geographic revenue analysis
•	Business-focused data visualization


