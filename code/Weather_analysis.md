
# Lets test the whether bad weather reduce the number people taking bike trips

## Import the Neccessary Libraries


```python
import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from scipy.stats import ttest_ind
%matplotlib inline
```

## Import the Dataset


```python
os.chdir("..")
data_set = pd.read_csv("Datasets/data.csv")
os.chdir('code')
```

## Lets take a look at the value counts to see the distribution of weather


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

## Pivot tables to find the mean and standard deviation for the weather groups


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



## Hypothesis Testing
Now that we have the mean and standard deviation for the weather, lets test the hypothesis with a t-test!

The null hypothesis will be that the **trip duration is equal for both clear and bad weather**


```python
pop1 = data_set[data_set['events']=='clear']['tripduration']
pop2 = data_set[data_set['events']=='bad']['tripduration']
ttest_ind(pop1, pop2, equal_var=False)
```




    Ttest_indResult(statistic=124.40031228827422, pvalue=0.0)



## Results and Key Takeaways

The p-value is 0.0009 which is waaaay lower than the typical p-value threshold of 0.05. Therefore, the probability of obtaining the data's difference of the average trip duration (11.47 seconds for clear weather - 10.52 seconds for bad weather = 0.95 seconds) given that the real difference is zero is 0.09%!

Due to this low probability, the trip durations are most likely different for clear and bad weather, with **trips taking longer on clear days!**

What?!?! How can this be? 

Maybe people in chicago take their time on sunny days to enjoy their ride or choose to ride a bike longer distances when it is a beautiful day.
