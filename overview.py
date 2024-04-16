import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('CWC23_all_innings.csv')

# Convert 'start_date' to datetime with a specific format
# Adjust the format string as per your date format in the CSV
data['start_date'] = pd.to_datetime(data['start_date'], format='%d-%b-%y')  # Change format as needed

# Extract year and month from the 'start_date'
data['year'] = data['start_date'].dt.year
data['month'] = data['start_date'].dt.month

# Group data by year and month, then aggregate runs and wickets
monthly_performance = data.groupby(['year', 'month']).agg({
    'runs': 'sum',
    'wkts': 'sum'
}).reset_index()

# Plotting the trends
plt.figure(figsize=(14, 7))

# Plot for runs
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first plot
plt.plot(monthly_performance['month'] + 12 * (monthly_performance['year'] - monthly_performance['year'].min()),
         monthly_performance['runs'], marker='o', linestyle='-')
plt.title('Monthly Runs Over Time')
plt.xlabel('Month from Start')
plt.ylabel('Total Runs')

# Plot for wickets
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second plot
plt.plot(monthly_performance['month'] + 12 * (monthly_performance['year'] - monthly_performance['year'].min()),
         monthly_performance['wkts'], marker='o', color='green', linestyle='-')
plt.title('Monthly Wickets Over Time')
plt.xlabel('Month from Start')
plt.ylabel('Total Wickets')

plt.tight_layout()
plt.show()
