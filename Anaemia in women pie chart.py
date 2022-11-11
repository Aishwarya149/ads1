# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 23:45:33 2022

@author: aishw
"""
#import all necessary libraries and packages
import pandas as pd
import matplotlib.pyplot as plt

#read file into dataframe and print
df = pd.read_excel("qwerty.xlsx")
q = df.groupby("Continent", as_index=False).sum()
print(q)

#storing the Values in another variable and print
value = q["Values"]
print(q)

# set labels and show the legend
labels = ['Africa', 'Americas', 'Eastern Mediterranean', 'Europe', 'South-East Asia', 'Western Pacific']
#Pie chart
plt.figure()
plt.pie(value, labels=labels, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.legend(loc='best')
plt.title('Prevalence of anaemia in women of reproductive age (aged 15-49)')
# saving the visualised data in a png format
plt.savefig('Prevalence of anaemia in women of reproductive age (aged 15-49).png')
# to show the visualisation of given data
plt.show()

"""
Data taken from the below link:
https://www.who.int/data/gho/data/indicators/indicator-details/GHO/prevalence-of-anaemia-in-women-of-reproductive-age-(-)
"""