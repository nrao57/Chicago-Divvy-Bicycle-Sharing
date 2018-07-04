from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim


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