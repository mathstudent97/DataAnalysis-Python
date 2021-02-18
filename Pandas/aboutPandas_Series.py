#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Analyzing the population.
# In millions.

g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])


# In[3]:


g7_pop


# In[6]:


# Others may not know that the population is represented in millions of inhabitants.
# Will name the series to avoid confusion.

g7_pop.name = 'G7 Populaion in millions'


# In[7]:


g7_pop


# In[8]:


g7_pop.dtype


# In[9]:


g7_pop.values


# In[10]:


type(g7_pop)


# In[11]:


type(g7_pop.values)


# In[12]:


g7_pop


# In[13]:


g7_pop[0]


# In[14]:


g7_pop[1]


# In[15]:


g7_pop.index


# In[16]:


l = ['a', 'b', 'c']


# In[17]:


g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States'
]


# In[18]:


g7_pop


# In[19]:


pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'UK': 64.511,
    'US': 318.523
}, name = 'G7 Population in millions')


# In[20]:


pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'UK', 'US'],
    name='G7 in millions')


# In[21]:


pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])


# In[ ]:





# In[22]:


# Indexing
g7_pop


# In[23]:


g7_pop['Canada']


# In[24]:


g7_pop['Japan']


# In[25]:


g7_pop.iloc[0]


# In[26]:


g7_pop.iloc[-1]


# In[27]:


g7_pop[['Italy', 'France']]


# In[28]:


g7_pop['Canada': 'Italy']


# In[ ]:





# In[30]:


# Conditional Selection (boolean arrays)
g7_pop


# In[31]:


g7_pop > 70


# In[32]:


g7_pop[g7_pop > 70]


# In[33]:


g7_pop.mean()


# In[34]:


g7_pop[g7_pop > g7_pop.mean()]


# In[36]:


g7_pop.std()


# In[ ]:


~ not
| or
& and


# In[37]:


g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]


# In[ ]:





# In[39]:


# Operations and Methods
g7_pop


# In[40]:


g7_pop * 1_000_000


# In[41]:


g7_pop.mean()


# In[42]:


np.log(g7_pop)


# In[43]:


g7_pop['France': 'Italy'].mean()


# In[ ]:





# In[44]:


# Boolean Arrays
g7_pop


# In[45]:


g7_pop > 80


# In[46]:


g7_pop[g7_pop > 80]


# In[47]:


g7_pop[(g7_pop > 80) | (g7_pop < 40)]


# In[48]:


g7_pop[(g7_pop > 80) & (g7_pop < 200)]


# In[49]:


# Modufying Series

g7_pop['Canada'] = 40.5


# In[50]:


g7_pop


# In[51]:


g7_pop.iloc[-1] = 500


# In[52]:


g7_pop


# In[53]:


g7_pop[g7_pop < 70]


# In[54]:


g7_pop[g7_pop < 70] = 99.99


# In[55]:


g7_pop


# In[ ]:





# In[ ]:




