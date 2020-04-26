#!/usr/bin/env python
# coding: utf-8

# #MY Project:2
# Hacker News is a site started by the startup incubator Y Combinator, where user-submitted stories (known as "posts") are voted and commented upon, similar to reddit. Hacker News is extremely popular in technology and startup circles, and posts that make it to the top of Hacker News' listings can get hundreds of thousands of visitors as a result.

# In[1]:


from csv import reader
open_file=open('hacker_news.csv')
read_file=reader(open_file)
hn=list(read_file)
print(hn[:5])


# In[2]:


headers=hn[0]
hn=hn[1:]
print(headers)
print(hn[:5])


# In[3]:


ask_posts=[]
show_posts=[]
other_posts=[]
for row in hn:
    title=row[1]
    title=title.lower()
    if title.startswith('ask hn'):
        ask_posts.append(row)
    elif title.startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
print('ask_posts=',len(ask_posts),'show_posts=',len(show_posts),'other_posts=',len(other_posts))
print(ask_posts[0:5],show_posts[0])


# In[4]:


total_ask_comments=0
for row in ask_posts:
    
    
    total_ask_comments+=int(row[4])
avg_ask_comm=total_ask_comments/len(ask_posts)
print(avg_ask_comm)

total_show_comments=0
for row in show_posts:
    
    total_show_comments+=int(row[4])
avg_show_comments=total_show_comments/len(show_posts)
print(avg_show_comments)


# In[5]:


import datetime as dt

result_list=[]


for row in ask_posts:
    created_at=row[6]
    no_of_comm=int(row[4])
    result_list.append([created_at,no_of_comm])
#print(result_list)
counts_by_hour={}
comments_by_hour={}
date_format=("%m/%d/%Y %H:%M")
for row in result_list:
    date=row[0]
    comment=row[1]
    time=dt.datetime.strptime(date, date_format).strftime("%H")
    
    if time in counts_by_hour:
        counts_by_hour[time]+=1
        comments_by_hour[time]+=comment
    else:
        counts_by_hour[time]=1
        comments_by_hour[time]=comment

    


# In[8]:


avg_by_hour=[]
for key in comments_by_hour:
    avg_by_hour.append([key,comments_by_hour[key]/counts_by_hour[key]])
print(avg_by_hour)

    
    


# In[10]:


swap_by_hour=[]
for row in avg_by_hour:
    swap_by_hour.append([row[1],row[0]])
print(swap_by_hour)
sorted_swap=sorted(swap_by_hour,reverse=True)
print("Top 5 Hours for Ask Posts Comments")
for row in sorted_swap[:5]:
    print(row)




# In[11]:




# Sort the values and print the the 5 hours with the highest average comments.

print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


