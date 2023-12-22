#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import re


# In[8]:


df = pd.read_csv("C:/Users/PCC/Downloads/HealthApp_2k.log_structured.csv")


# In[9]:


templates = pd.read_csv("C:/Users/PCC/Downloads/HealthApp_2k.log_templates.csv")


# In[12]:


df


# In[13]:


df.info()


# In[58]:


# Check for missing values and decide how to handle them. You can either remove rows with missing values or impute 
# them with appropriate values (mean, median, mode, etc.). To check for missing values:

df.isnull()


# In[54]:


df.notnull()


# In[56]:


df.shape


# In[15]:


df.head(5)


# In[57]:


df.tail(5)


# In[17]:


df.describe()


# In[25]:


df.count()


# In[32]:


df.min()


# In[34]:


df.head(5)


# In[36]:


df = df.drop('Pid', axis=1)


# In[37]:


df


# In[39]:


dfs23 = df[df['EventId'] == 'E22']
dfs23['Time'] = pd.to_datetime(dfs23['Time'], format='%Y%m%d-%H:%M:%S:%f')
dfs23['Steps'] = dfs23['Content'].str.extract(r'##(\d+)##')
dfs23['Steps'] = dfs23['Steps'].astype(int)
plt.figure(figsize=(12, 6))
plt.plot(dfs23['Time'], dfs23['Steps'], marker='o', linestyle='-')
plt.title('Time vs. Steps for Event E22')
plt.xlabel('Time')
plt.ylabel('Steps')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[40]:


dfs23.head()


# In[41]:


dfs23['Time'] = pd.to_datetime(dfs23['Time'], format='%Y%m%d-%H:%M:%S:%f')

dfs23['Date'] = dfs23['Time'].dt.date

print(dfs23[['Date', 'Steps']])

plt.figure(figsize=(10, 6))
plt.plot(dfs23['Date'], dfs23['Steps'], marker='o')
plt.title('Steps Per Day')
plt.xlabel('Date')
plt.ylabel('Steps')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[42]:


dfs23


# In[43]:


dfs23['Date'] = dfs23['Time'].dt.date
dfs23['Hour'] = dfs23['Time'].dt.hour
dfs23['Minute'] = dfs23['Time'].dt.minute

steps_increase_threshold = 1000
min_duration_minutes = 30

workout_sessions = []
current_session = None

for index, row in dfs23.iterrows():
    if row['Steps'] > steps_increase_threshold:
        if current_session is None:
            current_session = {'start_time': row['Time']}
        else:
            current_session['end_time'] = row['Time']
    else:
        if current_session is not None:
            duration = (current_session['end_time'] - current_session['start_time']).total_seconds() / 60
            if duration >= min_duration_minutes:
                workout_sessions.append(current_session)
            current_session = None

if workout_sessions:
    print("Workout sessions:")
    for session in workout_sessions:
        print(f"Start: {session['start_time']} - End: {session['end_time']}")


# In[44]:


dfsd24 = df[df['EventId'] == 'E4']
dfsd24['Calories'] = dfsd24['Content'].str.extract(r'(\d+)')
dfsd24['Calories'] = dfsd24['Calories'].astype(int)
dfsd24.head()


# In[52]:


dfsd24['Time'] = pd.to_datetime(dfsd24['Time'], format='%Y%m%d-%H:%M:%S:%f')

plt.figure(figsize=(12, 6))
plt.plot(dfsd24['Time'], dfsd24['Calories'], marker='o', linestyle='-', color='b')
plt.title('Calorie Burn Over Time')
plt.xlabel('Time')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.tight_layout()

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))

plt.show()


# In[61]:


# To remove rows with missing values:

df.dropna()


# In[62]:


# Check for null values
df.isnull().values.any()


# # Conclusions
# From the given observations app loads detailed steps data when event E22 occures. On further analysis (refer to cell 3) the following can be concluded:

on 23-12-2017(from 10:15PM to 23:57PM) person's total step count = 7214
on 24-12-2017(from 00:00AM to 00:29AM) person's total step count = 0
Person's average number of steps per day = 23898 (approx)
Workout sessions (Refer to cell 4): Start: 2017-12-23 22:15:29.635000 - End: 2017-12-24 00:00:00.234000
On 23-12-2017 after 11:14PM there is no change in steps or there isn't any movements so the person might be resting or put their phone on rest
# # Calorie Counter
# 
From the given observations app loads detailed calorie data when event E4 occures. On further analysis (refer to cell 7, 8) the following can be concluded:

on 23-12-2017(from 10:15PM to 23:57PM) person's total(cumulative) calories = 131208
on 24-12-2017(from 00:00AM to 00:29AM) person's total calories = 0
# # Confirmations
# 
On 23-12-2017 there is no any major change in steps and calories from 11:14 PM, this confirms that person is resting or put thier phone on rest
# In[ ]:




