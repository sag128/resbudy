#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:19:09 2020

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
import re
from _thread import start_new_thread
from concurrent.futures import ThreadPoolExecutor





d={}
test={}
temp_str = str()
url_ui = 'https://www.zomato.com/jaipur/burgs-fries-mansarovar'
agent_ui = {"User-Agent":'Chrome/61.0.3163.100'}
page_ui = requests.get(url_ui, headers=agent_ui)
soup_ui=BeautifulSoup(page_ui.content, 'lxml')

name_ui=soup_ui.find("main")
name = name_ui.find("h1")
d['name']=name.getText()
d['link'] = url_ui
test['url'] = url_ui

try:
    
    cuisines = name_ui.find_all("h5")
    if cuisines:
        
        for qq in range(len(cuisines)):
            if cuisines[qq].getText() == "Cuisines":
                loop_var_cuisines = qq
                
        cuisines = cuisines[loop_var_cuisines]
        cuisines = cuisines.findNextSibling()
        cuisines= cuisines.find_all('a')
        for i in range(len(cuisines)):
            temp_str.append(cuisines[i].getText())
        d['cuisines'] = ", ".join(temp_str)
    else:
        d['cuisines'] = ''
except:
    d['cuisines'] = ''
    
 

try:
    
    address = name_ui.find("p",{"class":"sc-1hez2tp-0 clKRrC"}).getText()
    if address:
        
        d['address'] = address
    else:
        d['address'] = ''
except:
    d['address'] = ''
    



try:
    ratings = name_ui.find("article")
    if ratings:
        
        d['ratings'] = ratings.getText()
    else:
        d['ratings'] = ''
    #print(ratings.getText())    
except:
    ratings=''
    d['ratings'] = ratings
    #print(ratings)
try:
    reviews = ratings.findNextSibling()
    if reviews:
        
        d['reviews'] = reviews.getText()
    else:
        d['reviews'] = ''
    #print(reviews.getText())
except:
    reviews = ''
    d['reviews'] = reviews
    #print(reviews)
#print(url_ui)
    


try:
    
    cost_all = name_ui.findAll("p",{"color":"#4F4F4F"})
    if not cost_all:
        d['cost for 2'] = ''
        print("oooaaaa")
    else:
        
        for cst in range(len(cost_all)):
            
            if '₹' in cost_all[cst].getText() and 'pint' not in cost_all[cst].getText():
                
                
                
                cost_for_two = cost_all[cst].getText()
                
                
                cost_for_two = ''.join(re.findall(r'\d+', cost_for_two))
                d['cost for 2'] = cost_for_two
          
        else:
            fav =cost_all[0].getText()
            if fav == cost_for_two:
                test['fav'] = ''
            else:
                test['fav'] = fav
    
    
                
        
        
        
    
    
        
except :
    test['fav'] = ''
    d['cost for 2'] = ''
    print("dsfsdgfsg")
    
    
    
    
try:
    
    loc = soup_ui.find_all("script",{"data-rh":"true"})
    if loc:
        
        loc = str(loc[1]).split("{")[1]
        loc = re.findall(r'\d+\.\d+', loc)
        
    
        test['lat']=loc[0]
        test['lon']=loc[1]
    else:
        test['lat']= ''
        test['lon']  = ''
except:
    test['lat']= ''
    test['lon']  = ''
