
# coding: utf-8

# In[13]:


#coding:utf-8
import os
os.chdir('C:\\Users\\hnw\\Desktop\\koujian')
new_name=0
movie_name = os.listdir('C:\\Users\\hnw\\Desktop\\koujian')
for temp in movie_name:
    new_name =new_name+1
 
    os.rename('C:\\Users\\hnw\\Desktop\\koujian\\'+temp,'C:\\Users\\hnw\\Desktop\\koujian\\'+str(new_name)+'.jpg')

