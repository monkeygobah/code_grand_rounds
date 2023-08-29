#ggplot 2 and tidyverse are packages for creating grpahical representations 
#of data in R. 
library(tidyverse)
library(ggplot2)
library(readxl)

#To load a built-in dataset in base R. Iris is one such dataset.
View(iris)


#ggplot2 is a versatile package that can be used to visualize data in various
#ways. As such, there are different ways to code one plot. We will call our 
#dataset using ggplot() and add on different functions to obtain different plots.

#Scatterplot - Arguments of ggplot are the dataset and a function aes(). aes takes
#the continuous variables you wish to examine in a scatterplot. geom_point() is a 
#function that is necessary for the scatterplot and takes certain arguments, as we will see later.
plot <- ggplot(iris, aes(x = Sepal.Length, Petal.Length)) + geom_point()
print(plot)

#Change visual parameters of points using geom_point().
plot <- ggplot(iris, aes(x = Sepal.Length, Petal.Length)) + geom_point(size = 4, shape = 20)
print(plot)

#Add in titles for axes and the overall plot. Make sure to put "+" at the end of 
#each line, not the beginning, at that triggers an error.
plot <- ggplot(iris, aes(x = Sepal.Length, Petal.Length)) + geom_point() +
  labs(x = "Sepal Length", y = "Petal Length", title = "Scatterplot")
print(plot)

#Now, let's look at plotting a histogram for one variable, which we specify using aes().
#geom_histogram generates the histogram. Binwidth specifies the resolution of your plot
#fill and color specify the color you wish your bars to be filled and outlined with, respectively.
histogram <- ggplot(iris, aes(x = Sepal.Length)) + 
  geom_histogram(binwidth = 1, fill = "lightblue", color = "black") +  
    labs(x = "Sepal Length", y = "Frequency", title = "Histogram") 
print(histogram)

#Let's try visualizing a boxplot on a continuous variable stratified by 
#a categorical one. 
boxplot<- ggplot(iris, aes(x = Sepal.Length, y = Species)) + 
  geom_boxplot(fill = "lightblue", color = "black") + 
  labs(x = "Sepal Length", y = "Species", title = "Boxplot of Sepal Length by Species") 
print(boxplot)

#We can visualize the boxplot a different way and specify stratification using aes() 
#and color.
boxplot<- ggplot(iris, aes(x = Sepal.Length)) + 
  geom_boxplot(aes(color = Species)) + 
  labs(x = "Sepal Length", title = "Boxplot of Sepal Length by Species") 
print(boxplot)


#Let's graph the same data that we used for the boxplot in a barchart.
barchart <- ggplot(iris, aes(x=Species, y = Sepal.Length)) + 
  geom_bar(stat = "identity", fill = "lightblue") +
  labs(x = "Species", y = "Sepal Length" , title = "Barchart") 
print(barchart)
