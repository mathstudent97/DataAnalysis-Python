#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inLine')


# In[7]:


import os


# In[9]:


# Ensure that you have the correct working directory.
# The file containing the data should be located within your current working directory.

#os.getcwd() -> This provides your current working directory.
#os.chdir('C:\\Users\\maullonv\\Desktop\\dataAnalysisPython') 
    #-> Use this to change your working directory if needed.


# In[ ]:





# In[13]:


# Load Data

# read the csv file into Python

sales = pd.read_csv(
    'sales_data.csv',
    parse_dates=['Date'])


# In[14]:


# The data at a glance:
sales.head()


# In[19]:


sales.shape
# This gives number of rows & columns within the data.
# (#rows, #columns)


# In[16]:


sales.info()


# In[17]:


sales.describe()


# In[ ]:





# In[20]:


# Numerical Analysis and Visualization

sales['Unit_Cost'].describe()


# In[ ]:


sales['Unit_Cost'].mean()


# In[ ]:


sales['Unit_Cost'].median()


# In[ ]:


sales['Unit_Cost'].plot(kind = 'box', vert = False, figsize = (14, 6))


# In[ ]:


sales['Unit_Cost'].plot(kind = 'density', figsize = (14, 6)) #kde


# In[ ]:


ax = sales['Unit_Cost'].plot(kind = 'density', figsize = (14, 6)) #kde
ax.axvline(sales['Unit_Cost'].mean(), color = 'red')
ax.axvline(sales['Unit_Cost'].median(), color = 'green')


# In[ ]:


ax = sales['Unit_Cost'], plot(kind = 'hist', figsize = (14, 6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')

