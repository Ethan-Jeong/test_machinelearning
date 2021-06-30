#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[2]:


# In[5]:


favorite_load = pickle.load(open('./favorite_save.pkl','rb'))
print(favorite_load)

type(favorite_load)


# In[6]:


print(favorite_load['tiger'])


# In[12]:


autompg_lr = pickle.load(open('./saves/autompg_lr.pkl','rb'))


# In[13]:


type(autompg_lr)


# In[14]:
# input from outside

a = 3504.8
b = 8

import numpy as np
pre = np.array([[a,b]])

print(autompg_lr.predict(pre))

print(autompg_lr.predict([[3504.0,8]]))


# In[ ]:




