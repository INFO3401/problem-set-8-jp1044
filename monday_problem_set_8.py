
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


df = pd.read_csv("./dd-comment-profile.csv", encoding="latin1")


# In[3]:


len(df)


# ## Problem 2

# In[4]:


def cleanhtml(df):
    df['comment_msg'] = df['comment_msg'].apply(lambda x: str(x).lstrip())
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'\r*',"", str(x)))
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'<.*?>',"",str(x)))
    
    return df
    
df = cleanhtml(df)


# ## Problem 1

# In[5]:


def cleanSpam (df):
    df['comment_msg'] = df['comment_msg'].apply(lambda x: x.lower())
    to_drop = ['app', 'free', '%20', 'check out my page', 'www.', 'http://']
    df = df[df.comment_msg.str.contains('|'.join(to_drop)) == False]
    return df

df = cleanSpam(df)


# In[6]:


len(df)


# ## Problem 3

# In[7]:


def cleanNA (df):
    df = df[df['comment_msg'] != ""]
    return df
    
df = cleanNA(df)


# In[8]:


df

