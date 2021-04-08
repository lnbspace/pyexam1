#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gTTS 


# In[2]:


pip install playsound


# In[3]:


pip install pyttsx3  


# In[4]:


import gtts  
from playsound import playsound


# In[5]:


t1 = gtts.gTTS("I found a love for me Oh darling, just dive right in and follow my lead Well, I found a girl, beautiful and sweetOh, I never knew you were the someone waiting for me") 


# In[7]:


t1.save("perfect.mp3")


# In[8]:


playsound("perfect.mp3")  


# In[ ]:




