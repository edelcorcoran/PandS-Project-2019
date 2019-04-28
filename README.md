
## <div align="center">Edel Corcoran ID#:G00010824</div>
## <div align="center">Higher Diploma in Data Analytics GMIT</div>
## <div align="center">Module: Progamming and Scripting 52445</div>
## <div align="center">PandS-Project-2019</div>
## <div align="center">Lecturer: Ian McLoughlin</div>


# <div align="center">Fisher's Iris Dataset</div>

## Intoduction


#### What Is It About?


In simple terms, the *Iris* is a plant and the *Iris Dataset* is a small study containing 150 observations and it's primary purpose is discriminating between three species of Iris from measurements of their petals and sepals. In the dataset four attributes of each plant were measured: sepal length, sepal width, petal length and petal width.

The Iris flower data set is a well-known data set example for data mining and data exploration, it's also often used to demonstrate simple machine learning techniques. 

*Ronald Fisher* a renowned biologist and statistician selected the *Iris Dataset* to illustrate the techniques described in his 1936 paper *The Use of Multiple Measurements in Taxonomic Problems* on discriminant analysis. It is a multivariate dataset and Fisher used it in the development of his linear discriminate model which distinguishes the species from each other. 




<p align="center">Iris Setosa<p align="center">
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/Images/Iris_setosa.jpg">
</p>

<p align="center">Iris Virginica<p align="center">
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/Images/Iris_virginica.jpg">
</p>

<p align="center">Iris Versicolor<p align="center">
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/Images/Iris_versicolor.jpg">
</p>

For those that are not green fingered and to avoid any confusion going forward, the image below gives a simple visual to help understand the various parts of a flower/plant and petal and sepal are clearly labelled. 

<p align="center">Petal vs Sepal<p align="center">
<p align="center"><img src="https://cdn-images-1.medium.com/max/1200/1*HPHOq7k53J4p1QY9ODf47g.gif">
</p>

#### How It Was Collected?

The dataset examines three species of Iris: Iris Setosa, Iris Virginica and Irish Versicolor. The dataset is a compilations of 150 records, there is 50 samples of each species which were used to measure specific features including the length and width of the sepals and petals. 


## Sir Ronald Aylmer Fisher

<p align="center">Sir Ronald Aylmer Fisher (1890-1962)<p align="center">
  
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/Images/SirRonaldFisher.JPG">
</p>

In 1890 Sir Ronald Aylmer Fisher was born into a wealthy family in London, England. At the age of 19 he entered the University of Cambridge as a student where he studied mathematics before persuing the study of physics at postgraduate level which including studying the theory of errors, a topic which heightened his interest in statistics. After college he worked for a time as a statistician in the Mercantile and General Investment Company in London al well as becoming a teacher of mathematics and physics. 

In 1917, Fisher married Ruth Guinness. They had two sons and seven daughters, one of whom died in infancy.

In 1919 following a short teaching career Fisher was offered and accepted the post of statistician at an agricultural research institute called the 'Rothamsted Agricultural Experiment Station'. 

Throughout Fisher lifetime he invented experimental design and was one of the principal founders of population genetics. He introduced the term variance and proposed its formal analysis. At Rothamsted, Fisher analysed crop data recorded over many years which led to his first application of the analysis of variance 'ANOVA'. In 1924 Fisher created the 'F distribution' , he later introduced the concept of 'null hypothesis'.

During his lifetime Fisher published 7 books and almost 400 academic research papers in the fields of statistics and genetics. He is considered by many to be the father of modern statistics given the enormous and profound contribution he made to the field of statistics through his work and research studies. 

Amongst his many other achievements Fisher was in 1933 appointed Professor of Eugenics at University College London. In 1943 he was appointed to the Balfour Chair of Genetics at the University of Cambridge. In 1952 Fisher was knighted by Queen Elizabeth, becoming Sir Ronald Aylmer Fisher.He was also the recipient of several honorary degrees from universities including Harvard (1936), University of Calcutta (1938), University of London (1946), University of Glasgow (1947), University of Adelaide (1959), University of Leeds (1961), and the Indian Statistical Institute (1962). 

In 1962 at the age of 72 Sir Ronald Fisher died in Adelaide Australia, he suffered from colon cancer. [1,2,3]

Some additional information on the dataset:



## How To Use The Python Code

The Iris Dataset is available to view by running the file named 'iris_dataset.py'. All the columns and rows within the dataset with numerical values in cms are visible.

Software Downloads:

