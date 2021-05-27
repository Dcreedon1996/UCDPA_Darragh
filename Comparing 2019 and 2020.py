# Importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2020 = pd.read_csv('2020.csv')
df2019 = pd.read_csv('2019.csv')

df3 = df2020.join(df2019, lsuffix=2020, rsuffix=2019)

# Some values for generosity in 2020s dataframe are negative, we take the absolute value of these numbers to convert them to usable data
df3['Generosity2020'] = df3['Generosity2020'].abs()

# Plotting a histogram to determine the distribution of generosity index scores in 2020

n_data = len(df3['Generosity2020'])

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
plt.hist(df3['Generosity2020'], bins=n_bins, color='blue')

# Label axes
_ = plt.xlabel('Generosity index 2020 (%)')
_ = plt.ylabel('count')

# Show histogram
plt.show()

# Doing the same for 2019

n_data = len(df3['Generosity2019'])

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
plt.hist(df3['Generosity2019'], bins=n_bins, color='red')

# Label axes
_ = plt.xlabel('Generosity index 2019 (%)')
_ = plt.ylabel('count')

# Show histogram
plt.show()
