
#Linear Regression in Iris Dataset

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = pd.read_csv('iris.csv')

#seaborn lmplot to illustrate linear regression
sns.lmplot(x = "SepalLengthCm", y = "SepalWidthCm",col='species', hue='Species', data=iris)
#Show plot
plt.show()

