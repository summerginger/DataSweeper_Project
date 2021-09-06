# Topic : Credit Card Approval Prediction  <img align="right" src="https://user-images.githubusercontent.com/82733723/131945205-72772eea-1781-4977-ac31-f0f8327ed418.png">

## 1. Overview of the Project


The objective of this project is to help a financial institution to decide whether to issue a credit card to an applicant or not. Using personal information and data submitted by credit card applicants, the model will predict the probability of future defaults and credit card borrowings.

## 2. Topic Selection Criteria

In today's fast-paced and high-tech world, credit scores can further impact many financial transactions, including personal loans, auto loans, mortgages, and credit cards. Credit scoring is a standard method of risk control in the financial industry. It uses the personal information and data submitted by credit card applicants to assess their creditworthiness. For protecting an individual's credit score, the financial institution has a responsibility to control and objectively quantify the magnitude of risk and credit card issuance. 

To help automate the process of credit card application approvals, new advanced machine learning algorithms will be used to predict whether a credit card applicant will default on their payments or not.

Datasets will be cleaned and analysed so that they can be used in multiple machine learning models. Following the results and information derived from the different models, recommendations will be provided so the financial institution can choose which model to use.



## 3. Overview of dataset
 
### The Dataset contains two files:

1. **Demographics & application data - "application_record.csv"**

   This data has been provided by the applicants at the time of the credit card application. It contains demographic information including gender, car & real estate ownership, income level, education, occupation, marital status, contact information.
   
 

 
|application_record.csv |||
| ------------- |-------------| -----|
| Feature name        |    Explanation       |  Remarks/Variable Type |
|    ID   | Client number |   |
| CODE_GENDER   | Gender     | Binary    |
|  FLAG_OWN_CAR |	Is there a car|  Binary   |  
| FLAG_OWN_REALTY	|Is there a property| Binary |
| CNT_CHILDREN |	Number of children | Continuous  |
| AMT_INCOME_TOTAL |	Annual income | Continuous  |
| NAME_INCOME_TYPE |	Income category   | Categorical   |
| NAME_EDUCATION_TYPE |	Education level    | Categorical   |
| NAME_FAMILY_STATUS	|Marital status    | Categorical   |
|  NAME_HOUSING_TYPE |	Way of living   |  Categorical  |
|  DAYS_BIRTH |	Birthday     |  Count backwards from current day (0), -1 means yesterday. / Continuous |
| DAYS_EMPLOYED |	Start date of employment | Count backwards from current day(0). If positive, it means the person currently unemployed. / Continuous |
| FLAG_MOBIL |	Is there a mobile phone   |  Binary  |
| FLAG_WORK_PHONE	| Is there a work phone | Binary   |
| FLAG_PHONE |	Is there a phone     | Binary   |
| FLAG_EMAIL	| Is there an email  | Binary   |
|  OCCUPATION_TYPE |	Occupation   | Categorical   |
|  CNT_FAM_MEMBERS |	Family size  | Continuous   |


##

2. **Credit Bureau data - "credit_record.csv"** 
   
   Data obtained from the credit bureau showing payment experience and the date of the last data extraction.  
   


