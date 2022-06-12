"""
Simple use of statsmodels library
"""

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Ordinary least squares using formulas
DAT = sm.datasets.get_rdataset("Guerry", "HistData").data
results = smf.ols("Lottery ~ Literacy + np.log(Pop1831)", data=DAT).fit()
print(results.summary())

# Ordinary least squares using numpy arrays instead of formulas
NOBS = 100
X = np.random.random((NOBS, 2))
X = sm.add_constant(X)
beta = [1, 0.1, 0.5]
e = np.random.random(NOBS)
y = np.dot(X, beta) + e
results = sm.OLS(y, X).fit()
print(results.summary())
