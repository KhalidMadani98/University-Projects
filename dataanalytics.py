#import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Acquisition using file pathway
my_employeeData = pd.read_csv(r"C:\Users\MADANIS\OneDrive - FUJITSU\Data Analytics Improved set.csv")

# Data Cleansing
my_employeeData.dropna(inplace=True)  # remove rows with missing values
my_employeeData.drop_duplicates(inplace=True)  # remove duplicate rows
my_employeeData.fillna(0, inplace=True)  # complete any missing values with zeros

# Data Exploration
employee_stats = my_employeeData.describe()  # Summary statistics
anomalies = my_employeeData[(my_employeeData['Performance Rating'] < employee_stats['Performance Rating']['25%']) | (my_employeeData['Performance Rating'] > employee_stats['Performance Rating']['75%'])]  # Outliers

# Set up the figure and axes
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Scatter plot
sns.scatterplot(data=my_employeeData, x='Satisfaction Rating', y='Salary', ax=axs[0, 0])
axs[0, 0].set_title('Productivity vs. Department')

# Box plot
sns.boxplot(data=my_employeeData, y='Performance Rating', ax=axs[0, 1])
axs[0, 1].set_title('Performance Distribution')

# Histogram
sns.histplot(data=my_employeeData, x='Productivity', kde=True, ax=axs[1, 0])
axs[1, 0].set_title('Productivity Distribution')
axs[1, 0].set_ylabel('Frequency')  # Set y-axis label to 'Frequency'

import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'Date' column exists in my_employeeData DataFrame
my_employeeData['Date'] = pd.to_datetime(my_employeeData['Date'], dayfirst=True)  # Convert 'Date' column to datetime with day first

# Extract month from 'Date' column
my_employeeData['Month'] = my_employeeData['Date'].dt.month

# Plot performance rating against month
plt.plot(my_employeeData['Month'], my_employeeData['Performance Rating'])
plt.xlabel('Month')
plt.ylabel('Performance Rating')
plt.title('Performance Rating vs Month')
plt.show()

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plots
plt.show()

