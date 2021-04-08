#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess


# In[4]:


devices = subprocess.check_output(['netsh','wlan','show','network'])
devices = devices.decode('ascii')
devices= devices.replace("\r","")
print(devices)


# In[ ]:




