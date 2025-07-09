import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a Sample CSV File
data = [
    ["Date", "Game", "Platform", "Region", "Units Sold", "Revenue"],
    ["2023-01-30", "Zelda", "PC", "North America", 1000, 50000],
    ["2023-01-30", "Mario Bros.", "PS4", "Europe", 1600, 77000],
    ["2023-01-30", "WoW", "PS4", "Europe", 1700, 80000],
    ["2023-02-28", "Zelda", "PC", "Asia", 2300, 140000],
    ["2023-02-28", "Mario Bros.", "PC", "Asia", 2000, 110000],
    ["2023-02-28", "WoW", "PC", "Asia", 2400, 150000],
    ["2023-03-31", "Zelda", "PC", "Asia", 1500, 90000],
    ["2023-03-31", "Mario Bros.", "PC", "Asia", 1800, 110000],
    ["2023-03-31", "WoW", "PC", "Asia", 1900, 120000],
    ["2023-04-30", "Zelda", "Xbox", "North America", 800, 25000],
    ["2023-04-30", "Mario Bros.", "Xbox", "North America", 600, 18000],
    ["2023-04-30", "WoW", "Xbox", "North America", 900, 27000],
    ["2023-05-31", "Zelda", "PS4", "Asia", 1200, 30000],
    ["2023-05-31", "Mario Bros.", "PS4", "Asia", 1350, 42000],
    ["2023-05-31", "WoW", "PS4", "Asia", 1800, 60000],
    ["2023-06-30", "Zelda", "PC", "Europe", 900, 27000],
    ["2023-06-30", "Mario Bros.", "PC", "Europe", 600, 18000],
    ["2023-06-30", "WoW", "PC", "Europe", 800, 25000],
    ["2023-07-31", "Zelda", "Xbox", "Asia", 700, 21000],
    ["2023-07-31", "Mario Bros.", "Xbox", "Asia", 750, 22000],
    ["2023-07-31", "WoW", "Xbox", "Asia", 775, 23500],
    ["2023-08-31", "Zelda", "PS4", "North America", 600, 20000],
    ["2023-08-31", "Mario Bros.", "PS4", "North America", 1400, 43000],
    ["2023-08-31", "WoW", "PS4", "North America", 1500, 90000],
    ["2023-09-30", "Mario Bros.", "PS4", "North America", 1600, 80000],
     
]

file_path = 'gaming_Company_Visualize.csv'

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Step 2: Perform Sales Analysis
# Load the data
df = pd.read_csv(file_path)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])


# Calculate total sales
total_units_sold = df['Units Sold'].sum()
total_revenue = df['Revenue'].sum()

# Sales by game
sales_by_game = df.groupby('Game').agg({'Units Sold': 'sum', 'Revenue': 'sum'})
print()
print("Sales by each game:")
print(sales_by_game)
print()

# Calculate average revenue by each game
average_revenue_by_game = df.groupby('Game')['Revenue'].mean()

# Monthly sales trends
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month').agg({'Units Sold': 'sum', 'Revenue': 'sum'})
print("Monthly Sales: ")
print(monthly_sales)

# Step 3: Visualize the Results
# Plot total units sold and revenue by game
# 1. Bar Chart: Sales by Game
# 2. Line Chart: Monthly Sales Trends
# 3. Line Chart: Monthly Sales Trend by Game
fig, ax1 = plt.subplots(figsize=(10, 6))

sales_by_game['Units Sold'].plot(kind='bar', ax=ax1, color='b', position=1, width=0.4, label='Units Sold')
ax1.set_ylabel('Units Sold', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xticklabels(sales_by_game.index, rotation=45)
ax2 = ax1.twinx()
sales_by_game['Revenue'].plot(kind='bar', ax=ax2, color='g', position=0, width=0.4, label='Revenue')
ax2.set_ylabel('Revenue', color='g')
ax2.tick_params(axis='y', labelcolor='g')
fig.suptitle('Sales by Game')
ax1.legend(loc='upper right')
ax2.legend(loc='upper left')
plt.show()


# Plot monthly sales trends
fig, ax = plt.subplots(figsize=(10, 6))
monthly_sales['Units Sold'].plot(kind='line', marker='o', ax=ax, color='b', label='Units Sold')
ax.set_ylabel('Units Sold', color='b')
ax.tick_params(axis='y', labelcolor='b')
ax2 = ax.twinx()
monthly_sales['Revenue'].plot(kind='line', marker='x', ax=ax2, color='g', label='Revenue')
ax2.set_ylabel('Revenue', color='g')
ax2.tick_params(axis='y', labelcolor='g')
fig.suptitle('Monthly Sales Trends')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

# New code for the sales trend of each game by month
fig, ax = plt.subplots(figsize=(10, 6))
for game in df['Game'].unique():
    game_data = df[df['Game'] == game].groupby('Month')['Units Sold'].sum()
    ax.plot(game_data.index.to_timestamp(), game_data.values, marker='o', label=game)

ax.set_xlabel('Month')
ax.set_ylabel('Units Sold')
ax.set_title('Monthly Sales Trend by Game')
ax.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# Print the analysis results
print("Total Units Sold:", total_units_sold)
print("Total Revenue:", total_revenue)
print("\nSales by Game:\n", sales_by_game)
print("\nAverage Revenue by Game:\n", average_revenue_by_game)
print("\nMonthly Sales Trends:\n", monthly_sales)
