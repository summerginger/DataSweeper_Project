from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    import pandas as pd
    from collections import Counter
    import warnings
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
    warnings.filterwarnings('ignore')

    credit_application_df = pd.read_csv("../../Resources/datasets/ML_credit_application.csv")
    credit_application_df.drop(['ID'], axis=1, inplace=True)
    # Create our features
    X = credit_application_df.drop(columns="STATUS_y")

    # Create our target
    y = pd.DataFrame(credit_application_df["STATUS_y"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # Creating a StandardScaler instance.
    scaler = StandardScaler()
    # Fitting the Standard Scaler with the training data.
    X_scaler = scaler.fit(X_train)

    # Scaling the data.
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)

    # Import pickle library
    import pickle

    filename = 'randomForest_SMOTE.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    predictions = loaded_model.predict(X_test_scaled)
    
    acc_score = accuracy_score(y_test, predictions)

    return render_template("index.html", predictions = predictions)


if __name__ == "__main__":
   app.run()