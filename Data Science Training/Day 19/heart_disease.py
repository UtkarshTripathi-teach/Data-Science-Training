import streamlit as st
import panadas as pd
import numpy as np

data = '''Heart Disease Prediction using Machine Learning Heart disease prevention is critical, and data-driven prediction systems can significantly aid in early diagnosis and treatment. Machine Learning offers accurate prediction capabilities, enhancing healthcare outcomes. In this project, I analyzed a heart disease dataset with appropriate preprocessing. Multiple classification algorithms were implemented in Python using Scikit-learn and Keras to predict the presence of heart disease.

Algorithms Used:

Logistic Regression
Naive Bayes
Support Vector Machine (Linear)
K-Nearest Neighbors
Decision Tree
Random Forest
XGBoost
Artificial Neural Network (1 Hidden Layer, Keras)'''



st.write(data)


st.image('https://cdn.analyticsvidhya.com/wp-content/uploads/2022/02/Heart-Disease-Prediction-using-Machine-Learning.webp')



with open('heart_disease_pred.pkl','rb') as f:
    chatgpt = pickle.load(f)

url = '''https://github.com/ankitmisk/Heart_Disease_Prediction_ML_Model/blob/main/heart.csv?raw=true'''
df = pd.read_csv(url)

st.sidebar.header('Select Features to predict Heart DFisease')
st.sidebar.image('https://humanbiomedia.org/animations/circulatory-system/cardiac-cycle/heart-beating.gif')

all_values = []

for i in df.iloc[:,:-1]:
    min_value, max_value = df[i].agg(['min','max'])

    var =st.sidebar.slider(f'Select {i} value', int(min_value), int(max_value),
                      random.randint(int(min_value),int(max_value)))

    all_values.append(var)

st.write(all_values)
