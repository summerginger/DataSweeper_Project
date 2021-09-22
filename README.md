<p align="center">
<img src="https://user-images.githubusercontent.com/82583576/134264658-70a9db96-b267-49f3-90f2-3c1b09e0d839.PNG" width="1000" height="100">
</p>     

# Credit Card Approval Prediction 


> Presentation [Google Slides](https://docs.google.com/presentation/d/1X4rjV2lNl-p0wkA_8FDF0slwy_Eo9o3j9r64zUZSoxs/edit#slide=id.gc6f980f91_0_0)


 ## Table of Contents 

- [Overview of the Project](https://github.com/summerginger/DataSweeper_Project#1-overview-of-the-project)

- [Topic Selection Criteria](https://github.com/summerginger/DataSweeper_Project#2-topic-selection-criteria) 

- [Overview of dataset](https://github.com/summerginger/DataSweeper_Project#3-overview-of-dataset)


        

- [Question](https://github.com/summerginger/DataSweeper_Project#4-question-the-team-wants-to-answer-with-the-data) 

- [Database](https://github.com/summerginger/DataSweeper_Project#6-database)

- [Machine Learning](https://github.com/summerginger/DataSweeper_Project/blob/main/README.md#5--machine-learning)

- [Result of the Analysis](https://github.com/summerginger/DataSweeper_Project#8-result-of-the-analysis)

- [Recommendations](https://github.com/summerginger/DataSweeper_Project#9-recommendations)

- [Technologies](https://github.com/summerginger/DataSweeper_Project#7-technologies)

- [Dashboard](https://github.com/summerginger/DataSweeper_Project#9-dashboard-description)

- Data Citations


## 1. Overview of the Project


The objective of this project is to help a financial institution to decide whether to issue a credit card to an applicant. Using personal information and data submitted by credit card applicants, the model will predict the probability of future defaults and credit card borrowings.

The decision of approving a credit card is mainly dependent on the personal and financial background of  the applicant. Factors like, age, gender, income, employment status, credit history and other attributes all carry weight in the approval decision. 

Credit analysis focus on recognizing, assessing and reducing the financial or other risks that could lead to loss involved in the transaction. 

There are two basic risks: 

- Business loss that results from not approving the good candidate
- Financial loss that results from by approving a non-credit worthy candidate. 
 
It is very important to manage credit risk and handle challenges efficiently for credit decision as it can have adverse effects on credit management. 


## 2. Topic Selection Criteria

In today's fast-paced and high-tech world, credit scores can further impact many financial transactions, including personal loans, auto loans, mortgages, and credit cards. Credit scoring is a standard method of risk control in the financial industry. It uses the personal information and data submitted by credit card applicants to assess their creditworthiness. To prenet its losses, the financial institution has a responsibility to control and objectively quantify the magnitude of risk and credit card issuance. 

The primary objective of this analysis is to implement the data mining techniques on a credit card applicant dataset. Data-based conclusions about probability of repayment can be derived and recommendations can be put forward.

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

1. Based on the dataset, what are the standard requirements for an individual to be approved for a credit card?

2. Can the model minimize the following risks? 

- Loss from not approving the good applicant
- Loss resulting from approving a non-credit worthy candidate


## 5.  Machine Learning  

 > Preliminary Data Preprocessing
 
### Data Cleaning and Preparation 

#### Choosing "good" and "bad" applicants
Before we conduct analysis and/or machine learning on our dataset, we must perform preliminary data preprocessing. The first preliminary data preprocessing we conducted was to determining "good" and "bad" applicants in the **credit_records.csv** file. As we can see from **Overview of Dataset**, the **credit_record.csv** contains the information of all the applicants and their payment experience. We can see the status of payment of the card holder's credit account from the starting month of their credit account until the current month. From [additional sources](https://www.valuepenguin.com/what-happens-if-you-dont-pay-credit-card-bill), we have found that credit accounts are closed and sold to a collection agency when an account has not recieved payment for 3 or more months. With this added information came the idea of how to determine how and applicant is "good" or "bad" for credit card companies. We decided to select applicants who have 3 or more of late payements (i.e. 3 times or more of "STATUS" of any 0-5) to be "bad" applicants, and any applicants who have less than 3 late payments as "good" applicants. The dataframe containing the modified status of applicants in under the name **new_credit** and the process of the preliminary data preprocessing steps above are demonstrated in cells 20 to 26 of **machine_learning.ipynb**. 

#### Cleaning and encoding data
The next preliminary data preprocessing we conducted was to clean, encode, and rescale data from the **application_record.csv** file. After converting the csv file to a dataframe, the first step of cleaning the **aplication_record_df** was to remove duplicates of records and filling in null values. We successfully removed duplicated records using the .drop_duplicates() method and filled in the null values in the "OCCUPATION_TYPE" column as "No Occupation Type". We then continued to encode the gender, owning a car, owning realty, income category, education level, Marital status, housing type, and occupation columns using the .get_dummies() method. Following this, we rescaled the annual income column by dividing the whole column by 10000 and created new columns for age and employment period as they were initially counted in days and not years. We then dropped days of birth, days of employement ,'FLAG_MOBIL' ,'FLAG_WORK_PHONE' ,'FLAG_PHONE' ,'FLAG_EMAIL' ,'Months_from_Today' ,'MONTHS_BALANCE' , and id columns as they are not important features for predicting whether an applicant pays their credit bills or not. The process of cleaning, and encoding of the **application_record_df** is demonstrated in the cells 29 to 54 of **machine_learning.ipynb**. We then merged the two dataframes **new_credit** and **application_record_df** to create the dataframe for the machine learning models, and export the merged dataset as a csv file for us to import to the PostgreSQL databse.

### Description of Machine Learning 
The machine learning models used in this dataset will be based on supervised binary classification models. This is because the target variable ("STATUS_y") for this dataset is a binary outcome, i.e. approve (1) or not approve (0). Classification machine learning models such as Logistic Regression, Decision Trees, Random Forests, and Gradient Boosted Trees, will be applied to the data.

### Connecting machine learning model with databse
But before we start our machine learning process, we must first import the dataset from the database. For this, a PostgreSQL database will be created and integrated with the Jupyter Notebook file for machine learning using 3 different libraries. 

These libraries are:
- ipython-sql
- SQLALCHEMY
- A python database API (DBAPI) library (i.e. psycopg2)
 
 > Feature Selection and Splitting Data
 
After importing the dataset, we then selected our features to be all the columns execpt for column "STATUS_y" and the target variable to be "STATUS_y". We then continued to split the dataset into training and testing sets, 75% training and 25% testing and we scaled the data using StandardScaler() for the features of the training and testing sets. 

The process above is demonstrated in cells 57-70 of **machine_learning.ipynb**.

 >  Preliminary feature engineering and preliminary feature selection, including decision-making process
   
### Balancing Data and Machine learning Results
Now, we are ready for machine learning. The dataset is unbalanced and to address this, we will be using sampling techniques to balance the dataset. At the end of the analysis, we will choose the best combination of sampling technique and machine learning model that can predict credit card approval. The first two sampling technique that we used are both oversampling technique called Random Oversampling and Synthetic Minority Oversampling Technique (SMOTE). The results for Logistic Regression, Decision Trees, Random Forests, and Gradient Boosted Trees for both oversampling techniques are shown in the tables below.

![machine learning results](images/MC_results1.PNG)

The following tables are the results for the logistic regression model for an undersampling technique called ClusterCentroids and a combination sampling technique called SMOTEENN.

![machine learning results 2](images/MC_results2.PNG)

> Limitations and benefits

From our results, we can see that RandomForest model and the SMOTE gave the best combination for predicting Credit Card Approval. However, the percision and recall for predicting "good" applicants are around 50% which is as good as a coin toss. Having percision around 50% means that if an applicant is approved to get a card by the model, the applicant is 50% likely to get a real credit card from the credit card company. And having a recall/sensitivity of 50% means that if a person already own a credit card from the credit card company, the model will have 50% chance of predicting that the applicant get a credit card from the credit card company. The reason behind the low percision and recall for approved applicants may be due to the fact that the dataset is imbalanced and hence it is more difficult for the machine learning models to predict good applicants. If more time were given to optimize this model, we would like to add more training data containing approved aplicants to strenghthen the percision and recall of approved applicants.

## 6. Database

The database for this project is a PostgreSQL database. The database is created through pgAdmin and the structure and connections of the tables can be demonstrated in the PostGresDB_Draft.txt from the **PostgreSQL_Database folder.** 

The machine learning model will be connected as shown in the demo.ipynb file from the **machine_learning** folder.

The ERD diagram for our provisional database is also provided in the PostGreSQL_Database folder.

<p align="center">

<image src="https://user-images.githubusercontent.com/82583576/132156481-105fea27-3ee5-4101-9a4b-e21047c3fdbc.png" width="400">

</p>

 
 
 ## 7. Technologies

<p align="center">

<image src="https://user-images.githubusercontent.com/82583576/133891249-6d3e4655-dae0-496c-b080-3d1f71d48f1c.png" width="500">

</p>

## 8. Dashboard Description
 
Tools: JavaScript, HTML, D3.Js
 
Interactive Features : 
 
- Age
- Education
- Occupation
- Net income
- Number of family members

> Dashboard [click here](https://summerginger.github.io/DataSweeper_Project/)
 
## 9. Result of the Analysis
      ***TBA***


## 10. Recommendations
      ***TBA***


### GITHUB Individual Branches
Each team member's brnch has been named as follows: "First_name_DeliverableN", where N stands for the deliverable number. Example for the first deliverable, "Binoy_Deliverable1"
 
- Binoy Luckoo's Branch Name:  Binoy_DeliverableN 
- Samir Rifi's Branch Name:  samir_DeliverableN
- Jane Huang's Branch Name: jane_DeliverableN
- Lucas Chandra's Branch Name: lucas_DeliverableN


## Resources
* [Kaggle Link](https://www.kaggle.com/rikdifos/credit-card-approval-prediction/code)

* [github markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)
 
<p align="center"> 
<img src="https://user-images.githubusercontent.com/82733723/133947489-cf784a14-c88c-4e3b-8e86-5fb6fc5e599e.png" width="600" height="300">
</p>