|credit_record.csv | | |
--- | --- | ---
*Feature name*  | `Explanation` | **Remarks**
ID   | Client number |   
MONTHS_BALANCE   | Record month    |  The month of the extracted data is the starting point, backwards, 0 is the current month, -1 is the previous month, and so on / Continuous 
STATUS |   Status  |   0: `1-29 days past due` 1: `30-59 days past due` 2: `60-89 days overdue` 3: `90-119 days overdue` 4: `120-149 days overdue` 5: `Overdue or bad debts, write-offs for more than 150 days` C: `paid off that month` X: `No loan for the month` / Categorical
 
 
### Description of data source
This dataset is from [kaggle](https://www.kaggle.com/rikdifos/credit-card-approval-prediction-using-ml), we have selected the highest number of [usability, votes and credits](https://www.kaggle.com/rikdifos/datasets). The precision of data is over 0.5. 

 The binary features including the following: 
- Gender
- Having a car or not
- Having house reality or not
- Having a phone or not
- Having an email or not
- Having a Work Phone or not


## 4. Question the team wants to answer with the data

Based on the dataset, what are the standard requirements for an individual to be approved for a credit card?




## 5. Data Exploration Phase

### Data Cleaning and Preparation
  
 However, we will drop a few columns where consideration does not apply to the prediction. 
 
## 6. Analysis Phase 
 
### Machine Learning Model

The purpose of this study is to find the best machine learning model to predict credit card approval for future credit card applicants. The machine learning models used in this dataset will be based on supervised binary classification models. This is because the target variable for this dataset is a binary outcome, i.e. approve (1) or not approve (0). Classification machine learning models such as Logistic Regression, Support Vector Machines, Decision Trees, Random Forests, and Gradient Boosted Trees, will be applied to the data. 

Before any machine learning models are applied on the dataset, encoding labels, scaling and normalizing data must be done to ensure machine learning models such as SVM to perform at its optimized conditions. 

The output label for this dataset will be the status of the applicant in the credit_records.csv file. As shown in Overview of Dataset, the status of the applicants are categorized into 8 outcomes (0, 1, 2, 3, 4, 5, X, and C). The challenge here is to categorize which applicant status is deemed “good” or “bad”. Hence, for this dataset, applicants who have a status of 0-5 are considered as “bad” applicants, i.e. not approved (0), and applicants who have a status of C or X are considered as “good” applicants, i.e. approved(1). This can be done with the .replace() method using the pandas library. 

Connecting the machine learning model to the database is another challenge that must be overcome. For this, a PostgreSQL database will be created and integrated with the Jupyter Notebook file for machine learning using 3 different libraries. 

These libraries are:
- ipython-sql
- SQLALCHEMY
- A python database API (DBAPI) library (i.e. psycopg2)
- 
Taking data from the provisional database is demonstrated in the demo.ipynb file from the Kaggle_Dataset folder.

Datasets will be cleaned and analysed so that they can be used in multiple machine learning models. Following the results and information derived from the different models, recommendations will be provided so the financial institution can choose which model to use.




### Database


The database for this project is a PostgreSQL database. The database is created through pgAdmin and the structure and connections of the tables can be demonstrated in the PostGresDB_Draft.txt from the **Kaggle_Dataset folder.** The machine learning model will be connected as shown in the demo.ipynb file from the Kaggle_Dataset folder.

The ERD diagram for our provisional database is also provided in the PostGreSQL_Database folder.

<p align="center">
<image src="https://user-images.githubusercontent.com/82583576/132156481-105fea27-3ee5-4101-9a4b-e21047c3fdbc.png"
</p>

 
 ## 7. Technologies

<p align="center">
<image src="https://user-images.githubusercontent.com/82583576/132108627-97f92b4f-57e3-495a-8665-37374aff7df6.PNG"
</p>


 
 
## 8. Result of the Analysis
 


## 9. Recommendations

###
 
***Resources***
* [Kaggle Link](https://www.kaggle.com/rikdifos/credit-card-approval-prediction/code)

* [github markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)

***Team communication protocols***
 
This week, each team member will choose a shape, with each shape responsible for a specific task. The shapes to choose from are square, circle, triangle, and X. 
We will use whatsapp,slack,zoom meeting, Github project and [google docs](https://docs.google.com/document/d/1NugbKt5vuU91jPWE3nzVjTbBYoNdhf9_9ET2l-FNRmI/edit?usp=sharing) tools for communications.
 
![1st segment task assigned](https://user-images.githubusercontent.com/82733723/131895610-d1dd9b98-d97b-4531-8029-8e3862d66451.png) 
 


