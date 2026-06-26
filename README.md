# Diabetes Prediction using Logistic Regression

## Overview

This project demonstrates how Machine Learning can be used to predict whether a person is likely to have diabetes based on various medical attributes. The project uses the **Logistic Regression** algorithm to classify patients as diabetic or non-diabetic.

The model is trained on a diabetes dataset, evaluated for its performance, and then used to predict diabetes status based on user-provided input values.

---

## Features

- Loads the diabetes dataset from a CSV file.
- Performs data preprocessing.
- Splits the dataset into training and testing sets.
- Trains a **Logistic Regression** classification model.
- Evaluates the model using accuracy score.
- Saves the trained model using Joblib.
- Loads the saved model for prediction.
- Accepts user input from the terminal.
- Predicts whether a person is diabetic or non-diabetic.

---

## Machine Learning Algorithm

**Algorithm Used:** Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems. In this project, it predicts whether a person has diabetes based on several medical measurements.

---

## Dataset

The dataset contains medical records of patients.

### Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

### Target Variable

- **Outcome**
  - **0** – Non-Diabetic
  - **1** – Diabetic

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Anaconda Prompt

---

## Project Workflow

1. Import the required Python libraries.
2. Load the diabetes dataset.
3. Separate the input features and target variable.
4. Split the dataset into training and testing sets.
5. Train the **Logistic Regression** model.
6. Evaluate the model using accuracy score.
7. Save the trained model.
8. Load the saved model.
9. Accept medical details from the user.
10. Predict whether the person is diabetic or non-diabetic.

---

## Project Structure

```
diabetes_prediction_project/
│
├── diabetes.csv
├── diabetes_model.py
├── predict_diabetes.py
├── diabetes_model.pkl
├── accuracy.png
├── prediction.png
├── README.md
```

---

## How to Run

### Step 1

Open **Anaconda Prompt**.

### Step 2

Navigate to the project folder.

```bash
cd path_to_project_folder
```

### Step 3

Train the model.

```bash
python diabetes_model.py
```

### Step 4

Run the prediction program.

```bash
python predict_diabetes.py
```

### Step 5

Enter the required medical details.

Example:

```
Pregnancies: 2
Glucose: 120
Blood Pressure: 70
Skin Thickness: 20
Insulin: 85
BMI: 28.5
Diabetes Pedigree Function: 0.35
Age: 35
```

Example Output:

```
Prediction: Non-Diabetic
```

or

```
Prediction: Diabetic
```

---

## Output Screenshots

### Model Accuracy

> Replace the filename below with your actual accuracy screenshot name if it is different.

![Model Accuracy](accuracy.png)

### Prediction Result

> Replace the filename below with your actual prediction screenshot name if it is different.

![Prediction Result](prediction.png)

---

## Requirements

This project was developed and executed using **Anaconda Prompt**.

Required Python libraries:

- numpy
- pandas
- scikit-learn
- joblib

---

## Applications

- Early diabetes risk prediction
- Healthcare decision support systems
- Medical data analysis
- Machine learning classification projects
- Educational purposes

---

## Future Improvements

- Train the model using a larger dataset.
- Improve prediction accuracy through feature engineering.
- Compare Logistic Regression with other classification algorithms.
- Develop a graphical user interface (GUI).
- Implement real-time prediction through a web application.

---

## Conclusion

This project demonstrates the implementation of the **Logistic Regression** algorithm for diabetes prediction using patient medical data. It provides a practical example of supervised machine learning for binary classification and serves as a strong foundation for healthcare-related machine learning applications.
