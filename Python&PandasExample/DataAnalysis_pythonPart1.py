#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[27]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inLine')


# In[28]:


import os


# In[9]:


# Ensure that you have the correct working directory.
# The file containing the data should be located within your current working directory.

#os.getcwd() -> This provides your current working directory.
#os.chdir('C:\\Users\\maullonv\\Desktop\\dataAnalysisPython') 
    #-> Use this to change your working directory if needed.


# In[ ]:





# In[29]:


# Load Data

# read the csv file into Python

sales = pd.read_csv(
    'sales_data.csv',
    parse_dates=['Date'])


# In[30]:


# The data at a glance:
sales.head()


# In[31]:


sales.shape
# This gives number of rows & columns within the data.
# (#rows, #columns)


# In[32]:


sales.info()


# In[33]:


sales.describe()


# In[ ]:





# In[34]:


# Numerical Analysis and Visualization

sales['Unit_Cost'].describe()


# In[35]:


sales['Unit_Cost'].mean()


# In[36]:


sales['Unit_Cost'].median()


# In[112]:


jtplot.style(theme='monokai')
#black & white will use this


# In[113]:


sales['Unit_Cost'].plot(kind = 'box', vert = False, figsize = (14, 6))


# In[115]:


sales['Unit_Cost'].plot(kind = 'density', figsize = (14, 6)) #kde


# In[116]:


ax = sales['Unit_Cost'].plot(kind = 'density', figsize = (14, 6)) #kde
ax.axvline(sales['Unit_Cost'].mean(), color = 'red')
ax.axvline(sales['Unit_Cost'].median(), color = 'green')


# In[131]:


ax = sales['Unit_Cost'].plot(kind = 'hist', figsize = (14, 6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')


# In[ ]:





# In[75]:


sales.head()


# In[57]:


# Categorical Analysis and Visualization
# Analyze the Age_Group column
sales['Age_Group'].value_counts()


# In[72]:


sales['Age_Group'].value_counts().plot(kind = 'pie', figsize=(6, 6))


# In[74]:


ax = sales['Age_Group'].value_counts().plot(kind = 'bar', figsize = (14, 6))
ax.set_ylabel('Number of Sales')


# In[76]:


# Relationships between columns
corr = sales.corr()
corr


# In[130]:


fig = plt.figure(figsize = (8, 8))
plt.matshow(corr, cmap = 'RdBu', fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation = 'vertical');
plt.yticks(range(len(corr.columns)), corr.columns);


# In[129]:


sales.plot(kind = 'scatter', x = 'Customer_Age', y = 'Revenue', figsize = (6, 6))


# In[128]:


sales.plot(kind = 'scatter', x = 'Revenue', y = 'Profit', figsize = (6, 6))


# In[127]:


ax = sales[['Profit', 'Age_Group']].boxplot(by = 'Age_Group', figsize = (10, 6))
ax.set_ylabel('Profit')


# In[124]:


boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
sales[boxplot_cols].plot(kind = 'box', subplots = True, layout = (2, 3), figsize = (14, 8))


# In[83]:


# Column Wrangling
# Create new columns or modify existing ones

sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']


# In[84]:


sales['Revenue_per_Age'].head()


# In[111]:


sales['Revenue_per_Age'].plot(kind = 'density', figsize = (14,6))


# In[108]:


sales['Revenue_per_Age'].plot(kind = 'hist', figsize = (14, 6))


# In[90]:


# Add and calculate new Calculated_Cost column

# Use the following formula:
# Calculated_Cost = Order_Quantity * Unit_Cost


# In[117]:


sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']
sales['Calculated_Cost'].head()
# total orders * the cost


# In[121]:


(sales['Calculated_Cost'] != sales['Cost']).sum()
# How many rows had a different value than what was provided by Cost?
# This checks if the Cost provided by the data set, at some point does not align
#with the Calculated_Cost (which is what we calculated above).


# In[119]:


# Can look at the relationship between Cost and Profit using a scatter plot

sales.plot(kind = 'scatter', x = 'Calculated_Cost', y = 'Profit', figsize = (6, 6) )
# Regression plot.
# This shows there exists linear dependency.


# In[107]:


# Add and calculate a new Calculated_Revenue column 

# Use the following formula:
# Calculated_Revenue = Cost + Profit


# In[120]:


sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']
sales['Calculated_Revenue'].head()


# In[122]:


(sales['Calculated_Revenue'] != sales['Revenue']).sum()
# This shows there is no difference between the Revenue and Calculated_Revenue.


# In[125]:


# Notice linear dependency as before.
sales.plot(kind = 'scatter', x = 'Calculated_Revenue', y = 'Profit', figsize = (6, 6))


# In[123]:


sales.head()


# In[126]:


sales['Revenue'].plot(kind = 'hist', bins = 100, figsize = (14, 6))


# In[ ]:


# Modify all Unit_Price values adding 3% tax to them


# In[132]:


sales['Unit_Price'].head()


# In[134]:


#sales['Unit_Price'] = sales['Unit_Price'] * 1.03
sales['Unit_Price'] *= 1.03


# In[135]:


sales['Unit_Price'].head()


# In[ ]:





# In[ ]:


# Selection & Indexing

# Get all the sales made in the state of Kentucky
sales.loc[sales['State'] == 'Kentucky']


# In[ ]:


# Get the mean revenue of the Adults (35-64) sales group
sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()


# In[ ]:


# How many records belong to Age Group Youth (<25) ?
sales.loc[sales['Age_Group'] == 'Youth (<25)'].sum()


# In[ ]:


# How many records belong to Age Group Youth (<25) or Adults (35-64) ?
sales.loc[sales['Age_Group'] == 'Youth (<25)' | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]


# In[ ]:


# Get the mean revenue of the sales group Adults (35-64) in the United States.
sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




