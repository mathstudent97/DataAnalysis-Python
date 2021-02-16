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
# Provides all entries from 0 index up to AND including the max index.


# In[8]:


a[1:3] 
# Indices from 1 up to 3, excluding index 3.


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


# In[166]:


A


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
# 2 groups, 2 rows in each group, 3 columns in each group


# In[39]:


B.ndim


# In[42]:


B.size
# 12 individual numbers within the array.


# In[ ]:


# If the shape isn't consistent, it'll just fall back to regular Python objects:


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


# In[167]:


C


# In[45]:


C.dtype


# In[46]:


C.shape


# In[47]:


C.size


# In[48]:


type(C[0])
# Recall what C looks like above.


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


# In[168]:


A


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
# All rows from index 0(including 0) up to and excluding index 2.


# In[63]:


A[:, :2]


# In[64]:


A[:2, 2:]


# In[65]:


A


# In[171]:


A[1] = np.array([10, 10, 10])


# In[172]:


A


# In[173]:


A[2] = 99
# This updates all indices in 2 position as 99.


# In[174]:


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
# Ex. For column 1: 1+4+7 = 12 / 3 = 4 <- which is the avrg.


# In[169]:


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
# Creates an array consisting of 4 entries as the indices.


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


# In[170]:


l


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
# The '~' implies negation of the conditions within the brackets.


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





# In[124]:


# Size of Objects in Memory
# Int, floats

sys.getsizeof(1)


# In[125]:


# Longs are even longer
sys.getsizeof(10**100)


# In[126]:


np.dtype(int).itemsize


# In[127]:


np.dtype(np.int8).itemsize


# In[128]:


np.dtype(float).itemsize


# In[129]:


# Lists are even larger.

# A one element list.
sys.getsizeof([1])


# In[131]:


# An array of one element in numpy.
np.array([1]).nbytes


# In[132]:


# Performance is also important.

l = list(range(100000))


# In[133]:


a = np.arange(100000)


# In[134]:


get_ipython().run_line_magic('time', 'np.sum(a ** 2)')


# In[135]:


get_ipython().run_line_magic('time', 'sum([x ** 2 for x in l])')


# In[ ]:





# In[136]:


# Useful Numpy Functions

# random
np.random.random(size = 2)


# In[137]:


np.random.normal(size = 2)


# In[138]:


np.random.rand(2, 4)
# 2 rows, 4 columns


# In[139]:


# arange
np.arange(10)


# In[140]:


np.arange(5, 10)


# In[141]:


np.arange(0, 1, .1)


# In[142]:


np.arange(10).reshape(2, 5)


# In[143]:


np.arange(10).reshape(5, 2)


# In[144]:


np.linspace(0, 1, 5)
# start at 0, stop at 1, 5 entries.


# In[145]:


np.linspace(0, 1, 20)
# start at 0, stop at 1, 20 entries.


# In[146]:


np.linspace(0, 1, 20, False)


# In[147]:


# zeros, ones, empty
np.zeros(5)
# 5 float '0.'


# In[150]:


np.zeros((3,3))
# 3 rows with 3 entries each where each entry is float '0.'


# In[152]:


np.zeros((3, 3), dtype=int)
# 3 rows with 3 entries each, where each entry is int '0'.


# In[154]:


np.ones(5)
# 1 row with 5 entries as float '1.'.


# In[156]:


np.ones((3, 3))
# 3 rows with 3 entries each, where each entry is float '1.'.


# In[157]:


np.empty(5)


# In[158]:


np.empty((2, 2))


# In[160]:


# identity and eye

np.identity(3)
# identity matrix with 3 rows.


# In[161]:


np.eye(3, 3)


# In[163]:


np.eye(8, 4)
# 8 by 4 identity matrix.


# In[164]:


np.eye(8, 4, k=1)


# In[165]:


"Hello World"[6]

