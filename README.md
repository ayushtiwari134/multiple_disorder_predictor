# Multiple Disorder Prediction App

Welcome to the Multiple Disorder Prediction app! This application predicts the likelihood of obesity and diabetes in a person based on various inputs. It utilizes machine learning models, pipelines, and column transformers to efficiently handle data and provide predictions.

## Overview

This project incorporates machine learning models trained to predict the probability of obesity and diabetes in individuals. The models are developed in a Jupyter Notebook environment using pipelines, column transformers, and exported as pickle files for easy deployment.

## Technology Stack

- **Model Development:** Jupyter Notebook
- **Machine Learning Algorithms:** Logistic Regression, Descision Tree Classifier, implemented using pipelines and column transformers
- **Frontend:** Streamlit
- **Deployment:** Streamlit Cloud Services

## Getting Started

### Clone the Repository

To run the application locally, clone this repository using the following command:

`git clone https://github.com/ayushtiwari134/multiple_disorder_predictor`


### Running the App

After cloning the repository, navigate to the project directory and execute the following command to run the app:

`streamlit run app.py`


This command will start the Streamlit web application locally, enabling access to the multiple disorder prediction interface.

## Deployment

The application is deployed using Streamlit Cloud Services, offering a live environment to predict the likelihood of obesity and diabetes in individuals.

## Features

- **Input Parameters:** Users can input various health-related factors, such as BMI, blood sugar levels, age, etc.
- **Prediction:** The application predicts whether a person is obesity and/or diabetic based on the provided inputs.
- **Efficient Data Processing:** Utilizes pipelines and column transformers for efficient data handling and model predictions.



