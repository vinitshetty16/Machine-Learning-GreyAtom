# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here
#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()
#Plotting bar plot
#loan_status.plot(kind='bar')
# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
#property_and_loan.plot(kind='bar',stacked=False,figsize=(14,8))
#Changing the x-axis label
plt.xlabel("Property Area")

#Changing the y-axis label
plt.ylabel("Loan Status")

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(14,8))
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate']
#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate']
#Plotting density plot for 'Graduate'
graduate.plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate.plot(kind='density',label='Not Graduate')

#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(20,20))

#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)

#Setting the subplot axis title
ax_1.set_title("Applicant Income")

#Plotting scatter plot
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)

#Setting the subplot axis title
ax_2.set_title("Coapplicant Income")

#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome']+ data['CoapplicantIncome']

#Plotting scatter plot
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)

#Setting the subplot axis title
ax_3.set_title("Total Income")


