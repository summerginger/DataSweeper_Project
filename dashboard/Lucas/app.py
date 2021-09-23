from pickle import load
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import pickle


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/prediction_form')
def prediction_form():
    return render_template('form.html')
 
@app.route('/result/', methods = ['POST', 'GET'])
def result():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/prediction_form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        user_info = []
        for key,value in form_data.items():
            user_info.append({key:value})
        
        # user_info = pd.DataFrame(user_info)

        # # Import pickle library
 


        filename = 'randomForest_SMOTE_new.sav'
        loaded_dict = pickle.load(open(filename, 'rb'))
        model = loaded_dict["model"]
        scaler = loaded_dict["scaler"]
        scaled_data = scaler.transform(user_info)
        
        predictions = model.predict(scaled_data)

        return render_template('result.html',predictions = predictions)

if __name__ == "__main__":
   app.run()

