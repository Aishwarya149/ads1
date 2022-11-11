# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 08:59:37 2022

@author: aishw
"""
#import all necessary libraries and packages
import pandas as pd
import matplotlib.pyplot as plt

#read file into dataframe and print
df = pd.read_csv("pop.csv")
print(df)
NoOfColumns = len(df.columns)
# Use iloc to extract columns
x = df.iloc[:, 0]

#Line chart
for i in range(1, NoOfColumns-1):
    plt.plot(x, df.iloc[:, i], label="Line "+str(i))
# set labels and show the legend
plt.legend()
plt.title('population mid-year estimate')
plt.xlabel('Years')
plt.ylabel('Values')
# saving the visualised data in a png format
plt.savefig('Population estimates time series dataset line.png')
# to show the visualisation of given data
plt.show()



"""

https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatestimeseriesdataset
Title	Scotland population mid-year estimate	Great Britain population mid-year estimate	England population mid-year estimate	United Kingdom population mid-year estimate	England and Wales population mid-year estimate	Northern Ireland population mid-year estimate	Wales population mid-year estimate
CDID	SCPOP	GBPOP	ENPOP	UKPOP	EWPOP	NIPOP	WAPOP
"""