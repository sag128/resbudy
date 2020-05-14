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

test_dict=dict()



url = "https://www.zomato.com/ncr/parikrama-the-revolving-restaurant-connaught-place-new-delhi"
agent = {"User-Agent":'Chrome/61.0.3163.100'}
page = requests.get(url, headers=agent)
soup_loop=BeautifulSoup(page.content, 'lxml')
fav =soup_loop.find("div",{"class" : "fontsize13 ln18"})
fav_loop = fav.find_all("span")

for i in fav_loop:
	test=str(test+","+i.getText().strip("\n ,")).lstrip(",").lower()
	# test_dict['test']=str(''.join(i.getText().strip("\n ,")))
if 'dal' in test:

	print(test)