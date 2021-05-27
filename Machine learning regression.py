# Importing necessary packages and modules
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Reading in the data frame and setting up the predictor and test variables
df = pd.read_csv('2020.csv')
X = df[['Logged GDP per capita', 'Social support']].values
y = df['Healthy life expectancy'].values

# Setting up the regressor and train/test splits
reg = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=31)

# Setting up a parameter grid for hyperparameter tuning,
parameters = {'fit_intercept': [True, False], 'normalize': [True, False], 'copy_X': [True, False]}
grid = GridSearchCV(reg, parameters, cv=5)
grid.fit(X_train, y_train)

print("Tuned Logistic Regression Parameters: {}".format(grid.best_params_))
print("Best score is {}".format(grid.best_score_))

# This gives us an opimal set of parameters of {'copy_X': True, 'fit_intercept': True, 'normalize': True}
# We will now apply these to a linear regression model

# Create new training and test sets with a different random state
Xfull_train, Xfull_test, yfull_train, yfull_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression(copy_X=True, fit_intercept=True, normalize=True)

# Fit the regressor to the training data
reg_all.fit(Xfull_train, yfull_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(Xfull_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(Xfull_test, yfull_test)))
rmse = np.sqrt(mean_squared_error(yfull_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))
