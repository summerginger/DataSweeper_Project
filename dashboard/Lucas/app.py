from flask import Flask, render_template, redirect, url_for, request

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
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('result.html',form_data = form_data)

if __name__ == "__main__":
   app.run()