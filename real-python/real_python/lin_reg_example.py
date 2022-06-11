"""
Linear Regression example
RealPython tutorial: https://realpython.com/linear-regression-in-python/
"""

# Step 1: Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 2: Provide data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# Step 3: Create a model and fit it
# model = LinearRegression()
# model.fit(x, y)

# Following lin is eqiuivelent to the two lines above
model = LinearRegression().fit(x, y)

# Step 4: Get results
r_sq = model.score(x, y)

print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

# Step 5: Predict response
y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")

# Alternate way to predict response using linear model equation
y_pred = model.intercept_ + model.coef_ * x
print(f"predicted response:\n{y_pred}")

# Predict response with new inputs
x_new = np.arange(5).reshape((-1, 1))
print(x_new)
y_new = model.predict(x_new)
print(y_new)
