
## <div align="center">Edel Corcoran ID#:G00010824</div>
## <div align="center">Higher Diploma in Data Analytics GMIT</div>
## <div align="center">Module: Progamming and Scripting 52445</div>
## <div align="center">PandS-Project-2019</div>
## <div align="center">Lecturer: Ian McLoughlin</div>


# <div align="center">Fisher's Iris Dataset</div>

# Introduction

The primary focus of this project is to research the Iris Dataset, to use python scripts and plots to analyse, visualise and clarify whether there are any trends or patterns betweens the Iris species observed in the dataset. On a basis level I extracted statisical data from the dataset to help compare the various attributes of the three species to help identify similarities and differences. On a more complex level I utilised python scripts to generate plots and tables in regards to linear regression and correlation to determine whether any trends were evident. Fisher's wanted to create a linear discriminant model to distinguish the various Iris species, in this short project I hope to proof clear differences/similaries between the species and confirm whether any particular feature or attribute helps distinguish the various species apart.

# Project Layout

1. The Iris Dataset - Some background information on the dataset.
- What it's About?
- How it was Collected?
- Some additional infor on the dataset
2. Ronald Fisher - Information on the man and his work.
3. Python Code / Contents
- How to use the scripts/code
- Contents of the repository
4. My Investigations/Research
- Tools Used to Analyses Dataset
- Outline/Analyse each tool: Includes any plots/tables/graphs and code
5. Findings/Conclusion
- Statiistical Overview
- Tends/Patterns
6. References - including scources for images and code and bibliography.

# 1. The Iris Dataset

## What Is It About?

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

## How It Was Collected?

The dataset examines three species of Iris: Iris Setosa, Iris Virginica and Irish Versicolor. The dataset is a compilations of 150 records, there is 50 samples of each species which were used to measure specific features including the length and width of the sepals and petals. 

"It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"." []

**Some additional information on the dataset:**

- "The UCI Machine Learning Repository, which contains what is probably the “official” iris data set, lists over 200 papers referencing the iris data." [7]
- It's somestimes referred to as the 'Anderson's Iris dataset' as it was he who collected the data.
- It's a good dataset for predictive modeling & machine learning.

#2.Sir Ronald Aylmer Fisher

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

#3. How To Use The Python Code / Contents 

This repository contain my images and code scripts to the Iris Project for Module 52445.

Instructions on how to download:

Download and install the following programs:Anaconda, Visual Studio Code and CMDER command line. They will enable you to view and run the programs/code in the repository.

