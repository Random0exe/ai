import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Input data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 6])

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict the output
X_test = np.array([[6]])
y_pred = model.predict(X_test)

# Plot the data points and the linear regression line
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, model.predict(X), color='red', label='Linear Regression Line')
plt.scatter(X_test, y_pred, color='green', label='Test Prediction')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
print("Predicted Output:", y_pred)
plt.show()
