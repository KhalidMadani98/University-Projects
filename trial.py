#import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# My_EmployeePerformanceData Acquisition using file pathway
My_EmployeePerformanceData = pd.read_csv(r"C:\Users\MADANIS\OneDrive - FUJITSU\Documents\sample data analytics final.csv")

# My_EmployeePerformanceData Cleansing
My_EmployeePerformanceData.dropna(inplace=True)  # remove rows with missing values
My_EmployeePerformanceData.drop_duplicates(inplace=True)  # remove duplicate rows
My_EmployeePerformanceData.fillna(0, inplace=True)  # complete any missing values with zeros

# My_EmployeePerformanceData Exploration
final_My_EmployeePerformanceData = My_EmployeePerformanceData.describe()  # Summary statistics
anomalies = My_EmployeePerformanceData[(My_EmployeePerformanceData['Performance'] < final_My_EmployeePerformanceData['Performance']['25%']) | (My_EmployeePerformanceData['Performance'] > final_My_EmployeePerformanceData['Performance']['75%'])]  # Outliers

# Set up the figure and axes
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Scatter plot
sns.scatterplot(My_EmployeePerformanceData=My_EmployeePerformanceData, x='Productivity', y='Department', ax=axs[0, 0])
axs[0, 0].set_title('Productivity vs. Department')

# Box plot
sns.boxplot(My_EmployeePerformanceData=My_EmployeePerformanceData, y='Performance', ax=axs[0, 1])
axs[0, 1].set_title('Performance Distribution')

# Histogram
sns.histplot(My_EmployeePerformanceData=My_EmployeePerformanceData, x='Productivity', kde=True, ax=axs[1, 0])
axs[1, 0].set_title('Productivity Distribution')
axs[1, 0].set_ylabel('Frequency')  # Set y-axis label to 'Frequency'

# Line plot
axs[1, 1].plot(My_EmployeePerformanceData['Date'], My_EmployeePerformanceData['Performance'])
axs[1, 1].set_xlabel('Date')
axs[1, 1].set_ylabel('Performance')
axs[1, 1].set_title('Performance Over Time')

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plots
