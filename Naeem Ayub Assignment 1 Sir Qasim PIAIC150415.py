#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


#    # 1. zeros ()  array , 2 by 3 Array Creation:
#    

# In[4]:


arr = np.zeros((2,3))


# In[5]:


arr


# # 2. empty ()  array

# In[6]:


arr1 = np.empty([4,5])    #empy array


# In[7]:


arr1     #Checking


# # 3. array creation by Arange arange () 

# In[8]:


arr2 = np.arange(1,20, 2)


# In[9]:


arr2  # Checking


# # 4. reshape() 

# In[10]:


arr2.reshape(2,5)


# # 5. linspace ()

# In[11]:


arr5 = np.linspace(0,10, 5)   # equal gap in between element


# In[12]:


arr5


# # 6. exp()

# In[13]:


np.exp(arr5)


# # 7. sum()

# In[14]:


np.sum(arr5)


# # 8. add()

# In[15]:


np.add(arr5, [1,2,3,4,5])


# # 9. sqrt()

# In[16]:


np.sqrt(arr5)


# # 10. min()

# In[17]:


np.min(arr5)


# # 11. Max()

# In[18]:


np.max(arr5)


# # 12. Average()

# In[19]:


np.average(arr5)


# # 13. view ()

# In[20]:


arr6 = arr5.view()


# In[21]:


arr6 is arr5


# In[22]:


arr6


# In[23]:


arr5


# In[24]:


arr5[0] = 3


# In[25]:


arr6


# In[26]:


arr5


# # 14. copy()

# In[27]:


arr7 = arr5.copy()


# In[28]:


arr7 


# In[29]:


arr7[0] = 20


# In[30]:


arr7


# In[31]:


arr5


# # 15. mean()

# In[32]:


arr5.mean()


# # 16 all()

# In[33]:



arr5.all()


# # 17 cumprod() 

# In[34]:



arr5.cumprod()


# # 18 cumsum()

# In[234]:


arr5.cumsum()


# # 19 size()

# In[36]:


#19
np.size(arr5)


# # 20 round()

# In[235]:



arr5.round()


# # 21 argmax()

# In[38]:




arr5.argmax()


# # 22. argmin()

# In[39]:




arr5.argmin()


# # 23 ravel()

# In[40]:



arr20 = np.array([[2,4,5,6],
                [6,7,7,8]])
arr20


# In[41]:


arr20.ravel()


# # 24 clip()

# In[42]:


#24
arr20.clip(5,9)


# # 25 argsort()

# In[43]:



arr20.argsort()


# # 26 true_divide()

# In[248]:



np.true_divide([30,40,50],5)


# # 27 var() 

# In[45]:



arr20


# In[46]:


arr20.var()


# # 28 byteswap()

# In[54]:



arr30 = arr20.byteswap()


# In[56]:


arr30


# # 29 arra_split()

# In[55]:



np.array_split(arr20,2)


# # 30. inner()

# In[49]:



x = np.array([2,4])
y = np.array([3,5])


# In[50]:


np.inner(x,y)


# # 31 round()

# In[82]:



arr35 = np.array([2.43,5.67,76.8,99.32])
np.round(arr35,1)


# # 32 around()

# In[85]:



np.around(arr35,2)


# # 33 fix()

# In[86]:



np.fix(arr35)


# # 34 floor()

# In[87]:



np.floor(arr35)


# # Ceil()

# In[89]:



np.ceil(arr35)


# # 35 trunc()

# In[249]:



np.trunc(arr35)


# # 36 rint()

# In[250]:



np.rint(arr35)


# # 37 lcm()

# In[129]:



np.lcm([55,66,7,8,99],2)


# # 38 gcd()

# In[128]:



np.gcd([55,66,7,8,99],3)


# # 39 clip()

# In[242]:



arr35


# In[134]:


np.clip(arr35,5,66)


# # 40 square()

# In[150]:



arr40 = np.square(arr35)
arr40


# # 41 absolute() or abs()

# In[241]:



np.absolute([-5,-6,6,3])
np.abs([-5,-6,6,3])


# # 42 remainder()

# In[195]:



arr50 = np.array([[30,40],[55,77]])


# In[198]:


np.remainder(arr50,3)


# # 43 exp()

# In[201]:



np.exp([4,5,6])


# # 44 exp2()

# In[203]:



np.exp2([4,5,6])


# # 45 log2()

# In[206]:




np.log2([4,5,6])


# # 46 cross()

# In[238]:



x = [3,5,6]
y = [6,8,9]
np.cross(x,y)


# # 47 subtract()

# In[220]:




np.subtract(x,y)


# # 49 ediff1d()

# In[224]:



p = np.array([44,5,8,7,88,99])
np.ediff1d(p)


#  # 50 power()

# In[232]:



nn = [4,5,6]
aa = [2,4,8]


# In[233]:


np.power(nn,aa)


# In[ ]:




