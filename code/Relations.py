#This script is to see if there are any correlations between
#the features and fields
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt

data_dir = "/Users/nikhil/Desktop/ChicagoBikeSharing/chicago-divvy-bicycle-sharing-data"
data_set = pd.read_csv(data_dir+"/data_randreduced.csv")

print("The shape of the dataset is {} rows and {} columns".format(data_set.shape[0], data_set.shape[1]))



#lets see if any of the features are correllated
correlation_matrix = data_set.corr()

#lets plot the matrix with a heatmap





