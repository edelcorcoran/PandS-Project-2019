
#Pivot Table to summarise the mean/average values for the four attributes of the dataset.
#Ref/Adapted from: https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/notebook

#Import Libraries
import pandas as pd
import numpy as np

#Load the dataset
iris = pd.read_csv('iris.csv')
iris.head(10)

#Create Pivot Table with 'Mean' showing average value for attributes (petallength, petalwidth, sepallength, sepalwidth) and 'Len' displaying count number
#Index set as 'Species', Values set as four attributes and 'aggfun' calculates average value for each attribute per species based on number of observations   
data = pd.pivot_table(iris,index=["Species"],values=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"],aggfunc=[np.mean,len])

#Print Pivot Table
print(data)

