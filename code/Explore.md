
# This Script Explores the Popularity of Chicago Bike Sharing Routes and Weather effects on Trip Times

We are going to look at the Chicago Bike Sharing Data from this [kaggle dataset](https://www.kaggle.com/yingwurenjian/chicago-divvy-bicycle-sharing-data)

Author: Nikhil Rao

GitHub: [https://github.com/nrao57](https://github.com/nrao57)

LinkedIn: [link](www.linkedin.com/in/nikhil-rao-54566862)

# Table of contents
1. [Introduction](#introduction)
2. [Import the Neccessary Libraries](#Libraries)
3. [Import the Dataset](#ImportData)
4. [Popularity of Bike Routes](#Popularity)
5. [Does bad weather slow bike riders?](#weather)

## Import the Neccessary Libraries <a name="Libraries"></a>


```python
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from scipy.stats import ttest_ind
%matplotlib inline
```

## Import the Dataset <a name="ImportData"></a>


```python
os.chdir("..")
data_set = pd.read_csv("Datasets/data.csv")
os.chdir('code')
```

What does the dataset look like?


```python
data_set.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>trip_id</th>
      <th>year</th>
      <th>month</th>
      <th>week</th>
      <th>day</th>
      <th>hour</th>
      <th>usertype</th>
      <th>gender</th>
      <th>starttime</th>
      <th>stoptime</th>
      <th>...</th>
      <th>from_station_id</th>
      <th>from_station_name</th>
      <th>latitude_start</th>
      <th>longitude_start</th>
      <th>dpcapacity_start</th>
      <th>to_station_id</th>
      <th>to_station_name</th>
      <th>latitude_end</th>
      <th>longitude_end</th>
      <th>dpcapacity_end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2355134</td>
      <td>2014</td>
      <td>6</td>
      <td>27</td>
      <td>0</td>
      <td>23</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>2014-06-30 23:57:00</td>
      <td>2014-07-01 00:07:00</td>
      <td>...</td>
      <td>131</td>
      <td>Lincoln Ave &amp; Belmont Ave</td>
      <td>41.939365</td>
      <td>-87.668385</td>
      <td>15.0</td>
      <td>303</td>
      <td>Broadway &amp; Cornelia Ave</td>
      <td>41.945512</td>
      <td>-87.645980</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2355133</td>
      <td>2014</td>
      <td>6</td>
      <td>27</td>
      <td>0</td>
      <td>23</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>2014-06-30 23:56:00</td>
      <td>2014-07-01 00:00:00</td>
      <td>...</td>
      <td>282</td>
      <td>Halsted St &amp; Maxwell St</td>
      <td>41.864580</td>
      <td>-87.646930</td>
      <td>15.0</td>
      <td>22</td>
      <td>May St &amp; Taylor St</td>
      <td>41.869482</td>
      <td>-87.655486</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2355130</td>
      <td>2014</td>
      <td>6</td>
      <td>27</td>
      <td>0</td>
      <td>23</td>
      <td>Subscriber</td>
      <td>Male</td>
      <td>2014-06-30 23:33:00</td>
      <td>2014-06-30 23:35:00</td>
      <td>...</td>
      <td>327</td>
      <td>Sheffield Ave &amp; Webster Ave</td>
      <td>41.921687</td>
      <td>-87.653714</td>
      <td>19.0</td>
      <td>225</td>
      <td>Halsted St &amp; Dickens Ave</td>
      <td>41.919936</td>
      <td>-87.648830</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2355129</td>
      <td>2014</td>
      <td>6</td>
      <td>27</td>
      <td>0</td>
      <td>23</td>
      <td>Subscriber</td>
      <td>Female</td>
      <td>2014-06-30 23:26:00</td>
      <td>2014-07-01 00:24:00</td>
      <td>...</td>
      <td>134</td>
      <td>Peoria St &amp; Jackson Blvd</td>
      <td>41.877749</td>
      <td>-87.649633</td>
      <td>19.0</td>
      <td>194</td>
      <td>State St &amp; Wacker Dr</td>
      <td>41.887155</td>
      <td>-87.627750</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2355128</td>
      <td>2014</td>
      <td>6</td>
      <td>27</td>
      <td>0</td>
      <td>23</td>
      <td>Subscriber</td>
      <td>Female</td>
      <td>2014-06-30 23:16:00</td>
      <td>2014-06-30 23:26:00</td>
      <td>...</td>
      <td>320</td>
      <td>Loomis St &amp; Lexington St</td>
      <td>41.872187</td>
      <td>-87.661501</td>
      <td>15.0</td>
      <td>134</td>
      <td>Peoria St &amp; Jackson Blvd</td>
      <td>41.877749</td>
      <td>-87.649633</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>



What are the columns?


```python
data_set.columns
```




    Index(['trip_id', 'year', 'month', 'week', 'day', 'hour', 'usertype', 'gender',
           'starttime', 'stoptime', 'tripduration', 'temperature', 'events',
           'from_station_id', 'from_station_name', 'latitude_start',
           'longitude_start', 'dpcapacity_start', 'to_station_id',
           'to_station_name', 'latitude_end', 'longitude_end', 'dpcapacity_end'],
          dtype='object')



## Lets look at the popularity of certain bike routes <a name="Popularity"></a>


```python
from_station="from_station_name"
to_station="to_station_name"
f1, ax1 = plt.subplots(1)
cross_table = pd.crosstab(data_set[from_station], data_set[to_station], normalize=False)
ax1.matshow(cross_table)
plt.show()
```


![png](output_11_0.png)


As you can see, there are certain bright spots in the heatmap visual, which indicates that some paths are more popular than others

### What is the most popular destination?


```python
cross_table.sum().sort_values(ascending=False).head(4)
```




    to_station_name
    Clinton St & Washington Blvd    161152
    Canal St & Adams St             139654
    Canal St & Madison St           129632
    Clinton St & Madison St         117378
    dtype: int64



#### From the data, it seems that the most popular destinations are 
1. Clinton St & Washington Blvd    
2. Canal St & Adams St             
3. Canal St & Madison St           
4. Clinton St & Madison St

### What are the most popular routes?


```python
top_to=cross_table.max().sort_values(ascending=False).head(4).index.values
most_pop = []
for top in top_to:
    most_pop.append([cross_table[top].sort_values(ascending=False).head(1).index.values[0], top])
most_pop
```




    [['Columbus Dr & Randolph St', 'Clinton St & Washington Blvd'],
     ['Southport Ave & Wellington Ave', 'Sheffield Ave & Wellington Ave'],
     ['LaSalle St & Jackson Blvd', 'Canal St & Madison St'],
     ['Canal St & Madison St', 'Michigan Ave & Washington St']]



#### From the data, the most popular routes are
1. From Columbus Dr & Randolph St to Clinton St & Washington Blvd
2. From Southport Ave & Wellington Ave to Sheffield Ave & Wellington Ave
3. From LaSalle St & Jackson Blvd to Canal St & Madison St
4. From Canal St & Madison St to Michigan Ave & Washington St

#### Does this make sense to all of my Chicagoans out there?

## Does bad weather reduce the time of bike trips around the city?<a name="weather"></a>

### Lets take a look at the value counts to see the distribution of weather


```python
data_set['events'].value_counts()/sum(data_set['events'].value_counts())
```




    cloudy          0.884496
    clear           0.053903
    rain or snow    0.045505
    not clear       0.009285
    tstorms         0.006755
    unknown         0.000056
    Name: events, dtype: float64



Based on the data, the majority of the time (88% to be exact) is cloudy. Then, the rest of the days are mostly clear or raining/snowing 

Lets combine "cloudy" and "clear" weather into one category called "clear". After all, cloudy does not mean there is precipitation. While we are at it, lets combine rain or snow, not clear, and tstorms into a category called "bad".


```python
data_set.loc[data_set['events']=='cloudy','events']='clear'
data_set.loc[data_set['events']=='rain or snow','events']='bad'
data_set.loc[data_set['events']=='not clear','events']='bad'
data_set.loc[data_set['events']=='tstorms','events']='bad'
data_set = data_set[data_set['events']!='unknown']
```


```python
data_set['tripduration'].describe()
```




    count    9.494699e+06
    mean     1.144687e+01
    std      7.206053e+00
    min      2.000000e+00
    25%      6.033333e+00
    50%      9.633333e+00
    75%      1.520000e+01
    max      6.000000e+01
    Name: tripduration, dtype: float64



** Note: The trip time is in units of minutes **

From the data, the average bike ride takes around 12 minutes and the longest rides take an hour

### Pivot tables to find the mean and standard deviation for the weather groups

There is a problem with just doing a t-test on the weather and their corresponding trip durations. What if, for some reason, cloudy days have more of one specific route than another (route being defined as from one station to another)? Then, those specific routes might be naturally longer, no matter the weather. Therefore, we must conduct a t-test for all of the routes, which is approximately the number of stations squared or 656 squared!!!! 

However, if we can show that each weather (clear or bad) contains the same set of routes, then we can just do a t-test on the entire set (it will not be correct, but an aproximation). To determine this justification, we can look at all of the routes for each weather and compare the length of the set of their tuples


```python
routes = data_set[['events',to_station, from_station]]
```


```python
clear_routes=routes[routes['events']=='clear']
#len(set(cloudy_routes[to_station].values,cloudy_routes[from_station])))
unique_clear_routes = len(set(list(zip(*[clear_routes[c].values.tolist() for c in [to_station, from_station]]))))
print('The number of unique clear routes: {}'.format(unique_clear_routes))
```

    The number of unique clear routes: 129367
    


```python
bad_routes=routes[routes['events']=='bad']
#len(set(cloudy_routes[to_station].values,cloudy_routes[from_station])))
unique_bad_routes = len(set(list(zip(*[bad_routes[c].values.tolist() for c in [to_station, from_station]]))))
print('The number of unique bad routes: {}'.format(unique_bad_routes))
```

    The number of unique bad routes: 63361
    

#### There are approximately twice as many unique routes for clear weather than bad weather. Therefore, we cannot legitimately compare the trip duration with a t-test. But lets do it anyway for practice  : ) <a name="wrongconclusion"></a>

Find the mean trip duration for each population of weather


```python
data_set[['events','tripduration']].groupby('events').mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tripduration</th>
    </tr>
    <tr>
      <th>events</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bad</th>
      <td>10.400526</td>
    </tr>
    <tr>
      <th>clear</th>
      <td>11.515496</td>
    </tr>
  </tbody>
</table>
</div>



Find the standard deviation for trip duration for each population of weather


```python
data_set[['events','tripduration']].groupby('events').std()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tripduration</th>
    </tr>
    <tr>
      <th>events</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bad</th>
      <td>6.595985</td>
    </tr>
    <tr>
      <th>clear</th>
      <td>7.238986</td>
    </tr>
  </tbody>
</table>
</div>



### Hypothesis Testing
Now that we have the mean and standard deviation for the weather, lets test the hypothesis with a t-test!

The null hypothesis will be that the **trip duration is equal for both clear and bad weather**


```python
pop1 = data_set[data_set['events']=='clear']['tripduration']
pop2 = data_set[data_set['events']=='bad']['tripduration']
ttest_ind(pop1, pop2, equal_var=False)
```




    Ttest_indResult(statistic=124.40031228827422, pvalue=0.0)



### Results and Key Takeaways

The p-value is 0.0009 which is waaaay lower than the typical p-value threshold of 0.05. Therefore, the probability of obtaining the data's difference of the average trip duration (11.47 seconds for clear weather - 10.52 seconds for bad weather = 0.95 seconds) given that the real difference is zero is 0.09%!

Due to this low probability, the trip durations are most likely different for clear and bad weather, with **trips taking longer on clear days!**

What?!?! How can this be? 

Maybe people in chicago take their time on sunny days to enjoy their ride or choose to ride a bike longer distances when it is a beautiful day.

#### [NOTE: As stated above, since clear weather has twice as many unique routes as bad weather, this result is meaningless. The clear weather could, and probably does, contain routes that are longer distances!](#wrongconclusion) 
