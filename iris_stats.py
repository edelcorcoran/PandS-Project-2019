
#Some summary statistics of the dataset including Min/Max/Mean/Standard Deviation and also the 25th, 50th, and 75th percentiles

#Ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html?highlight=dataset%20describe


#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import iris.csv file to use
data = ("iris.csv")

#use panda to read file and specify header
iris = pd.read_csv(data, header=0)

#Print Summary Statistics
print(iris.describe())

