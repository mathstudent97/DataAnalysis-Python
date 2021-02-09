```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inLine
```

    Matplotlib is building the font cache; this may take a moment.
    


```python
import os
```


```python
# Ensure that you have the correct working directory.
# The file containing the data should be located within your current working directory.

#os.getcwd() -> This provides your current working directory.
#os.chdir('C:\\Users\\maullonv\\Desktop\\dataAnalysisPython') 
    #-> Use this to change your working directory if needed.
```


```python

```


```python
# Load Data

# read the csv file into Python

sales = pd.read_csv(
    'sales_data.csv',
    parse_dates=['Date'])
```


```python
# The data at a glance:
sales.head()
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
      <th>Date</th>
      <th>Day</th>
      <th>Month</th>
      <th>Year</th>
      <th>Customer_Age</th>
      <th>Age_Group</th>
      <th>Customer_Gender</th>
      <th>Country</th>
      <th>State</th>
      <th>Product_Category</th>
      <th>Sub_Category</th>
      <th>Product</th>
      <th>Order_Quantity</th>
      <th>Unit_Cost</th>
      <th>Unit_Price</th>
      <th>Profit</th>
      <th>Cost</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-11-26</td>
      <td>26</td>
      <td>November</td>
      <td>2013</td>
      <td>19</td>
      <td>Youth (&lt;25)</td>
      <td>M</td>
      <td>Canada</td>
      <td>British Columbia</td>
      <td>Accessories</td>
      <td>Bike Racks</td>
      <td>Hitch Rack - 4-Bike</td>
      <td>8</td>
      <td>45</td>
      <td>120</td>
      <td>590</td>
      <td>360</td>
      <td>950</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-11-26</td>
      <td>26</td>
      <td>November</td>
      <td>2015</td>
      <td>19</td>
      <td>Youth (&lt;25)</td>
      <td>M</td>
      <td>Canada</td>
      <td>British Columbia</td>
      <td>Accessories</td>
      <td>Bike Racks</td>
      <td>Hitch Rack - 4-Bike</td>
      <td>8</td>
      <td>45</td>
      <td>120</td>
      <td>590</td>
      <td>360</td>
      <td>950</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-03-23</td>
      <td>23</td>
      <td>March</td>
      <td>2014</td>
      <td>49</td>
      <td>Adults (35-64)</td>
      <td>M</td>
      <td>Australia</td>
      <td>New South Wales</td>
      <td>Accessories</td>
      <td>Bike Racks</td>
      <td>Hitch Rack - 4-Bike</td>
      <td>23</td>
      <td>45</td>
      <td>120</td>
      <td>1366</td>
      <td>1035</td>
      <td>2401</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-03-23</td>
      <td>23</td>
      <td>March</td>
      <td>2016</td>
      <td>49</td>
      <td>Adults (35-64)</td>
      <td>M</td>
      <td>Australia</td>
      <td>New South Wales</td>
      <td>Accessories</td>
      <td>Bike Racks</td>
      <td>Hitch Rack - 4-Bike</td>
      <td>20</td>
      <td>45</td>
      <td>120</td>
      <td>1188</td>
      <td>900</td>
      <td>2088</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-05-15</td>
      <td>15</td>
      <td>May</td>
      <td>2014</td>
      <td>47</td>
      <td>Adults (35-64)</td>
      <td>F</td>
      <td>Australia</td>
      <td>New South Wales</td>
      <td>Accessories</td>
      <td>Bike Racks</td>
      <td>Hitch Rack - 4-Bike</td>
      <td>4</td>
      <td>45</td>
      <td>120</td>
      <td>238</td>
      <td>180</td>
      <td>418</td>
    </tr>
  </tbody>
</table>
</div>




```python
sales.shape
# This gives number of rows & columns within the data.
# (#rows, #columns)
```




    (113036, 18)




```python
sales.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 113036 entries, 0 to 113035
    Data columns (total 18 columns):
     #   Column            Non-Null Count   Dtype         
    ---  ------            --------------   -----         
     0   Date              113036 non-null  datetime64[ns]
     1   Day               113036 non-null  int64         
     2   Month             113036 non-null  object        
     3   Year              113036 non-null  int64         
     4   Customer_Age      113036 non-null  int64         
     5   Age_Group         113036 non-null  object        
     6   Customer_Gender   113036 non-null  object        
     7   Country           113036 non-null  object        
     8   State             113036 non-null  object        
     9   Product_Category  113036 non-null  object        
     10  Sub_Category      113036 non-null  object        
     11  Product           113036 non-null  object        
     12  Order_Quantity    113036 non-null  int64         
     13  Unit_Cost         113036 non-null  int64         
     14  Unit_Price        113036 non-null  int64         
     15  Profit            113036 non-null  int64         
     16  Cost              113036 non-null  int64         
     17  Revenue           113036 non-null  int64         
    dtypes: datetime64[ns](1), int64(9), object(8)
    memory usage: 12.1+ MB
    


```python
sales.describe()
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
      <th>Day</th>
      <th>Year</th>
      <th>Customer_Age</th>
      <th>Order_Quantity</th>
      <th>Unit_Cost</th>
      <th>Unit_Price</th>
      <th>Profit</th>
      <th>Cost</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
      <td>113036.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>15.665753</td>
      <td>2014.401739</td>
      <td>35.919212</td>
      <td>11.901660</td>
      <td>267.296366</td>
      <td>452.938427</td>
      <td>285.051665</td>
      <td>469.318695</td>
      <td>754.370360</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.781567</td>
      <td>1.272510</td>
      <td>11.021936</td>
      <td>9.561857</td>
      <td>549.835483</td>
      <td>922.071219</td>
      <td>453.887443</td>
      <td>884.866118</td>
      <td>1309.094674</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>2011.000000</td>
      <td>17.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>-30.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.000000</td>
      <td>2013.000000</td>
      <td>28.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>5.000000</td>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>63.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>16.000000</td>
      <td>2014.000000</td>
      <td>35.000000</td>
      <td>10.000000</td>
      <td>9.000000</td>
      <td>24.000000</td>
      <td>101.000000</td>
      <td>108.000000</td>
      <td>223.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>23.000000</td>
      <td>2016.000000</td>
      <td>43.000000</td>
      <td>20.000000</td>
      <td>42.000000</td>
      <td>70.000000</td>
      <td>358.000000</td>
      <td>432.000000</td>
      <td>800.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>31.000000</td>
      <td>2016.000000</td>
      <td>87.000000</td>
      <td>32.000000</td>
      <td>2171.000000</td>
      <td>3578.000000</td>
      <td>15096.000000</td>
      <td>42978.000000</td>
      <td>58074.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
# Numerical Analysis and Visualization

sales['Unit_Cost'].describe()
```




    count    113036.000000
    mean        267.296366
    std         549.835483
    min           1.000000
    25%           2.000000
    50%           9.000000
    75%          42.000000
    max        2171.000000
    Name: Unit_Cost, dtype: float64




```python
sales['Unit_Cost'].mean()
```


```python
sales['Unit_Cost'].median()
```


```python
sales['Unit_Cost'].plot(kind = 'box', vert = False, figsize = (14, 6))
```


```python
sales['Unit_Cost'].plot(kind = 'density', figsize = (14, 6)) #kde
```


```python
ax = sales['Unit_Cost'].plot(kind = 'density', figsize = (14, 6)) #kde
ax.axvline(sales['Unit_Cost'].mean(), color = 'red')
ax.axvline(sales['Unit_Cost'].median(), color = 'green')
```


```python
ax = sales['Unit_Cost'], plot(kind = 'hist', figsize = (14, 6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')
```
