import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load Dataset
df = pd.read_csv("student_data.csv")

print("\n===== DATASET =====")
print(df)

# Dataset Information
print("\n===== DATA INFO =====")
print(df.info())

# Check Missing Values
print("\n===== MISSING VALUES =====") 
print(df.isnull().sum())

# Fill Missing Values (if any)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Statistical Summary
print("\n===== EDA SUMMARY =====")
print(df.describe())

# Feature Selection
X = df[["Attendance", "StudyHours", "InternalMarks"]]

y = df["FinalMarks"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, y_pred)

print("\n===== MODEL ACCURACY =====")
print(round(accuracy * 100, 2), "%")

# User Prediction
print("\n===== STUDENT PERFORMANCE PREDICTION =====")

attendance = float(input("Enter Attendance (%): "))
study_hours = float(input("Enter Study Hours: "))
internal_marks = float(input("Enter Internal Marks: "))

prediction = model.predict(
    [[attendance, study_hours, internal_marks]]
)

print("\nPredicted Final Marks:", round(prediction[0], 2))

# Graph 1
plt.scatter(
    df["Attendance"],
    df["FinalMarks"]
)

plt.xlabel("Attendance")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.show()

# Graph 2
plt.scatter(
    df["StudyHours"],
    df["FinalMarks"]
)

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.show()