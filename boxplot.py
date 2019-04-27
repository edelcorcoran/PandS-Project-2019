
#Boxplot Iris Dataset - looks at the 4 attributes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#read csv file
iris = pd.read_csv('iris.csv')

sns.set()
#Generates a Boxplot for each column [SL, SW, PL, PW)
iris.boxplot()
#Assign a title to the Boxplot 
plt.title('Iris Dataset Boxplot')
#Labels the Y-axis
plt.ylabel('Length in CM')
#Show plot.
plt.show()

