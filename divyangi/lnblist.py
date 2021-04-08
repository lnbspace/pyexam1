#!/usr/bin/env python
# coding: utf-8

# In[1]:


l1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element= int(input())

    l1.append(element)
print(l1)

l2 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element= int(input())

    l2.append(element)
print(l2)


L3 = l1[1::2]+l2[::2]
print(L3)


# In[ ]:




