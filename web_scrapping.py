#!/usr/bin/env python
# coding: utf-8

# 
# HW#1 Web Scrapping

# ## Question#1:
# ### Complete the Python program below to display the name of the most recently added dataset and collect the total number of datasets currently listed on the URL provided below.
# Note: You may need to install **cssselect** module

# In[1]:


get_ipython().system('pip install cssselect')


# In[12]:


from lxml import html
import requests
from bs4 import BeautifulSoup
url = 'http://catalog.data.gov/dataset?q=&sort=metadata_created+desc'
url2 = 'http://www.data.gov/'
r = requests.get(url)
r2 = requests.get(url2)
html_soup = BeautifulSoup(r.text, 'html.parser')
html_soup2 = BeautifulSoup(r2.text, 'html.parser')


# In[13]:


new_data_set = html_soup.find('h3', {'class':'dataset-heading'})
print(new_data_set.text, end='')


# In[5]:


from IPython.display import Image
Image('top_data_set.JPG')


# In[14]:


for item in html_soup2.find_all('div', {'class': 'text-center getstarted'}):
    item_a = item.find('a')
    item_text = item_a.get_text(strip=True) if item_a else None

print(item_text)


# In[15]:


Image('number of datasets.JPG')


# ## Question#2:
# ### Complete the Python program below to download and display the content below.

# In[17]:


url = 'https://en.wikipedia.org/robots.txt'

r3 = requests.get(url)
html_soup = BeautifulSoup(r3.text, 'html.parser')

print(html_soup)


# ## Question#3:
# ### Complete the Python program below to extract and display all the header tags from the URL below.
# Note: HTML headers are 'h1', 'h2','h3','h4','h5','h6'
# 

# In[18]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://blogs.baruch.cuny.edu/abuk/')

url = ('https://blogs.baruch.cuny.edu/abuk/')
r4 = requests.get(url)
html_soup = BeautifulSoup(r4.text, 'html.parser')


# In[19]:


for item in html_soup.find_all(['h1','h2', 'h3', 'h4', 'h5', 'h6']):
    item = str(item)
    start_tag = item[:3]
    if item[3] == '>':
        start_tag += item[3]
    else:
        try:
            indx = item.index('>')
            start_tag += item[indx]
        except ValueError:
            print("No index found for '>'")
    end_tag = item[-5:]
    print(start_tag, end_tag)


# ## Question#4:
# ### Complete the Python program below to extract and display all the image links from the URL below.
# 
# 

# In[20]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://baruch.cuny.edu/')
bs = BeautifulSoup(html, 'html.parser')


# In[21]:


for link in bs.findAll('img', attrs={'src': re.compile("^https://")}):
    print(link.get('src'))


# ## Question#5:
# ### Complete the Python program below to list all language names and number of related articles in the order they appear in the URL below
# 

# In[22]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.wikipedia.org/')
bs = BeautifulSoup(html, "html.parser")


# In[28]:


for item in bs.find_all('a', {'class': 'link-box'}):
    item_font = item.find('strong')
    num_of_articles = item.find('bdi', {'dir': 'ltr'})
    print('Language: ', item_font.text)
    print('Articles: ', num_of_articles.text, "\n")


# ## Question#6:
# ### Write a Python program to get the number of followers of a given twitter account

# In[34]:


from selenium import webdriver
url = 'https://twitter.com/hak5darren?lang=en'

driver = webdriver.Chrome()

driver.implicitly_wait(25)
driver.get(url)

followers = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div/div/div/div[1]/div[2]/div[5]/div[2]/a/span[1]/span')
print('Darren Kitchen\@hak5darren')
print('Number of followers:', followers.get_attribute('innerHTML'))
input('Press ENTER to close the automated browser')
driver.quit()


# ## Reference(s) title & URL: https://twitter.com/hak5darren?lang=en
# 

# In[ ]:




