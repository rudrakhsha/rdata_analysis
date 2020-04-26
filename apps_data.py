#!/usr/bin/env python
# coding: utf-8

# # My First Data Science Project
# -This project revloves around finding the company's core apps, which are more used as compared to others. 
# 
# -The idea behiend this project was to analyse the available data to find the type of apps which are best suited for the people(best liked by people) and work harder towards creating those kind of apps.

# In[1]:


open_file1=open('AppleStore.csv')
from csv import reader
read_file1=reader(open_file1)
apps_data1=list(read_file1)

open_file2=open('googleplaystore.csv')
from csv import reader
read_file2=reader(open_file2)
apps_data2=list(read_file2)


# In[2]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        print('\n')
explore_data(apps_data1,1,5,True)
explore_data(apps_data2,1,5,True)




# In[3]:


print('Column Names:\nFor Applestore: ')
print(apps_data1[0])
print('\n')
print('For googleplaystore: ')
print(apps_data2[0])


# In[4]:


print(apps_data2[10473])
del apps_data2[10473]



# In[5]:


#code to find duplicate entriesin googleplaystore
unique=[]
duplicate=[]
print('finding the duplicate apps in googleplaystore')
for app in apps_data2[1:]:
    name=app[0]
    if name in unique:
        duplicate.append(name)
        
    else:
        unique.append(name)
print('No of duplicate apps',len(duplicate))
print(duplicate)

# for app in apps_data2:
#     name=app[0]
#     if name in duplicate:
        


        


# CALCULATING THE FINAL LIST AFTER REMOVING THE DUPLICATES.
# - AFTER HAVING MADE THE 2 LISTS,'unique' and 'duplicate' we'll create a dictionary 'review_max' which will help us REMOVE the duplicate apps.
# - Print the final elements in review_max and verify if it satisfies the actual no.
# - Thenafter, create 2 lists,'android_clean' and 'already_added' to store the final dataset for googleplaystore

# In[6]:


review_max={}#this will be our final list ie dictionary
for app in apps_data2[1:]:
    n_reviews=app[3]
    name=app[0]
    if name in review_max and review_max[name]<n_reviews:
        review_max[name]=n_reviews
    elif name not in review_max:
        review_max[name]=n_reviews


# In[7]:


print('expected length:',len(apps_data2[1:])-1181)
print('length obtained:',len(review_max))
print('Each dictionary key is a unique app name, and the corresponding key values will represent the highest rating for that app.')


# In[8]:


android_clean=[]
already_added=[]
for app in apps_data2[1:]:
    name=app[0]
    n_reviews=app[3]
    if n_reviews==review_max[name] and name not in already_added:
        android_clean.append(app)
        already_added.append(name)
print('Final dataset(android_clean) for googleplaystore apps contains :',len(android_clean),' rows')
    


# In[9]:


print('Cleaning out the duplicate apps from Applestore')
unique1=[]
duplicate1=[]
for app in apps_data1[1:]:
    name=app[0]
    if name in unique1:
        duplicate1.append(name)
    else:
        unique1.append(name)
print('The no of duplicate apps on the applestore are:',len(duplicate1))
print(duplicate1)
print('total no  of apps on applestore are:',len(unique1))


# In[13]:


ios_clean=[]
print(apps_data1[0])
for app in apps_data1[1:]:
    name=app[1]
    ans=non_english(name)
    if ans==True:
        ios_clean.append(app)
print('The no of apps remaining after removing non-english apps are:',len(ios_clean))
    


# In[14]:


# finding the free apps on applestore and removing the non-free from the list of lists
ios_clean2=[]

for app in ios_clean:
    price=float(app[4])#price at index 4 in applestore.csv
    
    if price==0.0:
        ios_clean2.append(app)
print('The no of apps remaining after removiing the nonfree apps is:',len(ios_clean2))


# In[15]:


def non_english(str1):
    count=0
    for character in str1:
        if ord(character)>127:
            count+=1
    if count>3:
        return False
    else:
        return True
ans=non_english(str1='Instagram')
print(ans)
print(non_english('Instachat😜'))
print(non_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))


# In[16]:


android_clean2=[]
print(android_clean[0])
for app in android_clean:
    name=app[0]
    ans=non_english(name)
    if ans==True:
        android_clean2.append(app)
print('The total no of actual english apps are...',len(android_clean2))
print(android_clean2[:5])


# In[17]:


# finding the free apps and removing the non-free from the list of lists
android_clean3=[]
print(android_clean2[:1])
for app in android_clean2:
    price=app[7]
    type=app[6]
    if price=='0' or type=='Free':
        android_clean3.append(app)
print('The no of apps remaining after removiing the nonfree apps is:',len(android_clean3))
      


# # Finding the silver space for apps.
# - Our end goal is to increase our revenues and that can be achieved if there are more apps which the people would like better and eventually end uo using it more.
# - Therefore its vital that our apps reach the maximum devices out there and for that we have to make a profile which fits both, the applestore as well as the google playstore.
# - the columns used to generate frequency tables will probably be category in which the app lies, and the genre of the app.

# In[19]:


def freq_table(dataset,index):
    freq={}
    for value in dataset:
        genre=value[index]
        if genre in freq:
            freq[genre]+=1
        else:
            freq[genre]=1
    return freq

def display_table(dataset, index):
    table = freq_table(dataset, index)
    #table is ournew dictionary which contains the freq table
    #now we convert the dictionary into tuples cuz sorted() cant sort dictionaries,but can sort tuples
    table_display=[]
    for key in table:
        key_val_as_tuple=(table[key],key)
        #append formed tuple value in the final list which we'll sort afterwards
        table_display.append(key_val_as_tuple)
    table_sorted=sorted(table_display,reverse=True)
    for value in table_sorted:
        print(value[1],':',value[0])
        
        
#print('Freq table for googlepalystore in dataset android_clean3')
#display_table(android_clean3,9)
print('Freq table for apple store')
display_table(ios_clean2,11)
#print('Freq table for google playstore based on category.')
#display_table(android_clean3,1)


# In[24]:


genre_list=freq_table(android_clean3,9)
for genre in genre_list:
    total=0
    len_genre=0
    for app in android_clean3:
        genre_app=app[9]
        if genre_app==genre:
            n_installs=app[5]
            n_installs=n_installs.replace(',','')
            n_installs=n_installs.replace('+','')
            total+=int(n_installs)
            len_genre+=1
    avg_genre=total/len_genre
    print(genre,":",avg_genre)
    



# In[27]:


# finding the avg genre for applestore
#Note: we've created a freq list first (which is in decs order of most used apps
# which will help us to find the maxm used genre in the actual dataset we have..
#i.e 'ios_clean2' or 'android_clean3' and therefore we've put that for loop inside the for loop of the list we just created
#if face any difficulty, just follos the foor loops and you'll understand the reason.
apple_genre_list=freq_table(ios_clean2,11)
for genre in apple_genre_list:
    total=0
    len_genre=0
    for app in ios_clean2:
        genre_app=app[11]
        if genre_app==genre:
            n_rating=app[5]
            total+=int(n_rating)
            len_genre+=1
    avg_genre=total/len_genre
    print(genre,":",avg_genre)
    


# In[29]:


unique_genre=freq_table(android_clean3,9)
for category in unique_genre:
    total=0
    len_category=0
    for app in android_clean3:
        genre_app=app[9]
        if category==genre_app:
            n_installs=app[5]
            n_installs=n_installs.replace('+','')
            n_installs=n_installs.replace(',','')
            total+=int(n_installs)
            len_category+=1
    avg_installs=total/len_category
    print(category,':',avg_installs)
    

