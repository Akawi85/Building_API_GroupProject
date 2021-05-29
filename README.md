# Predict Titanic Survivors

This project builds an API that predicts Titanic survivors given the following columns `Pclass`, `Sex`, `Age`, `Number of Siblings/Spouse`, `Number of Parents/Children`, `Passenger Fare`, and `Port of Embarkation`.  
Several Classifier algorithms were used on the training data, but the Random Forest Classifier Performed best on both `accuracy`, `f1` and `ROC_AUC` metrics, hence its usage for training the entire [cleaned dataset](https://github.com/Akawi85/predict_titanic_survivors/blob/main/datasets/titanic_clean.csv).

The project made use of the popular titanic dataset which can be gotten from [here](https://raw.githubusercontent.com/Akawi85/Building_API_GroupProject/main/datasets/titanic.csv).

In order to execute this project on your local machine, you are expected create a python 3 virtual environment ([see how here](https://docs.google.com/document/d/19IpozHrM38HzVSI4PjwRFJSNeLdcceUKg98fr2Db-DQ/edit)) and have pip installed in your environment. You are also expected to install all the necessary modules and libraries using pip in the [requirements](https://github.com/Akawi85/predict_titanic_survivors/blob/main/requirements.txt) file.  

To perform prediction:
- run the `api.py` script and click on the local host link
- this takes you to a html page, where you are expected to fill out the details of a passenger
- Click the `Predict` button to see if the passenger died or survived.
- You can also get the top view, bottom view or basic information of the dataset used for training the model, by clicking `Top view`, `Bottom view` or `Show dataset info` respectively.