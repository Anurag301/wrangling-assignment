#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
z = np.zeros(10)
z[4] = 1
print(z)


# In[6]:


import numpy as np
z = np.arange(10,50)
print(z)


# In[7]:


import numpy as np
z=np.arange(9).reshape(3,3)
print(z)


# In[8]:


import numpy as np
ap=np.nonzero([1,2,0,0,4,0])
print(ap)


# In[10]:


import numpy as np
z=np.random.random((10,10))
zmin,zmax=z.min(),z.max()
print(zmin,zmax)


# In[12]:


import numpy as np
z=np.random.random(30)
mean_value = z.mean()
print(mean_value)

