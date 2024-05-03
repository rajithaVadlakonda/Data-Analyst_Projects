#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[2]:


dataset=pandas.read_excel("C:\\Users\\Windows10\\Desktop\\Data Gardener Solutions\\csv\\demoset.xlsx")


# In[3]:


import pandas as pd


# In[4]:


dataset=pd.read_excel("C:\\Users\\Windows10\\Desktop\\Data Gardener Solutions\\csv\\demoset.xlsx")


# In[5]:


#dataset


# In[6]:


d2=dataset[["COMPANY_NAME","TURNOVER"]]


# In[7]:


g=d2.groupby("COMPANY_NAME", sort=False)


# In[8]:


g


# In[9]:


for company,company_name in g:
    print(company)
    #print(company_name)


# In[10]:


li=list(g)


# In[11]:


CAGR=[] 
j=0
for i in range(0,len(li)):
    l=len(li[i][1])
    for k in range(j,j+l):
    
        d2.CAGR=((d2.TURNOVER.iloc[k]/d2.TURNOVER.iloc[j])**(1/len(li[i][1]))-1)*100
        CAGR+=[d2.CAGR]

    j=l+j
#print(CAGR)
dataset.loc[:, "CAGR"]=CAGR


# In[12]:


dataset["EBITDA"]=dataset["OPERATING_PROFITS"]+dataset["DEPRECIATION"]


# len(CAGR)

# In[13]:


dataset["Z_SCORE"]=(1.2)*(dataset["WORKING_CAPITAL"]/dataset["TOTAL_ASSETS"])+(1.4)*(dataset["RETURN_NET_ASSETS"]/dataset["TOTAL_ASSETS"])+(3.3)*(dataset["EBITDA"]/dataset["TOTAL_ASSETS"])+(0.6)*(dataset["RETURN_EQUITY"]/dataset["TOTAL_CURRENT_LIABILITIES"])+(1.0)*(dataset["SALES_PER_NET_WORKING_CAPITAL"]/dataset["TOTAL_ASSETS"])


# In[14]:


dataset.to_excel("C:\\Users\\Windows10\\Desktop\\Data Gardener Solutions\\csv\\demoset6.xlsx")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




