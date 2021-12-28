#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:06:43 2017

@author: jrbrad
"""
import json
import requests

my_wm_username = 'mrpelletier'
search_url = 'https://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
 
#Parse the JSON
root=response.json()
    
numJumpShotsAttempt = 0
numJumpShotsMade = 0


#Looping though JSON to find jumpshots only
for i in range(len(root)):
    if root[i]['ACTION_TYPE'] == 'Jump Shot':
        numJumpShotsAttempt = numJumpShotsAttempt + 1
        
for i in range(len(root)):
    if root[i]['EVENT_TYPE'] == 'Made Shot' and  root[i]['ACTION_TYPE'] == 'Jump Shot':
        numJumpShotsMade = numJumpShotsMade + 1

#Calculating jump shot percentage        
percJumpShotMade = (numJumpShotsMade/numJumpShotsAttempt)  

# Write your program here to populate the appropriate variables
            
print(numJumpShotsAttempt)
print(numJumpShotsMade)
print(percJumpShotMade)


# In[ ]:




