#This script is to see if there are any correlations between
#the features and fields
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim


data_dir = "/Users/nikhil/Desktop/ChicagoBikeSharing/chicago-divvy-bicycle-sharing-data"
data_set = pd.read_csv(data_dir+"/data_randreduced.csv")
data_set = data_set.drop(['Unnamed: 0'], axis=1)

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

    
#plot longitudes and latitudes with line weights based on tripduration
#basemap git: https://github.com/matplotlib/basemap.git

def visualize(data, uplat=55, lowlat=20, leftlat=-135, rightlat=-60):
    data_gps = data_set_format[['latitude_start', 'longitude_start', 'latitude_end', 'longitude_end']]
    #get coordinates of city of chicago
    geolocator = Nominatim()
    loc = geolocator.geocode("Chicago") #get coordinates for chicago
    f1, ax1 = plt.subplots(1)
    lons_start, lats_start = data['longitude_start'].values, data['latitude_start'].values
    lons_stop, lats_stop = data['longitude_end'].values, data['latitude_end'].values
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # lat_ts is the latitude of true scale.
    # resolution = 'c' means use crude resolution coastlines.
    m = Basemap(projection='merc',
                llcrnrlat=lowlat,urcrnrlat=uplat,
                llcrnrlon=leftlat,urcrnrlon=rightlat,
                lat_ts=20,resolution='l')
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    #m.drawmapboundary(fill_color='aqua')
    x,y = m(lons_start,lats_start)
    m.scatter(x,y,marker='o')
    plt.title("Mercator Projection of Chicago Bike Sharing")
    plt.show()



#look at the weather

''' Hypothesis 

Bad weather affect tripduration
Highest biked paths have the most capacity
Most frequent have later starttimes and earlier stoptime
Most usertypes are not subscriptions
Most riders are during the summer
Riders have increased over the years

'''

