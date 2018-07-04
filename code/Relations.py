#This script is to see if there are any correlations between
#the features and fields
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt



os.chdir("..")
data_set = pd.read_csv("Datasets/data_randreduced.csv")


print("The shape of the dataset is {} rows and {} columns".format(data_set.shape[0], data_set.shape[1]))

#Gender
print(data_set['gender'].value_counts())


#lets see if any of the features are correlated
#first, lets map the strings to integer
data_set_format = pd.get_dummies(data_set, prefix='gender', columns=['gender'])
data_set_format = pd.get_dummies(data_set, prefix='gender', columns=['gender'])
data_set_format = pd.get_dummies(data_set, prefix='usertype', columns=['usertype'])
data_set_format = pd.get_dummies(data_set, prefix='events', columns=['events'])


from_station="from_station_name"
to_station="to_station_name"
f1, ax1 = plt.subplots(1)
cross_table = pd.crosstab(data_set[from_station], data_set[to_station], normalize=False)
ax1.matshow(cross_table)
plt.show()


#lets plot the absolute values of the matrix with a heatmap
def heat(data_set_format):
    correlation_matrix = data_set_format.corr()
    plt.matshow(correlation_matrix.abs(), cmap='plasma')
    plt.show()



''' Hypothesis Testing

Bad weather affect tripduration
Highest biked paths have the most capacity
Most frequent have later starttimes and earlier stoptime
Most usertypes are not subscriptions
Most riders are during the summer
Riders have increased over the years
More men ride bikes than women

'''

