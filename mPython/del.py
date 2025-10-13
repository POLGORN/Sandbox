import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [102.06, 1, 0.125],
    [148.5, 2, 0.8],
    [97.2, 1, 1.0],
    [128.25, 2, 0.6],
    [94.5, 1, 0.375]
])

y = np.array([22000, 30000, 25000, 32000, 22000])

model = LinearRegression()
model.fit(X, y)

print("Коэффициенты:", model.coef_)
print("Свободный член:", model.intercept_)
