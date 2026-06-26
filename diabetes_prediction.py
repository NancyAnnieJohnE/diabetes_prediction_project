
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Load Dataset
df = pd.read_csv("diabetes_dataset.csv")

print("\nFirst 5 Rows of Dataset:\n")
print(df.head())

# Split Features and Target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Machine Learning Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Accuracy Graph
plt.figure(figsize=(5,4))
plt.bar(["Accuracy"], [accuracy])
plt.ylim(0,1)
plt.ylabel("Score")
plt.title("Model Accuracy")
plt.savefig("accuracy_graph.png")
plt.show()

# Confusion Matrix Graph
fig, ax = plt.subplots(figsize=(5,5))
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(ax=ax)
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()
