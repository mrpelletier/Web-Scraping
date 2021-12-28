#!/usr/bin/env python
# coding: utf-8

# In[40]:


#Importing packages
import requests
from lxml import objectify

#Retrieving our data and amking is parsable
response = requests.get("https://www.ncdc.noaa.gov/cag/statewide/rankings/44-tavg-201608/data.xml").content
root = objectify.fromstring(response)

#Embedding URL to store empty spots for values we seek
template = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'

#Assigning values to variables
state = '44'
parameter = 'tavg'
year = '2016'
mon = '08'

#Creating URL with inputed values
URL = template % (state,parameter,year,mon)

#Pasting parameters as strings

print('Value:',root.data[4]['value'])
print('Mean:',root.data[4]['mean'])
print('Departure:',root.data[4]['departure'])
print('Low rank:',root.data[4]['lowRank'])
print('High rank:',root.data[4]['highRank'])


# In[ ]:





# In[ ]:




