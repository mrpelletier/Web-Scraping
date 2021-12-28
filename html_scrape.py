#!/usr/bin/env python
# coding: utf-8

# In[64]:


import requests 
from bs4 import BeautifulSoup

#Creating variable for url
url = 'http://publicinterestlegal.org/county-list/'

#Requesting info with header
response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/50.0.2661.102Safari/537.36"}).content

#Parsing data
root = BeautifulSoup(response, 'lxml')

#Assigning rows to a variable
target_rows = root.find_all('tr')

#Counting rows and assigning it to a variable
sublist_total = (len(target_rows))

#Looping through rows to create sublists 
sub = []
for i in target_rows:
    new_sub = []
    for x in i.find_all('td'):
        new_sub.append(x.text)    
        
    sub.append(new_sub)

#Printing outcomes

print(sublist_total)
print(sub)


# In[ ]:





# In[ ]:





# In[ ]:




