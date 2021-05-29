#!/usr/bin/env python3

# import relevant libraries
from flask import Flask, request, render_template
from joblib import load
import pandas as pd
import numpy as np


# Load model
loaded_model = load('random_forest_model.joblib')
scaler = load('scaler.joblib')

print('@@ Model Loaded!')

def predict_survivors(data_ints):
    """ Get Data from Form and Predict Class """

    # convert list of tuples to an array of appropriate shape and then to a dataframe
    query_data = np.array(data_ints).reshape(1, -1)
    
    # scale the data using standard scaler
    scaled_data = scaler.transform(query_data)

    # predict the scaled data
    result = loaded_model.predict(scaled_data)

    print('@@ Scaled Data = ', scaled_data)
    print('@@ Raw result = ', result)
        
    return result


# api definition
app = Flask(__name__)

# display the home page index.html
@app.route('/')
def display_form():
    return render_template('./index.html')
    

# ---------------------------------------------------------------------------------------------------
# define the predict function
@app.route('/predict', methods= ['POST']) # endpoint url will contain /predict
def predict():
    """display the prediction page"""

    if request.method == 'POST':
        data_dict = request.form.to_dict() # convert the form fields to dictionary
        # the dictionary above also returns a value for the predict button as an empty string,
        # we'll subset this dictionary using a condition
        a_subset = {key: value for key, value in data_dict.items() if value != ''}
        data_list = list(a_subset.values()) # convert the values of the dictionary to list

        # get the index of the vaues in the list
        sex = data_list[0]; pclass = data_list[2]; age = data_list[3]; sibsp = data_list[4]; parch = data_list[5]
        fare = data_list[6]; embarked = data_list[1]

        # order the values in the format of the training data
        ord_data_list = [pclass, sex, age, sibsp, parch, fare, embarked]

        # convert the ordered values to integers
        data_ints = list(map(int, ord_data_list)) 

        print('@@ Raw Data = ', data_ints)
        prediction = predict_survivors(data_ints)

        if prediction >= 0.5: # Adjust the threshold to capture more defaulters due to class imbalance of the training data
            pred = 'Survived'
        else:
            pred = 'Died'

    return render_template('./result.html', prediction = pred)

        
# function that prints the head of the cleaned dataset
@app.route('/view_data', methods = ['POST'])
def get_head_tail_info():

    # get the cleaned dataset
    read_file = pd.read_csv('./datasets/titanic_clean.csv')

    # get the form submit button whose name is head and value is head
    if request.form.get("head") == "head":
        # show just the head
        return read_file.head().to_html()

    # get the form submit button whose name is tail and value is tail
    elif request.form.get("tail") == "tail":
        # show just the tail
        return read_file.tail().to_html()

    # get the form submit button whose name is info and value is info
    elif request.form.get('info') == "info":
        # return the dataset description
        return read_file.describe().to_html()

# write the main function
if __name__ == '__main__':
    app.run(debug=True)