# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
data['Gender'].value_counts().plot(kind='bar')
data['Alignment'].value_counts().plot(kind='bar')

# Find mean of Combat, strength , Intelligence
meanX = data['Combat'].mean()
meanY = data['Strength'].mean()
meanZ = data['Intelligence'].mean()

subX = data.Combat - meanX
subY = data.Strength - meanY
subZ = data.Intelligence - meanZ

A = (subX*subY).sum()
B = ((subX ** 2).sum())*((subY ** 2).sum())**(1/2)

C = (subX*subZ).sum()
D = ((subX ** 2).sum())*((subZ ** 2).sum())**(1/2)

corr1= A/B
corr2= C/D
print(corr1)
print(corr2)

best = data['Total'].quantile(0.99)
Total = data[data['Total'] > best]
super_best_list = Total['Name']
super_best_names = super_best_list.values.tolist()
print(super_best_list)










# Code starts here



