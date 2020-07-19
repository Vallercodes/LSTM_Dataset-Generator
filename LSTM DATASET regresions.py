#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


long = []                  # sett blanc list for tracking
def generated_LSTM(n):      # set function name with n. n to be number of iterations
    k = 0.00                  # initialise the long list with Zero float
    for i in range(n):                   #takes number of iterations for dataset
        c = random.randint(0,3)         # probability of postive to negative is set to 2/3 neg
        if c == 0:
            k = k + round(random.uniform(01.00, 25.00), 2)        # for 1/3 positive random travel set up to 25 to 2 dp
        else:
            k = k - round(random.uniform(1.00, 3.33), 2)          # for 2/3 negative random travel set to upto 33.33
            long.append(k)          # append new total of k to continue long list
        #print(k)
           
generated_LSTM(9000)           # set desired number of iterarations


# In[4]:


df = pd.DataFrame(long, columns=['Roll'])          # save completed list to Pandas DataFrame
#df = pd.DataFrame(long)
print(df.head())
df.to_csv('LSTM_GenData.csv', index=False)              # save Dataset to csv removing index as will be index when read if nessacery
plt.plot(long)

plt.show()


# In[ ]:




