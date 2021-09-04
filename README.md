
# Topic : Credit Card Approval Prediction  <img align="right" src="https://user-images.githubusercontent.com/82733723/131945205-72772eea-1781-4977-ac31-f0f8327ed418.png">

## 1. Overview
The objective of this project is to help a financial institution to decide whether to issue a credit card to an applicant or not. Using personal information and data submitted by credit card applicants, the model will predict the probability of future defaults and credit card borrowings.

## Why we chose this topic? 
In today's fast-paced and high-tech world, credit scores can further impact many financial transactions, including personal loans, auto loans, mortgages, and credit cards. Credit scoring is a standard method of risk control in the financial industry. It uses the personal information and data submitted by credit card applicants to assess their creditworthiness. For protecting an individual's credit score, the financial sector owns a responsibility to control and objectively quantify the magnitude of risk and credit card issuance. As data analysts, we are most likely to handle this task, and we will apply new advanced learning machine algorithms to improve predictive power.

## Question
Based on the dataset, what are the standard requirements for an individual to be approved for a credit card?

## 2. Technologies

<p align="center">
<image src="https://user-images.githubusercontent.com/82583576/132108627-97f92b4f-57e3-495a-8665-37374aff7df6.PNG"
</p>




### 3. Machine Learning Model 
In the financial industry Credit Score cards have been used for a long time to determine the approval of loans. 



*This can even be a diagram that explains how it will work concurrently with the rest of the project steps.

## 4. Overview of dataset
 
The Dataset contains two files:
1. Demographics & application data - "application_record.csv" - this data has been provided by the applicants at the time of the credit card application. It contains demographic information including gender, car & real estate ownership, income level, education, occupation, marital status, contact information.
 
2. Credit Bureau data - "credit_record.csv" - data obtained from the credit bureau showing payment experience and the date of the last data extraction.  
 
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

### Data Cleaning and Preparation
 
 
 However, we will drop a few columns where consideration does not apply to the prediction. 
### 5. Result 
### 6. Summary
### 7. Recommendation

###
 
***Resources***
* [Kaggle Link](https://www.kaggle.com/rikdifos/credit-card-approval-prediction/code)

* [github markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)

***Team communication protocols***
 
This week, each team member will choose a shape, with each shape responsible for a specific task. The shapes to choose from are square, circle, triangle, and X. 
We will use whatsapp,slack,zoom meeting, Github project and [google docs](https://docs.google.com/document/d/1NugbKt5vuU91jPWE3nzVjTbBYoNdhf9_9ET2l-FNRmI/edit?usp=sharing) tools for communications.
 
![1st segment task assigned](https://user-images.githubusercontent.com/82733723/131895610-d1dd9b98-d97b-4531-8029-8e3862d66451.png) 
 



