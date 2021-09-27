from pickle import load
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import pickle


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route('/livedemo')
def livedemo():
    return render_template('livedemo.html')

@app.route('/result/', methods = ['POST', 'GET'])
def result():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/prediction_form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        user_info_dict = {}
        for key,value in form_data.items():
            user_info_dict[key] = value
        
        user_info = [user_info_dict]
        # Create dataframe for user_info
        user_info_df = pd.DataFrame(user_info)

        # # Custom encode data
        # # ----------------------------------------------------------------------------------------------------
        gender_encode = {
            "M" : 0,
            "F" : 1
        }
        own_car_encode = {
            "N" : 0,
            "Y" : 1
        }
        own_realty_encode = {
            "N" : 0,
            "Y" : 1
        }
        own_occupation_encode = {
            "Accountants" : 0,
            "Cleaning staff" : 1,
            "Cooking staff" : 2,
            "Core staff" : 3,
            "Drivers" : 4,
            "HR staff" : 5,
            "High skill tech staff" : 6,
            "IT staff" : 7,
            "Laborers" : 8,
            "Low-skill Laborers" : 9,
            "Managers" : 10,
            "Medicine staff" : 11,
            "No Occupation Type" : 12,
            "Private service staff" : 13,
            "Realty agents" : 14,
            "Sales staff" : 15,
            "Secretaries" : 16,
            "Security staff" : 17,
            "Waiters/barmen staff" : 18
        }
        own_income_type = {
            "Commercial associate" : 0,
            "Pensioner" : 1,
            "State servant" : 2,
            "Student" : 3,
            "Working" : 4,
        }
        own_education_type = {
            "Academic degree" : 0,
            "Higher education" : 1,
            "Incomplete higher" : 2,
            "Lower secondary" : 3,
            "Secondary / secondary special" : 4,
        }
        own_family_status = {
            "Civil marriage" : 0,
            "Married" : 1,
            "Separated" : 2,
            "Single / not married" : 3,
            "Widow" : 4,
        }
        own_housing_type = {
            "Co-op apartment" : 0,
            "House / apartment" : 1,
            "Municipal apartment" : 2,
            "Office apartment" : 3,
            "Rented apartment" : 4,
            "With parents" : 4
        }

        user_info_df["CODE_GENDER"] = user_info_df["CODE_GENDER"].apply(lambda x: gender_encode[x])
        user_info_df["FLAG_OWN_CAR"] = user_info_df["FLAG_OWN_CAR"].apply(lambda x: own_car_encode[x])
        user_info_df["FLAG_OWN_REALTY"] = user_info_df["FLAG_OWN_REALTY"].apply(lambda x: own_realty_encode[x])
        user_info_df["OCCUPATION_TYPE"] = user_info_df["OCCUPATION_TYPE"].apply(lambda x: own_occupation_encode[x])
        user_info_df["NAME_INCOME_TYPE"] = user_info_df["NAME_INCOME_TYPE"].apply(lambda x: own_income_type[x])
        user_info_df["NAME_EDUCATION_TYPE"] = user_info_df["NAME_EDUCATION_TYPE"].apply(lambda x: own_education_type[x])
        user_info_df["NAME_FAMILY_STATUS"] = user_info_df["NAME_FAMILY_STATUS"].apply(lambda x: own_family_status[x])
        user_info_df["NAME_HOUSING_TYPE"] = user_info_df["NAME_HOUSING_TYPE"].apply(lambda x: own_housing_type[x])
        user_info_df[["CNT_CHILDREN", "AMT_INCOME_TOTAL", "CNT_FAM_MEMBERS", "AGE", "EMPLOYMENT_PERIOD"]] = user_info_df[["CNT_CHILDREN", "AMT_INCOME_TOTAL", "CNT_FAM_MEMBERS", "AGE", "EMPLOYMENT_PERIOD"]].apply(pd.to_numeric)
        user_info_df["AMT_INCOME_TOTAL"] = user_info_df["AMT_INCOME_TOTAL"] / 100000
        # # -----------------------------------------------------------------------------------------------------
        
        # Import pickle file and load model and scaler
        filename = 'randomForest_SMOTE_new.sav'
        loaded_dict = pickle.load(open(filename, 'rb'))
        model = loaded_dict["model"]
        scaler = loaded_dict["scaler"]

        # Scale user info
        scaled_data = scaler.transform(user_info_df)
                
        # Make prediction using rf_model
        predictions = model.predict(scaled_data)

        return render_template('results.html', predictions=predictions)



@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/ml')
def machineLearning():
    return render_template('ML.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')
 

if __name__ == "__main__":
   app.run()

