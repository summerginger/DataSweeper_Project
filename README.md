
<p align="center">
<img src="https://user-images.githubusercontent.com/82583576/134264658-70a9db96-b267-49f3-90f2-3c1b09e0d839.PNG" width="1000" height="100">
</p>     


# Credit Card Approval Prediction 

> Presentation [Google Slides](https://docs.google.com/presentation/d/1X4rjV2lNl-p0wkA_8FDF0slwy_Eo9o3j9r64zUZSoxs/edit#slide=id.gc6f980f91_0_0)

>  Dashboard [click here](https://summerginger.github.io/DataSweeper_Project/index.html)
<img align="right" src="https://user-images.githubusercontent.com/82733723/133947489-cf784a14-c88c-4e3b-8e86-5fb6fc5e599e.png">


 ## Table of Contents 

1. [Overview of the Project](https://github.com/summerginger/DataSweeper_Project#1-overview-of-the-project)

2. [Topic Selection Criteria](https://github.com/summerginger/DataSweeper_Project#2-topic-selection-criteria) 

3. [Overview of dataset](https://github.com/summerginger/DataSweeper_Project#3-overview-of-dataset)

4. [Question](https://github.com/summerginger/DataSweeper_Project#4-question-the-team-wants-to-answer-with-the-data) 

5. [Machine Learning](https://github.com/summerginger/DataSweeper_Project/blob/main/README.md#5--machine-learning)

6. [Database](https://github.com/summerginger/DataSweeper_Project#6-database)

7. [Technologies](https://github.com/summerginger/DataSweeper_Project#7-technologies)

8. [Dashboard](https://github.com/summerginger/DataSweeper_Project#8-dashboard-description)

9. [Result of the Analysis](https://github.com/summerginger/DataSweeper_Project#9-Result-of-the-Analysis)

10. [Recommendations](https://github.com/summerginger/DataSweeper_Project#10-recommendations)

11. [Team](https://github.com/summerginger/DataSweeper_Project#11-team) 

12. [Citations](https://github.com/summerginger/DataSweeper_Project#12-Citations)


## 1. Overview of the Project


The objective of this project is to help a financial institution to decide whether to issue a credit card to an applicant. Using personal information and data submitted by credit card applicants, the model will predict the probability of future defaults and credit card borrowings.

The decision of approving a credit card is mainly dependent on the personal and financial background of  the applicant. Factors like, age, gender, income, employment status, credit history and other attributes all carry weight in the approval decision. 

Credit analysis focus on recognizing, assessing and reducing the financial or other risks that could lead to loss involved in the transaction. 

There are two basic risks: 

- Business loss that results from not approving the good candidate
- Financial loss that results from by approving a non-credit worthy candidate. 
 
It is very important to manage credit risk and handle challenges efficiently for credit decision as it can have adverse effects on credit management. 


## 2. Topic Selection Criteria

In today's fast-paced and high-tech world, credit scores can further impact many financial transactions, including personal loans, auto loans, mortgages, and credit cards. Credit scoring is a standard method of risk control in the financial industry. It uses the personal information and data submitted by credit card applicants to assess their creditworthiness. To minimize its losses, the financial institution has a responsibility to control and objectively quantify the magnitude of risk and credit card issuance. 

The primary objective of this analysis is to implement the data mining techniques on a credit card applicant dataset. Data-based conclusions about probability of repayment can be derived and recommendations can be put forward.


Datasets will be cleaned and analysed so that they can be used in multiple machine learning models. Following the results and information derived from the different models, recommendations will be provided so the financial institution can choose which model to use.

>[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)

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
 
 >[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)
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

### Preliminary Data Preprocessing
 

### Data Cleaning and Preparation 

#### Choosing "good" and "bad" applicants

Preliminary data preprocessing must be completed before any analysis and/or machine learning models can be used on the dataset. 

The following steps were undertaken to pre-process the datasets provided by the bank:

**1. Determine "good" and "bad" applicants in the **credit_records.csv** file** 

As illustrated in the **Overview of Dataset**, the **credit_record.csv** contains the information of all the applicants and their payment experience. 
The status of payment of the card holder's credit account from the starting month of their credit account until the current month is provided. 
From [additional sources](https://www.valuepenguin.com/what-happens-if-you-dont-pay-credit-card-bill), credit card accounts are closed and sold to a collection agency when an account has not recieved payment for 3 or more months. 

With this added information came the idea of how to determine how an applicant is "good" or "bad" for credit card companies. 
Applicants with 3 or more late payements (i.e. 3 times or more of "STATUS" of any 0-5) were classified be "bad" applicants, and any applicants who have less than 3 late payments as "good" applicants. The dataframe containing the modified status of applicants in under the name ***new_credit - TBR*** and the process of the preliminary data preprocessing steps above are demonstrated in cells 20 to 26 of ***machine_learning.ipynb TBR***. 

**2. Cleaning and encoding data** ***May need to change this section as we made some changes as to how and where the dataset was cleaned and merged, i.e. in PostGres vs Python DF**

The next preliminary data preprocessing was to clean, encode, and rescale data from the **application_record.csv** file.

After converting the csv file to a dataframe, the first step of cleaning the **aplication_record_df** was to remove duplicate records and filling in null values. 
The .drop_duplicates() method was used to remove duplicates and filled in the null values in the "OCCUPATION_TYPE" column as "No Occupation Type". 

Further encoding of gender, owning a car, owning realty, income category, education level, Marital status, housing type, and occupation columns was done.

The annual income column was re-scaled by dividing the whole column by 10000 and new columns for age and employment period were created as they were initially counted in days and not years.

Features, such as days of birth, days of employment ,'FLAG_MOBIL' ,'FLAG_WORK_PHONE' ,'FLAG_PHONE' ,'FLAG_EMAIL' ,'Months_from_Today' ,'MONTHS_BALANCE' and 'id' were dropped as they were not deemed important for predicting whether an applicants pay their credit cards or not. 

The process of cleaning, and encoding of the **application_record_df** is demonstrated in the cells 29 to 54 of ***machine_learning.ipynb TBR***. 


The two dataframes **new_credit** and **application_record_df** were merged to create the dataframe for the machine learning models, and export the merged dataset as a csv file from the PostgreSQL databse hosted on AWS RDS.

### Description of Machine Learning 

The target variable ("STATUS_y") for this dataset is binary, i.e. approve (1) or not approve (0).
Hence, the machine learning models used will be based on supervised binary classification models.  Classification machine learning models such as Logistic Regression, Decision Trees, Random Forests, and Gradient Boosted Trees, will be applied to the data.

### Connecting the Database to the Machine Learning Models

The data is in a PostgreSQL database hosted on AWS RDS. The two files making up the dataset will be merged in PostgreSQL and then integrated with the Jupyter Notebook file for machine learning using 3 different libraries. 

- Cleaning and encoding data

The next preliminary data preprocessing we conducted was to clean, encode, and rescale data from the **application_record.csv** file. After converting the csv file to a dataframe, the first step of cleaning the **aplication_record_df** was to remove duplicates of records and filling in null values. We successfully removed duplicated records using the .drop_duplicates() method and filled in the null values in the "OCCUPATION_TYPE" column as "No Occupation Type". We then continued to encode the gender, owning a car, owning realty, income category, education level, Marital status, housing type, and occupation columns using the .get_dummies() method. Following this, we rescaled the annual income column by dividing the whole column by 10000 and created new columns for age and employment period as they were initially counted in days and not years. We then dropped days of birth, days of employement ,'FLAG_MOBIL' ,'FLAG_WORK_PHONE' ,'FLAG_PHONE' ,'FLAG_EMAIL' ,'Months_from_Today' ,'MONTHS_BALANCE' , and id columns as they are not important features for predicting whether an applicant pays their credit bills or not. The process of cleaning, and encoding of the **application_record_df** is demonstrated in the cells 29 to 54 of **machine_learning.ipynb**. We then merged the two dataframes **new_credit** and **application_record_df** to create the dataframe for the machine learning models, and export the merged dataset as a csv file for us to import to the PostgreSQL databse.

- Description of Machine Learning 

The machine learning models used in this dataset will be based on supervised binary classification models. This is because the target variable ("STATUS_y") for this dataset is a binary outcome, i.e. approve (1) or not approve (0). Classification machine learning models such as Logistic Regression, Decision Trees, Random Forests, and Gradient Boosted Trees, will be applied to the data.

- Connecting machine learning model with databse

But before we start our machine learning process, we must first import the dataset from the database. For this, a PostgreSQL database will be created and integrated with the Jupyter Notebook file for machine learning using 3 different libraries. 


These libraries are:
- ipython-sql
- SQLALCHEMY
- A python database API (DBAPI) library (i.e. psycopg2)
 
>[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)

 ### Feature Selection and Splitting Data
 
All the columns, except for the column "STATUS_y" from the pre-processed dataset were used as features to build the models. The target variable was determined to be "STATUS_y". 
The dataset was split into training and testing sets, 75% training and 25% testing. 
The data was scaled using StandardScaler() for the features of the training and testing sets. 


***The process above is demonstrated in cells 57-70 of **machine_learning.ipynb**.TBR*** 

 >  Preliminary feature engineering and preliminary feature selection, including decision-making process
   
### Balancing Data and Machine Learning Results

The next step is to feed the cleaned dataset into multiple Machine Learning models to find out which model is the best suited for the dataset.

The dataset is unbalanced and to address this, different sampling techniques will be used to balance the dataset. 

Two oversampling techniques, Random Oversampling and Synthetic Minority Oversampling Technique (SMOTE) will be used for the first set of analyses.


The process above is demonstrated in cells 57-70 of **machine_learning.ipynb**. 

- Balancing Data and Machine learning Results

**The results for Logistic Regression, Decision Tree, Random Forest and Gradient Boosted Tree for both oversampling techniques are shown in the tables below.**


<p align="center">
<image src ="https://user-images.githubusercontent.com/82583576/134831147-7a95eec3-30c8-4b99-932a-509092693c60.PNG" width="750">
</p>


 
**Undersampling models yielded the following results:**

### Limitations and benefits

 
<p align="center">
<image src = "https://user-images.githubusercontent.com/82583576/134831301-a482eff4-802b-4fec-979c-27827fe5ed07.PNG" width="750">
</p>

 
**Combination Sampling using SMOTEENN provided the following results when used on the same dataset.** 

 
<p align="center">
<image src = "https://user-images.githubusercontent.com/82583576/134831403-72731c6a-38d9-42bd-952b-666641d22a40.PNG" width="750">
</p>
 
 
 
**Interpreting the Machine Learning Results**

 The tables above have a multitude of variables for what is deemed as "Good Apllicants" and "Bad Applicants".
 
 The Bank has 2 risks to mitigate for losses from its credit card applicants:

 1. Loss by approving "bad" applicants - known as Type I error. 
 
 2. Loss by deying "good" applicants - known as Type II error.
 
 From the tables above, the Random Forest method under both the Random Oversampling and SMOTE techniques yielded the best results to help achieve the banks risks mitigation goals.
 ***NEED TO PROVIDE MORE EXPLANATIONS WITH REGARDS TO ACCURACY PRECISION RECALL F1 SCORE
 
 

>[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)

## 6. Database

The database for this project is a PostgreSQL database. The database is created through pgAdmin and the structure and connections of the tables can be demonstrated in the PostGresDB_Draft.txt from the **PostgreSQL_Database folder.** 

The machine learning model will be connected as shown in the demo.ipynb file from the **machine_learning** folder.

The ERD diagram for our provisional database is also provided in the PostGreSQL_Database folder.

<p align="center">

<image src="https://user-images.githubusercontent.com/82583576/132156481-105fea27-3ee5-4101-9a4b-e21047c3fdbc.png" width="600">

</p>
 
 >[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)
 
 ## 7. Technologies

<p align="center">

<image src= "https://user-images.githubusercontent.com/82583576/134785783-062206f6-bde2-4ec5-bd60-02b30856716a.png" width="800" height="500">

</p>

As illustrated above, Python in combination with multiple librairies and tools were used for the project.
 
**Data Cleaning and Analysis**
Pandas and NumPy libraries in Jupyter notebook was used to clean data and perform exploratory analysis. 

**Database**
PostgreSQL was used to create the database tables and AWS RDS used for data storage.

**Machine Learning**
Scikit-learn was the machine learning library used to create the Oversampling and Undersampling models. 

**Visualization** 
Seaborn SNS is the library used to create graphics for the Confusion Matrices.
Matplotlib is used for all other charts within the project.
 
**Presentation and Dashboard**
Google Slides have been used to walk the client through the methodologies used, the findings from the data set amd commentaries about how the machine learning model will help the bank with its credit card application approval process.
 
A dashboard using JavaScript, HTML and CSS have been used for a live demonstration of the project's findings.
Flask and Pickle have also been used to demonstrate the interactivity of the model. The Pickle module has been used to enable applicants to input data in the model and have an instantaneous reply with regards to the application's status.
 
The dashboard is hosted on GitHub Pages.
 
## 8. Dashboard Description

Tools: JavaScript, HTML
 
Interactive Features : 
 
- Age
- Education
- Occupation
- Net income
- Number of children
 -Number of car

> Dashboard Display [click here](https://summerginger.github.io/DataSweeper_Project/)

 
## 9. Result of the Analysis
      ***TBA***

## 10. Recommendations

  ***TBA***
 - Better qualifying questions
 - Questions on applications must drive more detailed or focused answers
 - Acquisition of better quality data from the credit bureau to build a more performing model


### GITHUB Individual Branches

While there are many criteria that may disprove our customer’s credit card applications, however, we should retain all our client’s information and continue to adapt machine learning techniques to direct them to have other cards, such as cash cards, points reward cards etc. for the benefit of the growing business. 
 
>[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)
 
## 11. Team

Each team member's brnch has been named as follows: "First_name_DeliverableN", where N stands for the deliverable number. Example for the first deliverable, "Binoy_Deliverable1"
 
- Binoy Luckoo's Branch Name:  Binoy_DeliverableN 
- Samir Rifi's Branch Name:  samir_DeliverableN
- Jane Huang's Branch Name: jane_DeliverableN
- Lucas Chandra's Branch Name: lucas_DeliverableN

## 12. Citations
* [Kaggle Link](https://www.kaggle.com/rikdifos/credit-card-approval-prediction/code)

* [github markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)

<p align="center"> 
<img src="https://user-images.githubusercontent.com/82733723/133947489-cf784a14-c88c-4e3b-8e86-5fb6fc5e599e.png" width="600" height="300">
</p>

>[Back_to_top](https://github.com/summerginger/DataSweeper_Project#credit-card-approval-prediction)
