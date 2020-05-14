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




url2 ="https://www.zomato.com/manipal/the-blind-spot-cafe-vidyaratna-nagar"
agent2 = {"User-Agent":'Chrome/61.0.3163.100'}
page = requests.get(url2, headers=agent2)
soup_loop=BeautifulSoup(page.content, 'lxml')
lat =soup_loop.find("meta",{"property" : "place:location:latitude"})
lon =soup_loop.find("meta",{"property" : "place:location:longitude"})
print(lat["content"])