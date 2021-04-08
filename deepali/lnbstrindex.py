#!/usr/bin/env python
# coding: utf-8

# In[1]:


value = input('enter string value : ')


# In[2]:


len(value)


# In[4]:


if(len(value)>7):
    for i in range(0, len(value), 2):  
        print(value[i]); 


# In[5]:


if(len(value)<=7):
    for i in range(0, len(value), 2):  
        print(value[i]); 


# In[ ]:




