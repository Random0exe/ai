from sklearn import svm

# Sample feature vectors
X = [[2, 3], [1, 5], [4, 2], [3, 4], [5, 1], [2, 2]]

# Sample class labels
y = [0, 0, 1, 1, 0, 1]

# Create an SVM classifier
clf = svm.SVC()

# Train the classifier on the sample data
clf.fit(X, y)

# Make predictions on new data
new_data = [[3, 3], [1, 3]]
predictions = clf.predict(new_data)

# Print the predictions
for i, pred in enumerate(predictions):
    print(f"Prediction for sample {i+1}: {pred}")
