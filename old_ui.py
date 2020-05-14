#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:12:52 2020

@author: sagar
"""

import collections
import pandas as pd
from multiprocessing import Pool
import threading
import requests
from bs4 import BeautifulSoup
import time
import argparse
import timeit
start_time = time.time()
import os
class Dictlist(dict):

    def __setitem__(self, key, value):

        try:
            self[key]
        except KeyError:

            super(Dictlist, self).__setitem__(key, [])

        self[key].append(value) 




test = Dictlist()








    

        
       

test1 = str()
url = 'https://www.zomato.com/allahabad/sagar-ratna-tagore-town'
agent = {"User-Agent":'Chrome/61.0.3163.100'}
page = requests.get(url, headers=agent)
soup_loop=BeautifulSoup(page.content, 'lxml')

main = soup_loop.find("div",{"class":"res-info-left col-l-11"})
try:
    
    
    test['address'] = main.find("div",{"class":"resinfo-icon"}).getText()
except:
    test['address'] = ''

try:
    cost_for_two = main.find("div",{"class":"res-info-detail"})
    test['cost_for_2'] = cost_for_two.find("span",{"tabindex":"0"}).getText()
except:
    test['cost_for_2'] = ''
        
try:
    rating = main.find("div",{"class":"col-l-4 tac left"})
    rating= rating.find("div",{"tabindex":"0"})['aria-label']
    test['rating'] = rating
except:
    
    rating=''
    test['rating'] = ''
    

try:
    reviews = main.find("div",{"class":"col-l-4 tac left"})
    reviews = reviews.find("span",{"itemprop":"ratingCount"}).getText()
    test['reviews'] = reviews
except:
    
    reviews=''
    test['reviews'] = ''
    
try:
    cuisines = main.find("div",{"class":"res-info-cuisines clearfix"}).getText()
    
    test['cuisines'] = cuisines
except:
    
    cuisines=''
    test['cuisines'] = ''

try:
    fav = main.find("div",{"class":"fontsize13 ln18"}).getText()
    fav = fav.replace("\n"," ").strip(' ')
    test['fav'] = fav
except:
    
    fav=''
    test['fav'] = ''

    





test['url'] = str(url)
try:
    lat =soup_loop.find("meta",{"property" : "place:location:latitude"})

    test['lat'] = str(lat["content"])
except:
    test['lat'] = ""


try:
    lon =soup_loop.find("meta",{"property" : "place:location:longitude"})

    test['lon'] = str(lon["content"])
except:
    test['lon'] = ""

try:
    fav =main.find("div",{"class" : "fontsize13 ln18"})
    fav_loop = fav.find_all("span")


    for i in fav_loop:

        test1=str(test1+","+i.getText().strip("\n ,")).lstrip(",").lower()
    test['fav'] = test1
    
except:
    test['fav'] = ""

