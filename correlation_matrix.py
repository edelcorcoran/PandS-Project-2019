
# Correlation Matrix - This helps clarify whether or not there's any correlation between the various parameters in the dataset.
# It illustrates that the PL and PW have positive correlation.
#Ref: Adapted from: https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/notebook

# import libraries necessary
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read dataset csv file using pandas
iris = pd.read_csv("iris.csv")

#create correlation matrix using csv file
corr = iris.corr()
#plot fig size
plt.figure(figsize=(10,8)) 

ax = plt.axes()
#Generate Heatmap/ Allow annotations(numerical value for each cell)/ Colormap using one of the uniform sequential colourmaps (plasma)
sns.heatmap(corr, 
            #Apply xticks/yticks
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
           cmap='plasma', annot=True)
#Title for plot
ax.set_title('Correlation Matrix')
#Show plot
plt.show()


