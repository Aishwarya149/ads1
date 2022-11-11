# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:51:11 2022

@author: aishw
"""
#import all necessary libraries and packages
import pandas as pd
import matplotlib.pyplot as plt

#read file into dataframe and print
df = pd.read_csv("malaria.csv")
print(df)

#ploting the bar graph
plt.bar(df.ParentLocation,df.FactValueNumeric)
plt.legend()
plt.title('Estimated number of malaria cases')
# saving the visualised data in a png format
plt.savefig('Estimated number of malaria cases.png')
# to show the visualisation of given data
plt.show()
