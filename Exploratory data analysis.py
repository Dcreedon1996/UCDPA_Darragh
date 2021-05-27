# Importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# Reading in CSV and creating appropriate labels to determine correlation between social support, GDP per capita, and
# Life expectancy
df = pd.read_csv('2020.csv')
X1 = df['Social support']
X2 = df['Logged GDP per capita']
Y = df['Healthy life expectancy']

# Plotting both seperately

plt.scatter(X1, Y, alpha=0.75, c='blue')
plt.title('Social support versus Life expectancy')
plt.xlabel('Social support')
plt.ylabel('Healthy life expectancy')

plt.show()

plt.scatter(X2, Y, alpha=0.75, c='red')
plt.title('GDP per capita versus Life expectancy')
plt.xlabel('Logged GDP per capita')
plt.ylabel('Healthy life expectancy')

plt.show()

# Both show a degree of correlation, and it may be appropriate to construct a machine learning model to see if they can
# act as accurate predictors of life expectancy
