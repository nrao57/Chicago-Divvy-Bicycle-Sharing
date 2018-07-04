#this code is to just explore the dataset with basic panda tools
import pandas as pd
import numpy as np
import os

data_columns = ['trip_id', 'year', 'month', 
		'week', 'day', 'hour', 
		'usertype', 'gender','starttime',
		 'stoptime', 'tripduration', 'temperature',
		 'events','from_station_id', 'from_station_name', 
		'latitude_start','longitude_start', 'dpcapacity_start', 
		'to_station_id','to_station_name', 'latitude_end', 
		'longitude_end', 'dpcapacity_end'] 

#lets set the directory path where all the data is located
data_dir = '/Users/nikhil/Desktop/ChicagoBikeSharing/chicago-divvy-bicycle-sharing-data'
data_filename = "data.csv" 

#Create an Iterator from the data
data_set = pd.read_csv(data_dir+'/'+data_filename, chunksize=100000)

#calculate total number of rows of data
def calc_totalrows():
	row_len_map = map(lambda x: x.shape[0], data_set)
	row_len_list = list(row_len_map)
	total_rows = sum(row_len_list) #returns 9495235
 

#get dataframe of a random sample of all data 
def get_subset(data_set):
	data_reduced = pd.DataFrame()
	for chunk in data_set:
		data_reduced = pd.concat([data_reduced,chunk.sample(frac=0.001)])
	return data_reduced

data_randreduced = get_subset(data_set)

data_randreduced.to_csv('data_randreduced.csv')




