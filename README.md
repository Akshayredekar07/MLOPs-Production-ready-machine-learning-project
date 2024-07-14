# MLOPs-Production-ready-machine-learning-project 

## Overview

### Understanding the Problem Statement
The goal of this project is to predict whether a US visa application will be approved or not based on a set of features such as continent, education, job experience, training, employment, current age, etc.

### Understanding the Solution
We will explore both Machine Learning (ML) classification algorithms and a custom Artificial Neural Network (ANN) to create a predictive model.

### Code Understanding and Walkthrough
The code will be thoroughly documented to guide you through the process, from loading data to deploying the model.

### Understanding the Deployment
We will deploy the model using Docker and cloud services, add a self-hosted runner, and set up workflows for continuous integration and deployment.

## Deployment

### Docker
Instructions for containerizing the application using Docker.

### Cloud Services
Steps for deploying the application to cloud platforms.

### Adding Self-Hosted Runner
Guide for setting up a self-hosted runner for continuous integration.

### Workflows
Configuration of workflows for automating tasks such as testing, building, and deploying.

## Problem Statement

The task is to predict the approval status of a US visa application based on the following features:

- **Continent**: Asia, Africa, North America, Europe, South America, Oceania
- **Education**: High School, Master's Degree, Bachelor's, Doctorate
- **Job Experience**: Yes, No
- **Required Training**: Yes, No
- **Number of Employees**: 15000 to 40000
- **Region of Employment**: West, Northeast, South, Midwest, Island
- **Prevailing Wage**: 700 to 70000
- **Contract Tenure**: Hour, Year, Week, Month
- **Full Time**: Yes, No
- **Age of Company**: 15 to 180

## Solution Approach

### 1. Machine Learning: 
Using ML classification algorithms to predict visa approval.

### 2. Deep Learning:
Developing a custom ANN with a sigmoid activation function for prediction.

### Solution Proposed

1. Load the data from the database.
2. Perform Exploratory Data Analysis (EDA) and feature engineering to select the desirable features.
3. Fit the ML classification algorithms and determine which one performs best.
4. Select the top-performing models and tune their hyperparameters.
5. Choose the best model based on desired metrics.

- Flowchart 
`
https://whimsical.com/
`
- MLOPS tool 
`
https://www.evidentlyai.com/ 
`

** Creating the virtualenvirment**
```bash
conda create -n visa python=3.9 -y
```

```bash
conda activate visa
```

```bash
pip install -r requirements.txt
```