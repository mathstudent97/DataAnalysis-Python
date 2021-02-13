#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import numpy as np


# In[3]:


# Basic Numpy Arrays
np.array([1, 2, 3, 4])


# In[4]:


a = np.array([1, 2, 3, 4])


# In[5]:


b = np.array([0, .5, 1, 1.5, 2])


# In[6]:


a[0], a[1]


# In[7]:


a[0:]


# In[8]:


a[1:3] 
# indices from 1 to 3 excluding index 3


# In[9]:


a[1:-1]


# In[10]:


a[::2]


# In[11]:


b


# In[12]:


b[0], b[2], b[-1]


# In[14]:


b[[0, 2, -1]]


# In[ ]:





# In[15]:


# Array Types


# In[16]:


a


# In[17]:


a.dtype


# In[18]:


b


# In[19]:


b.dtype


# In[21]:


np.array([1, 2, 3, 4], dtype=float)


# In[23]:


np.array([1, 2, 3, 4], dtype=np.int8)


# In[24]:


c = np.array(['a', 'b', 'c'])


# In[25]:


c.dtype


# In[26]:


d = np.array([{'a': 1}, sys])


# In[27]:


d.dtype


# In[ ]:





# In[28]:


# Dimensions and shapes
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])


# In[30]:


A.shape
# (2 rows, 3 columns)


# In[40]:


A.ndim
# 2 sets of [[?


# In[33]:


A.size
# 6 individual numbers within the array


# In[34]:


B = np.array([
    [
        [12, 11, 10],
        [9, 8, 7]
    ],
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
])


# In[35]:


B


# In[37]:


B.shape
# 2 groups, 2 rows ine ach group, 3 columns in each group


# In[39]:


B.ndim


# In[42]:


B.size
# 12 individual numbers within the array.


# In[44]:


C = np.array([
    [
        [12, 11, 10],
        [9, 8, 7],
    ],
    [
        [6, 5, 4]
    ]
])


# In[45]:


C.dtype


# In[46]:


C.shape


# In[47]:


C.size


# In[48]:


type(C[0])


# In[ ]:





# In[58]:


# Indexing and Slicing of Matrices

# Square matrix
A = np.array([
#.   0. 1. 2.    
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8 ,9]  #2
])


# In[59]:


A[1]


# In[60]:


A[1][0]
# row first, then column.


# In[61]:


# A[d1, d2, d3, d4]
A[1, 0]
# basically combined the above.


# In[62]:


A[0:2]
# All rows from 0(including 0) up to and excluding 2


# In[63]:


A[:, :2]


# In[64]:


A[:2, 2:]


# In[65]:


A


# In[66]:


A[2] = 99
# This updates all indices in 2 position as 99.


# In[67]:


A


# In[ ]:





# In[68]:


# Summary Statistics
a = np.array([1, 2, 3, 4])


# In[69]:


a.sum()


# In[70]:


a.mean()


# In[71]:


a.std()


# In[72]:


a.var()


# In[73]:


A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# In[74]:


A.sum()


# In[75]:


A.mean()


# In[76]:


A.std()


# In[77]:


A.var()


# In[78]:


A.sum(axis=0)
# This provides the sum of numbers within each column index.


# In[79]:


A.sum(axis=1)
# This provides the sum of numbers within each row index.


# In[80]:


A.mean(axis=0)
# This provides the mean/ avrg. of the numbers within each column index.
# Ex. For column 1: 1+4+7 = 12 / 3 = 4 <- which is the avrg


# In[ ]:


A.mean(axis=1)
# Similar to above.
# This provides the mean/avg. of the numbers within each row index.
# Ex. For row 1: 1+2+3 = 6 / 3 = 2 


# In[81]:


A.std(axis=0)


# In[82]:


A.std(axis=1)


# In[ ]:





# In[84]:


# Broadcasting and Vectorized Operations

a = np.arange(4)


# In[85]:


a


# In[86]:


a + 10


# In[87]:


a * 10


# In[88]:


a


# In[89]:


a += 100


# In[90]:


a


# In[91]:


l = [0, 1, 2, 3]


# In[92]:


[i * 10 for i in l]


# In[93]:


a = np.arange(4)


# In[94]:


a


# In[95]:


b = np.array([10, 10, 10, 10])


# In[96]:


b


# In[97]:


a + b


# In[98]:


a * b


# In[ ]:





# In[99]:


# Boolean Arrays

a = np.arange(4)


# In[100]:


a


# In[101]:


a[0], a[-1]


# In[102]:


a[[0, -1]]


# In[103]:


a[[True, False, False, True]]


# In[104]:


a


# In[105]:


a >= 2


# In[106]:


a[a >= 2]


# In[107]:


a.mean()


# In[108]:


a[a > a.mean()]


# In[109]:


a[~(a > a.mean())]


# In[110]:


a[(a == 0) | (a == 1)]


# In[111]:


a[(a <= 2) & (a % 2 == 0)]


# In[112]:


A = np.random.randint(100, size=(3, 3))


# In[113]:


A


# In[114]:


A[np.array([
    [True, False, True],
    [False, True, False],
    [True, False, True]
])]


# In[115]:


A > 30


# In[116]:


A[A > 30]


# In[ ]:





# In[117]:


# Linear Algebra
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# In[118]:


B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])


# In[119]:


A.dot(B)


# In[120]:


A @ B


# In[121]:


B.T


# In[122]:


A


# In[123]:


B.T @ A


# In[ ]:




