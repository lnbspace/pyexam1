#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = []
n = int(input("Enter number of elements : "))
for i in range(0, 5):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)


# In[2]:


lst.remove(6)


# In[3]:


lst.remove(5)


# In[4]:


lst


# In[6]:


total=0
for ele in range(0, len(lst)):
    total = total + lst[ele]
 
# printing total value
print("Sum of all elements in given list: ", total)


# In[ ]:




