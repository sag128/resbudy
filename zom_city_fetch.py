import collections
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import argparse

cities_list=[]
cities_link =[]
url = "https://www.zomato.com/cities"
agent = {"User-Agent":'Chrome/61.0.3163.100'}
page = requests.get(url, headers=agent)
soup=BeautifulSoup(page.content, 'lxml')



# fetch all cities for india, only india has selected class only works for india
l2=soup.find("div",{'class':'selected'})
child = l2.find_next_sibling('ul')
child2 = child.find_all("a")
print(child2[0].getText())
print(child2[0]['href'])


for ct in range(len(child)):
    cities_link.append(child2[ct]['href'])
    cities_list.append(child2[ct].getText())

    


dataframe1=pd.DataFrame({'cities':cities_list,'link':cities_link})

dataframe1.to_csv('india_cities.csv',index=False)
