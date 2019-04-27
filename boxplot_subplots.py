
#Boxplot: Subplot for each attribute/species

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read csv file
iris = pd.read_csv('iris.csv')

#Plot grid 
plt.style.use('ggplot')
#Generate a boxplot for each attributes, illustrating the 3 species. ie. Four plots each with 3 species visible for comparison.
plt.subplot(2,2,1)
sns.boxplot(x="Species", y="SepalLengthCm", data=iris)
plt.subplot(2,2,2)
sns.boxplot(x="Species", y="SepalWidthCm", data=iris)
plt.subplot(2,2,3)
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
plt.subplot(2,2,4)
sns.boxplot(x="Species", y="PetalWidthCm", data=iris)

#Show plot.
plt.show()
