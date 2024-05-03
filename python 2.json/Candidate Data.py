#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import csv


# In[2]:


with open("C:/Users/Windows10/Downloads/python json/test.json") as f:
    data=json.load(f)


# In[3]:


with open('degree6.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    header_row=['full_name','social_url','location']
    for i in range(1, 7): 
        header_row.extend(['Degree {}'.format(i), 'Start Time {}'.format(i), 'End Time {}'.format(i)])
    csvwriter.writerow(header_row)


    for entry in data:
        full_name = entry['full_name']
        social_url = entry['social_url']
        location = entry['location']
        education = entry['education']
        
        unique_degrees = set()
        degrees_info = []

        for edu in education:
            if edu.get("degree") is None:
                continue
            degree_str = " ".join(edu['degree'])
            start_time = edu.get('start_time', '')  
            end_time = edu.get('end_time', '') 
            if degree_str and degree_str not in unique_degrees:
                degrees_info.append((degree_str, start_time, end_time))
                unique_degrees.add(degree_str)
                
        while len(degrees_info) < 5:
            degrees_info.append(('',' ',' '))
            
        
        row_data = [full_name, social_url, location]
        for degree, start_time, end_time in degrees_info:
            row_data.extend([degree, start_time, end_time])
        csvwriter.writerow(row_data)


# In[4]:


df=pd.read_csv("degree6.csv")


# In[5]:


df2=df.drop(columns=['Degree 6','Degree 5','Start Time 5','Start Time 6','End Time 5','End Time 6'])


# In[6]:


df2[['Local Authority Name','local_authority_name_modified','district_modified']]=df['location'].str.split(',',expand=True)


# In[7]:


df3=df2[['full_name','social_url','location','Local Authority Name','local_authority_name_modified','district_modified','Degree 1','Start Time 1','End Time 1','Degree 2','Start Time 2','End Time 2','Degree 3','Start Time 3','End Time 3','Degree 4','Start Time 4','End Time 4']]


# In[8]:


df4=df3.rename(columns = {'Start Time 1': 'start year 1','Start Time 2': 'start year 2',
                        'Start Time 3': 'start year 3','Start Time 4': 'start year 4',
                        'End Time 1': 'end year 1','End Time 2': 'end year 2','End Time 3': 'end year 3','End Time 4': 'end year 4'})


# In[9]:


df4[['degree 1','subject 1','sub1']]=df3['Degree 1'].str.split('-',expand=True)
df4[['degree 2','subject 2','sub2']]=df3['Degree 2'].str.split('-',expand=True)
df4[['degree 3','subject 3','sub3']]=df3['Degree 3'].str.split('-',expand=True)


# In[28]:


#df4.drop(columns=['sub1','sub3','sub2','Degree 1','Degree 2','Degree 3'])


# In[11]:


df5=df4[['full_name','social_url','location','Local Authority Name','local_authority_name_modified','district_modified','degree 1','subject 1','start year 1','end year 1','degree 2','subject 2','start year 2','end year 2','degree 3','subject 3','start year 3','end year 3','Degree 4','start year 4','end year 4']]


# In[12]:


postal_codes_df=pd.read_csv("C:/Users/Windows10/Downloads/National_Statistics_Postcode_Lookup_UK_20240327.csv")


# In[13]:


get_ipython().system('pip install geopy')


# In[14]:


import geopy
from geopy.geocoders import Nominatim


# In[30]:


def get_postal_code(location):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location_data = geolocator.geocode(location)
    if location_data:
        return location_data.raw.get('postcode')
    else:
        return "Postal code not found"
get_postal_code(location)
#df5['postal code'] = df5['location'].apply(get_postal_code)
df5.loc[:, "postalcode"]=get_postal_code(location)
#df5


# In[16]:


df5.to_excel("output4.xlsx")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




