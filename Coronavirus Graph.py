#!/usr/bin/env python
# coding: utf-8

# In[73]:


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import scale
from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.cluster import AgglomerativeClustering
from datetime import date
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('D:\\covid-19-data-master\\us-states.csv')


# In[4]:


df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].map(lambda x: x.strftime('%B'))


# In[5]:


reference_dic = dict()
state_codes = (df.loc[: , ('state', 'fips')]).copy()
monthly_cases = dict()
for i, j, k in state_codes.itertuples():
    reference_dic[k] = j
    monthly_cases['Jan/f' + str(k)] = [] 
    monthly_cases['Feb/f' + str(k)] = []


# In[6]:


new_df = df.reindex(columns=['fips', 'month', 'cases'])


# In[7]:


for i, j, k, m in new_df.itertuples():
    if k == 'January':
        monthly_cases['Jan/f' + str(j)].append(m)
    elif k == 'February':
        monthly_cases['Feb/f' + str(j)].append(m)


# In[8]:


df2 = pd.DataFrame(columns=['states', 'covid19_rate', 'unempl_rate'])


# In[9]:


avg_covid19_rate = dict() 
for i, j in monthly_cases.items():
    if i[:3] == 'Jan' and j == []:
        avg_covid19_rate[i] = 0
    elif i[:3] == 'Feb' and j == []:
        avg_covid19_rate[i] = 0
    elif i[:3] == 'Jan' and j != []:
        rate = pd.Series(j).pct_change().mean() 
        avg_covid19_rate[i] =  rate  
    elif i[:3] == 'Feb' and j != []:
        rate = pd.Series(j).pct_change().mean() 
        avg_covid19_rate[i] =  rate 


# In[10]:


for i, j in avg_covid19_rate.items():
    if i[:3] == 'Jan':
        rate = j - avg_covid19_rate['Feb/' + i[4:]] 
        df2 = df2.append({'states': reference_dic[int(i[5:])], 'covid19_rate': rate}, ignore_index=True)


# In[11]:


df2 = df2.set_index('states')


# In[12]:


df3 = pd.read_html('https://www.bls.gov/web/laus/laumstcm.htm#laumstcm.f.p')


# In[13]:


df3 = df3[0].drop([51,52, 53])


# In[14]:


for i, j, k, l, m, n in df3.itertuples():
    if j in df2.index:
        df2.loc[j, 'unempl_rate'] = m


# In[15]:


df2.dropna(inplace=True)


# In[71]:


X = (scale(df2))


# In[74]:


dendrogram = dendrogram(linkage(X, method='complete'))


# In[57]:


model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='complete')
model.fit(X)
labels = model.labels_


# In[58]:


labels


# In[76]:


plt.title('COVID-19 rate Vs. Unemployment rate within the U.S\n(for the month of Jan & Feb)')
plt.scatter(X[labels==0, 0], X[labels==0, 1], s=50, marker='+', color='red')
plt.scatter(X[labels==1, 0], X[labels==1, 1], s=50, marker='+', color='blue')


# In[ ]:




