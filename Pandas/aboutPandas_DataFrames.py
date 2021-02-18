#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075   
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])


# In[3]:


df


# In[4]:


df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'UK',
    'US'
]


# In[5]:


df


# In[6]:


df.index


# In[7]:


df.info()


# In[8]:


df.size


# In[10]:


df.shape


# In[11]:


df.describe()


# In[12]:


df.dtypes


# In[13]:


df.dtypes.value_counts()


# In[ ]:





# In[14]:


# Indexing, Selection and Slicing
df


# In[15]:


df.loc['Canada']


# In[16]:


df.iloc[-1]


# In[17]:


df['Population']


# In[18]:


df['Population'].to_frame()


# In[19]:


df[['Population', 'GDP']]


# In[20]:


df[1:3]


# In[21]:


df.loc['Italy']


# In[22]:


df.loc['France': 'Italy']


# In[24]:


df.loc['France': 'Italy', 'Population']


# In[25]:


df.loc['France': 'Italy', 'Population'].to_frame()


# In[26]:


df.loc['France': 'Italy', ['Population', 'GDP']]


# In[29]:


df


# In[30]:


df.iloc[0]


# In[31]:


df.iloc[0].to_frame()


# In[32]:


df.iloc[-1]


# In[33]:


df.iloc[[0, 1, -1]]


# In[34]:


df.iloc[1:3]


# In[35]:


df.iloc[1:3, 3]


# In[36]:


df.iloc[1:3, 3].to_frame()


# In[37]:


df.iloc[1:3, [0,3]]


# In[38]:


df.iloc[1:3, 1:3]


# In[ ]:





# In[ ]:


# Conditional selection (boolean arrays)


# In[39]:


df


# In[40]:


df['Population'] > 70


# In[44]:


(df['Population'] > 70).to_frame()


# In[45]:


df.loc[df['Population'] > 70]


# In[46]:


df.loc[df['Population'] > 70, 'Population']


# In[48]:


df.loc[df['Population'] > 70, 'Population'].to_frame()


# In[49]:


df.loc[df['Population'] > 70, ['Population', 'GDP']]


# In[ ]:





# In[50]:


# Dropping Stuff
df.drop('Canada')


# In[53]:


df.drop(['Canada', 'Japan'])


# In[54]:


df.drop(columns=['Population', 'HDI'])


# In[56]:


df


# In[57]:


df.drop(['Italy', 'Canada'], axis=0)


# In[59]:


df.drop(['Population', 'HDI'], axis=1)


# In[60]:


df.drop(['Population', 'HDI'], axis='columns')


# In[61]:


df.drop(['Canada', 'Germany'], axis='rows')


# In[ ]:





# In[ ]:


# Operations


# In[62]:


df[['Population', 'GDP']]


# In[63]:


df[['Population', 'GDP']] / 100


# In[65]:


crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
crisis


# In[66]:


df[['GDP', 'HDI']]


# In[67]:


df[['GDP', 'HDI']] + crisis


# In[ ]:





# In[ ]:


# Modifying DataFrames


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




