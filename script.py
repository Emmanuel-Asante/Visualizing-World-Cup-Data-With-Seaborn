# Import libraries
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Load WorldCupMatches.csv file into a DataFrame called df
df = pd.read_csv('WorldCupMatches.csv')

# Output the first five rows of df
print(df.head())

# Create "Total Goals" column and set it equal to the sum of the columns "Home Team Goals" and "Away Team Goals"
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

# Output the first five rows of df
print(df.head())

# Set plot style
sns.set_style("whitegrid")

# Scale context and font
sns.set_context("poster", font_scale=0.8)

# Create figure and axes with width of 12 and height of 7
f, ax = plt.subplots(figsize=(12, 7))

# Create a bar chart
ax = sns.barplot(data=df, x="Year", y="Total Goals")

# Set title
ax.set_title("Average Goals Scored In World Cup Matches By Year", fontweight="bold")

# Rotate x-axis ticks
plt.xticks(rotation=90)

# Show plot
plt.show()

# Clear current figure
plt.clf()

# Load goals.csv file into a DataFrame called df_goals
df_goals = pd.read_csv('goals.csv')

# Output the first five rows of df_goals
print(df_goals.head())

# Scale context and font
sns.set_context("notebook", font_scale=1.25)

# Create figure and axes with width of 12 and height of 7
f, ax2 = plt.subplots(figsize=(12, 7))

# Create box plots
ax2 = sns.boxplot(data=df_goals, x="year", y="goals", palette="Spectral")

# Set title
ax2.set_title("Goals Visualization", fontweight="bold")

# Rotate x-axis ticks
plt.xticks(rotation=90)

# Show plot
plt.show()