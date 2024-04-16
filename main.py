import pandas as pd

# Load the data
data = pd.read_csv('CWC23_all_innings.csv')

# Convert start_date to datetime, assuming the format is "dd-MMM-yy"
data['start_date'] = pd.to_datetime(data['start_date'], format='%d-%b-%y')

# Team Performance Analysis
team_performance = data.groupby('team').agg({
    'runs': 'sum',
    'wkts': 'sum',
    'bb_bf': 'sum',
    'runs_per_ball': 'mean',
    'wicketball_prob': 'mean'
}).reset_index()
top_teams = team_performance.nlargest(5, ['runs', 'wkts'])
print("Top Performing Teams:")
print(top_teams)

# Player Performance Analysis
batting_data = data[data['bat_or_bowl'] == 'bat']
bowling_data = data[data['bat_or_bowl'] == 'bowl']
top_batters = batting_data.groupby('player').agg({
    'runs': 'sum',
    'sr': 'mean'
}).nlargest(5, 'runs')
top_bowlers = bowling_data.groupby('player').agg({
    'wkts': 'sum',
    'econ': 'mean'
}).nlargest(5, 'wkts')
print("\nTop Batters:")
print(top_batters)
print("\nTop Bowlers:")
print(top_bowlers)

# Opposition and Ground Analysis
opposition_performance = data.groupby(['team', 'opposition']).agg({
    'runs': 'sum',
    'wkts': 'sum'
}).reset_index()
ground_performance = data.groupby(['team', 'ground']).agg({
    'runs': 'sum',
    'wkts': 'sum'
}).reset_index()
print("\nPerformance Against Different Oppositions:")
print(opposition_performance)
print("\nPerformance Across Different Grounds:")
print(ground_performance)

# Temporal Analysis
temporal_trends = data.groupby([data['start_date'].dt.year, data['start_date'].dt.month]).agg({
    'runs': 'sum',
    'wkts': 'sum'
})
print("\nTemporal Trends:")
print(temporal_trends)