Go to my repository on GitHub: [Repository](https://github.com/edelcorcoran/PandS-Project-2019).
Once the repository is open click on the clone/download button.

Instrucions to Run:

- Open Cmder or Anaconda.
- Save the repositoy folder to your computer.
- Navigate to the directory/location where you have saved/unzipped my repository.
- In CMDER once you've navigated to the folder location, you can run ipython to run the code.
- On the command line select the script you want to open for example type "run" followed by the file name eg. "iris_dataset.py" and click enter/return on your keyboard to open.

Contents:
- Readme
- Images Folder - which holds photos obtained online which were saved in case any changes are made to the website which may have effected the photos if linked to the sites.
- iris.cvs 
- iris_dataset.py
- irisdataset.png
- iris_stats.py
- irisstats.png
- pivot_table.py
- pivottable.png
- boxplot.py
- boxplot.png
- boxplot_subplots.py
- boxplots_subplots.png
- correlation_matrix.py
- correlation_matrix.png
- linear_regression.py
- linear_regression.png
- linear_regression_species.py 
- linear_regression_species.png
- linear_regression_petal.py
- linear_regression_petal.png
- linear_regression_petal_species.py
- linear_regression_petal_species.png
- git

The images and python scripts are discussed in detail below and the images are screenshots of the output which you should get if you run the relevant script.

Software Downloads:

[Python](https://www.python.org/downloads/) via [Anaconda](https://www.anaconda.com/distribution/#download-section) version 3.7

[Visual Studio Code](https://code.visualstudio.com/)

Libraries imported in code scripts:

Links below for further information
- [Numpy as np](https://www.numpy.org/)
- [Pandas as pd](https://pandas.pydata.org/)
- [Matplotlib as plt](https://matplotlib.org/) 
- [Seaborn as sns](https://seaborn.pydata.org/)

The Iris Dataset is available to view by running the file named 'iris_dataset.py'. All the columns and rows within the dataset with numerical values in cms are visible.

#4.My Investigations/Research

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

<div align="center">Fig:1 Iris Dataset Overview</div>
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

<div align="center">Fig 2: Iris Statisical Overview</div>
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/irisstats.png">
</p>

**Pivot Table**

Whilst the 'describe' code outlined basic statistics like mean/min/max for each attribute in the dataset, these statistics aren't broken down by species. A pivot table plot generated using the pandas library helps give better statistics by breaking the statistics into the various species ie. it's possible to view the mean of each attribute by species. 

For example the mean sepal length for the dataset is 5.84333cms, but the pivot table outlines that the actual mean sepal length for Setosa is 1.464cm, for Versicolor it's 4.26cms and for Virginica it's 5.552cms. You can view mean values for each attribute by species in the screenshot below, this help's to better understand the differences between the species.

**File:** 'pivot_table.py'

**Python Code:**

- iris.head(10)
- data = pd.pivot_table(iris,index=["Species"],values=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"],aggfunc=[np.mean,len])

<div align="center">Fig 3: Pivot Table</div>
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

<div align="center">Fig 4: Linear Regression Sepal by Species</div>
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression_species.png">
</p>

<div align="center">Fig 5: Linear Regression Sepal Comparison</div>
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression.png">
</p>

<div align="center">Fig 6: Linear Regression Petal by Species</div>
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/linear_regression_petal_species.png">
</p>

<div align="center">Fig 7: Linear Regression Petal Comparison</div>
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


<div align="center">Fig 8: Boxplot Iris</div>
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/boxplot.png">
</p>

<div align="center">Fig 9: Boxplot by Species</div>
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

<div align="center">Fig 10: Correlation</div>
<p align="center"><img src="https://github.com/edelcorcoran/PandS-Project-2019/blob/master/correlation_matrix.png">
</p>

## Main Findings/Conclusions

Statistical Analysis:

The largest standard deviation in the dataset (iris_stats.py) was in the petal length attributes which means the findings/values were more spread out for this attribute. When you look at the various classifications the mean petal length for Setosa was 1.464 cms, it was 4.26 cm for Versicolor and 5.52 cms for Virginica (Fig.2). Clearly Virginica and Versicolor are more in line with each other and are separable from Setosa. If you reandomly selected one flower from that dataset, if it had a small petal length it's likely to be a Setosa iris. This attribute is clearly the best feature with which to distinguish the species apart.

As a whole looking at the statistical data it's evident that Virginica and Versicolor are similar with Setosa being separable from them. In three of the four attributes within the dataset the Virginica species had the largest mean value (Petal length, Petal Width and Sepal length), it's also evident that in those same three attributes Versicolor had the second largest mean. In all those attributes the Setosa species had a notibly smaller mean value which makes it detachable from the other species in the dateset. (Fig.3)

In the linear regression/distibution plots it's clear the distributions (dots) are more clustered for the Petal Length/Width plots (Fig.6/7) which indicates that the attributes are correlated. Likewise, it's clear from the same plots in regards to sepal length/width that these two attributes are not correlated as the distributions aren't clustered and are clearly more widespread with outliers. (Figs.4/5 )

Trends/Patterns:

It is fair to say that simply by inspecting some of the images contained in this project that it's clear that patterns/trends do exist within dataset. The linear regression lines for the petal length/width are more in line for the iris species than they are in the sepal length/width regression lines. It's evident also from the correcation matrix that the petal width/length are positively correlated give the output of 0.96 in the correction matrix in the respective cells. 

The graphs and tables contained in this project help to visualise and analysis the various species of iris, clear similarities and differences are evident between the three species. Further study and analysis could look deeper into predictive analysis and more algorithms to help proof the probable species of randomly selected particularly given that Fisher's main ambition with his linear discriminant model when working on the Iris dataset was to distinguish the species from each other.


## References/Bibliography

1. https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html viewed 16/4/19
2. https://www.famousscientists.org/ronald-fisher/ viewed 17/04/19
3. http://www-history.mcs.st-andrews.ac.uk/Biographies/Fisher.html viewed 17/4/19
4. [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) viewed 11/04/19
5. [Kaggle](https://www.kaggle.com/uciml/iris) vieweded 11/04/19 source for iris.csv file
6. [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set) viewed 27/4/19
7. [200 papers- iris uses](https://blog.revolutionanalytics.com/2014/08/the-iris-data-set-for-big-data.html)

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
- [Kaggle - Iris CSV](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/notebook) accessed 30/3/19
- [Pandas - Describe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html?highlight=dataset%20describe) accessed 30/3/19
- [Correlation Matrix](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/notebook)
- [Pivot Table](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis/notebook)