[Python](https://www.python.org/downloads/) via [Anaconda](https://www.anaconda.com/distribution/#download-section) version 3.7

[Visual Studio Code](https://code.visualstudio.com/)

Libraries imported in code scripts:

Links below for further information
- [Numpy as np](https://www.numpy.org/)
- [Pandas as pd](https://pandas.pydata.org/)
- [Matplotlib as plt](https://matplotlib.org/) 
- [Seaborn as sns](https://seaborn.pydata.org/)



## My Work

 What it's about/My aims

What do I want to learn from project



**Tools Used to Analyses Dataset**:
- Dataset Describe/View
- Statistics Overview
- Pivot Table 
- Correlation Matrix
- Boxplots
- Linear Regression

**View the Dataset**

In order to get a clear overview and understanding of the data involved I started by downloading a copy of of the Iris Dataset and used the pandas library to view the data:

**File:** 'iris_dataset.py'

**Python Code:** 

- import pandas as pd
- data = pd.read_csv('iris.csv') 
- print(data)

Below is a screenshot of the first ten rows of the output. You can clearly see the columns with the four attributes with numerical values in cms (Petal Length, Petal Width, Sepal Length and Sepal Width) and a column outlining the species (Setosa/Virginica/Versicolor). 

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/irisdataset.png">
</p>

**Statistics Overview**

I gathered some basic statistics and distributions by running the 'describe' code, this gave a brief summary of the mean, maximum, minimum, standard diviation and percentiles (25%/50%/75%) of the four attributes in the dataset.

**File:** 'iris_stats.py'

**Python Code:** 

- import pandas as pd
- data = ("iris.csv")
- iris = pd.read_csv(data, header=0)
- print(iris.describe())

There is a screenshot of the output of the python script below which illustrates the summary statistics of the dataset.

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/irisstats.png">
</p>

**Pivot Table**

Whilst the 'describe' code outlined basic statistics like mean/min/max for each attribute in the dataset, these statistics aren't broken down by species. A pivot table plot generated using the pandas library helps give better statistics by breaking the statistics into the various species ie. it's possible to view the mean of each attribute by species. 

For example the mean sepal length for the dataset is 5.84333cms, but the pivot table outlines that the actual mean sepal length for Setosa is 1.464cm, for Versicolor it's 4.26cms and for Virginica it's 5.552cms. You can view mean values for each attribute by species in the screenshot below, this help's to better understand the differences between the species.

**File:** 'pivot_table.py'

**Python Code:**

- iris.head(10)
- data = pd.pivot_table(iris,index=["Species"],values=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"],aggfunc=[np.mean,len])

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/pivottable.png">
</p>

**Linear Regression**

The seaborn library was imported to generate the 'lmplot', the linear line across our plot is the best fit for the trend of the sepal width with respect to the sepal length. There are two images firstly you see the linear regression for each species the Setosa (blue), Versicolor(orange) and Virginoca (green), the second image plots all three species on the same grid which help visualise the difference/similarity between the various species. Similar code and logic were used to generate the petal lenght/width linear regression images.

**Files:** 'linear_regression.py' / 'linear_regression_species.py'

**Python Code:**

- iris = pd.read_csv('iris.csv') 
- sns.lmplot(x = "SepalLengthCm", y = "SepalWidthCm", hue='Species', data=iris)

and also:

- sns.lmplot(x = "SepalLengthCm", y = "SepalWidthCm",col='species', hue='Species', data=iris)


<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression_species.png">
</p>

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression.png">
</p>

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression_petal_species.png">
</p>

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression_petal.png">
</p>

**Boxplots**

Again several libraries were imported to create boxplots for the dataset as well as subplots which help visualise the differences and similaries between the species. Similarly to the linear regression images, here I have looked at the attributes for the dataset before breaking the data down into the individual species in order to visualise the similarities and differences.

**Files:** 'boxplot.py' and 'boxplot_subplots.py' 

**Python Code:**

-iris = pd.read_csv('iris.csv')
-sns.set()
-iris.boxplot()
-plt.title('Iris Dataset Boxplot')
-plt.ylabel('Length in CM')

Also for subplots:

- plt.style.use('ggplot')
- plt.subplot(2,2,1)
- sns.boxplot(x="Species", y="SepalLengthCm", data=iris)
- plt.subplot(2,2,2)
- sns.boxplot(x="Species", y="SepalWidthCm", data=iris)
- plt.subplot(2,2,3)
- sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
- plt.subplot(2,2,4)
- sns.boxplot(x="Species", y="PetalWidthCm", data=iris)

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/boxplot.png">
</p>

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/boxplot_subplots.png">
</p>

**Correlation Matrix**

A correlation matrix was generated to help analyse which if any of the attributes in the dataset correlate to each other. A scale is visible to the right of the image, this gives an understanding of how the matrix works. The closer the numerical value in a cell is to 1 the higher the correlation between the attributes connected to that cell. ie. it's clear there is a high correlation between petal width and petal length as the numerical values in those cells is 0.96.

**Files:** 'correlation_matrix.py'

**Python Code:**

- corr = iris.corr()
- plt.figure(figsize=(10,8)) 
- ax = plt.axes()
- sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values,cmap='plasma', annot=True)
- ax.set_title('Correlation Matrix')

<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/correlation_matrix.png">
</p>

## Summary



## References/Bibliography

1. https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html viewed 16/4/19
2. https://www.famousscientists.org/ronald-fisher/ viewed 17/04/19
3. http://www-history.mcs.st-andrews.ac.uk/Biographies/Fisher.html viewed 17/4/19
4. [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) viewed 11/04/19
5. [Kaggle](https://www.kaggle.com/uciml/iris) vieweded 11/04/19 source for iris.csv file

Bibliography:

- [Numpy as np](https://www.numpy.org/)
- [Pandas as pd](https://pandas.pydata.org/)
- [Matplotlib as plt](https://matplotlib.org/) 
- [Seaborn as sns](https://seaborn.pydata.org/)

Image Sources:

- [Iris Setosa](https://en.wikipedia.org/wiki/Iris_setosa) accessed 12/04/19
- [Iris Virginica](https://en.wikipedia.org/wiki/Iris_virginica) accessed 12/04/19
- [Iris Versicolor](https://en.wikipedia.org/wiki/Iris_versicolor) accessed 12/04/19
- [Sir Ronald Fisher](https://en.wikipedia.org/wiki/File:Youngronaldfisher2.JPG) accessed 18/4/19
- [Petal vs Sepal](https://cdn-images-1.medium.com/max/1200/1*HPHOq7k53J4p1QY9ODf47g.gif) accessed 18/4/19

Code Sources:
- [Kaggle](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/notebook) accessed 30/3/19
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html?highlight=dataset%20describe) accessed 30/3/19

