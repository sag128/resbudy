#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:22:26 2019

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
from pincode import suggest
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-ci", "--city", type=str, default="ahmedabad", nargs='+',
    help="city name eg. Ahmedabad (required)")

ap.add_argument("-rev", "--reviews", type=str, default="100",
    help="minumum reviews  eg. 100 default:100")


ap.add_argument("-rat", "--ratings", type=str, default="",
    help="minumum rating  eg. 3  default:None")


ap.add_argument("-rat_max", "--ratingsmax", type=str, default="",
    help="maximum rating  eg. 3  default:None")


ap.add_argument("-cui", "--cuisines", type=str, default="",nargs='+',
    help="particular cuisines  eg. Fast food default:None")
args = vars(ap.parse_args())

class Dictlist(dict):

    def __setitem__(self, key, value):

        try:
            self[key]
        except KeyError:

            super(Dictlist, self).__setitem__(key, [])

        self[key].append(value) 






d=Dictlist()
inp_rev = str(args['reviews'])
inp_rat = str(args['ratings'])
inp_rat_max = str(args['ratingsmax'])
test= Dictlist()
panda_dict = Dictlist()
panda_dict1 = Dictlist()
city_name = ''.join(args['city']).lower()

aa2=[]
final_url = []
url_less_than_2 =[]
branch_dict = {}   


url = "https://www.zomato.com/"+city_name+"/restaurants?sort=best&page="
print(city_name)
if(city_name == "delhi"):

    city_name = "ncr"
    url = "https://www.zomato.com/"+city_name+"/restaurants?sort=best&page="

if( city_name == "gurgaon" or city_name == "noida" or city_name == "faridabad" or city_name == "ghaziabad" ):


    url = "https://www.zomato.com/ncr/restaurants/"+city_name+"?sort=best&page="
    print(url)
if( city_name == "bangalore" or city_name == "banglore"):
        
    url= "https://www.zomato.com/bangalore/restaurants/?sort=best&page="
    print(url)
else:
        
    url = "https://www.zomato.com/"+city_name+"/restaurants?sort=best&page="
        
       



agent = {"User-Agent":'Chrome/77.0.3865.90'}
page = requests.get(url, headers=agent)
soup=BeautifulSoup(page.content, 'lxml')

l2=len(soup.find_all("div",{'class':'col-l-4 mtop pagination-number'}))

page=soup.find_all("div",{'class':'col-l-4 mtop pagination-number'})

aa=int(str(list(page[0])).split("<b>")[-1].split("<")[0])
res_len=int()


url_more_than_2 = []
def final_page(start,stop,city_name2):
    

    for i in range(start,stop):
            
        
            url = 'https://www.zomato.com/'+city_name2+'/restaurants?sort=best&page='+str(i)
            agent = {"User-Agent":'Chrome/77.0.3865.90'}
            page = requests.get(url, headers=agent)
            soup=BeautifulSoup(page.content, 'lxml')
            for_page=soup.find_all("div",{'class':'card search-snippet-card search-card'})

            try:
                if "flex align-center both-rating" not in str(for_page) and "single-rating flex" not in str(for_page):
                    
                    aa2.append(i)
                    break                
            except :
                print("pass")
                    

    
    #for j in range(len(test)):
        
     #   d2['ratings'] = test[j].getText().split()[0]
        
if os.path.exists(city_name+'.csv') == True or os.path.exists(city_name+'lat_lon'+'.csv') == True:
        print("no pages")
        

else:

   
    threads3=list()
    t = threading.Thread(target=final_page, args=(1,aa//25,city_name) , name="1")
    threads3.append(t)
    t.start()

    t2 = threading.Thread(target=final_page, args=(aa//25,(aa//25)*2,city_name), name="2")
    threads3.append(t2)
    t2.start()

    t3 = threading.Thread(target=final_page, args=((aa//25)*2,(aa//25)*3,city_name), name="3")
    threads3.append(t3)
    t3.start()

    t4 = threading.Thread(target=final_page, args=((aa//25)*3,(aa//25)*4,city_name), name="4")
    threads3.append(t4)
    t4.start()

    t5 = threading.Thread(target=final_page, args=((aa//25)*4,(aa//25)*5,city_name), name="5")
    threads3.append(t5)
    t5.start()


    t6 = threading.Thread(target=final_page, args=((aa//25)*5,(aa//25)*6,city_name), name="6")
    threads3.append(t6)
    t6.start()

    t7 = threading.Thread(target=final_page, args=((aa//25)*6,(aa//25)*7,city_name), name="7")
    threads3.append(t7)
    t7.start()

    t8 = threading.Thread(target=final_page, args=((aa//25)*7,(aa//25)*8,city_name), name="8")
    threads3.append(t8)
    t8.start()

    t9 = threading.Thread(target=final_page, args=((aa//25)*8,(aa//25)*9,city_name), name="9")
    threads3.append(t9)
    t9.start()

    t10 = threading.Thread(target=final_page, args=((aa//25)*9,(aa//25)*10,city_name), name="10")
    threads3.append(t10)
    t10.start()


    t11 = threading.Thread(target=final_page, args=((aa//25)*10,(aa//25)*11,city_name), name="11")
    threads3.append(t11)
    t11.start()

    t12 = threading.Thread(target=final_page, args=((aa//25)*11,(aa//25)*12,city_name), name="12")
    threads3.append(t12)
    t12.start()

    t13 = threading.Thread(target=final_page, args=((aa//25)*12,(aa//25)*13,city_name), name="13")
    threads3.append(t13)
    t13.start()

    t14 = threading.Thread(target=final_page, args=((aa//25)*13,(aa//25)*14,city_name), name="14")
    threads3.append(t14)
    t14.start()

    t15 = threading.Thread(target= final_page, args=((aa//25)*14,(aa//25)*15,city_name), name="15")
    threads3.append(t15)
    t15.start()


    t16 = threading.Thread(target=final_page, args=((aa//25)*15,(aa//25)*16,city_name), name="16")
    threads3.append(t16)
    t16.start()

    t17 = threading.Thread(target=final_page, args=((aa//25)*16,(aa//25)*17,city_name), name="17")
    threads3.append(t17)
    t17.start()

    t18 = threading.Thread(target=final_page, args=((aa//25)*17,(aa//25)*18,city_name), name="18")
    threads3.append(t18)
    t18.start()

    t19 = threading.Thread(target=final_page, args=((aa//25)*18,(aa//25)*19,city_name), name="19")
    threads3.append(t19)
    t19.start()

    t20 = threading.Thread(target=final_page, args=((aa//25)*19,(aa//25)*20,city_name), name="20")
    threads3.append(t20)
    t20.start()

    t21 = threading.Thread(target=final_page, args=((aa//25)*20,(aa//25)*21,city_name), name="21")
    threads3.append(t21)
    t21.start()

    t22 = threading.Thread(target=final_page, args=((aa//25)*21,(aa//25)*22,city_name), name="22")
    threads3.append(t22)
    t22.start()

    t23 = threading.Thread(target=final_page, args=((aa//25)*22,(aa//25)*23,city_name), name="23")
    threads3.append(t23)
    t23.start()

    t24 = threading.Thread(target=final_page, args=((aa//25)*23,(aa//25)*24,city_name), name="24")
    threads3.append(t24)
    t24.start()

    t25 = threading.Thread(target=final_page, args=((aa//25)*24,aa+1,city_name), name="25")
    threads3.append(t25)
    t25.start()




    # t20 = threading.Thread(target=zomato, args=((aa//26)*20,aa+1,city_name))
    # threads1.append(t20)
    # t20.start()




    t.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()


    aa2 = sorted(aa2)
    aa_final = aa2[0]
    print(aa_final)






#fn for scraping all urls from a city

# def zomato_url(start,stop,city_name):
    
#     for i in range(start,stop):
        
    
#         url = 'https://www.zomato.com/'+city_name+'/restaurants?sort=best&page='+str(i)
#         agent = {"User-Agent":'Chrome/77.0.3865.90'}
#         page = requests.get(url, headers=agent)
#         soup=BeautifulSoup(page.content, 'lxml')
        
#         #l2=soup.find_all("div",{'class':'ui col-l-16 fontsize5 grey-text'})
#         #l3 = soup.find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})
        
        
#         parent = soup.find_all("div",{"class":"card search-snippet-card search-card"})
        
        
        
        
#         for i in range(len(parent)):
#             final_url.append(parent[i].find("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})['href'])
#             if parent[i].find("a",{"class":"ui ta-right pt10 fontsize3 zred pb10 pr10"}):
                
#                 url_more_than_2.append('http://www.zomato.com'+str(parent[i].find_all("a",{"class":"ui ta-right pt10 fontsize3 zred pb10 pr10"})[0]['href']))
                
#             else:
#                 if len(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})) == 1:
                    
                    

#                     url_less_than_2.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[0]['href'])
                    
#                 if len(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})) == 2:
                    
#                     url_less_than_2.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[0]['href'])
#                     url_less_than_2.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[1]['href'])
                    
    
    #for i2 in range(len(html_less_than_2)):
        
    
     #   for i3 in range(len(html_less_than_2[i2])):
            
      #      url_less_than_2.append(html_less_than_2[i2][i3]['href'])
    
    
#for getting all restaurants from list - url_more_than_2


#for total number of branches
#for i in range(len(l2)):
 #   tot.extend(re.findall(r'\b\d+\b',l2[i].getText()) )
    
#if total branches are less than or equal to 2

# threads4=list()
# t = threading.Thread(target=zomato_url, args=(1,aa_final//25,city_name) , name="1")
# threads4.append(t)
# t.start()

# t2 = threading.Thread(target=zomato_url, args=(aa_final//25,(aa_final//25)*2,city_name), name="2")
# threads4.append(t2)
# t2.start()

# t3 = threading.Thread(target=zomato_url, args=((aa_final//25)*2,(aa_final//25)*3,city_name), name="3")
# threads4.append(t3)
# t3.start()

# t4 = threading.Thread(target=zomato_url, args=((aa_final//25)*3,(aa_final//25)*4,city_name), name="4")
# threads4.append(t4)
# t4.start()

# t5 = threading.Thread(target=zomato_url, args=((aa_final//25)*4,(aa_final//25)*5,city_name), name="5")
# threads4.append(t5)
# t5.start()


# t6 = threading.Thread(target=zomato_url, args=((aa_final//25)*5,(aa_final//25)*6,city_name), name="6")
# threads4.append(t6)
# t6.start()

# t7 = threading.Thread(target=zomato_url, args=((aa_final//25)*6,(aa_final//25)*7,city_name), name="7")
# threads4.append(t7)
# t7.start()

# t8 = threading.Thread(target=zomato_url, args=((aa_final//25)*7,(aa_final//25)*8,city_name), name="8")
# threads4.append(t8)
# t8.start()

# t9 = threading.Thread(target=zomato_url, args=((aa_final//25)*8,(aa_final//25)*9,city_name), name="9")
# threads4.append(t9)
# t9.start()

# t10 = threading.Thread(target=zomato_url, args=((aa_final//25)*9,(aa_final//25)*10,city_name), name="10")
# threads4.append(t10)
# t10.start()


# t11 = threading.Thread(target=zomato_url, args=((aa_final//25)*10,(aa_final//25)*11,city_name), name="11")
# threads4.append(t11)
# t11.start()

# t12 = threading.Thread(target=zomato_url, args=((aa_final//25)*11,(aa_final//25)*12,city_name), name="12")
# threads4.append(t12)
# t12.start()

# t13 = threading.Thread(target=zomato_url, args=((aa_final//25)*12,(aa_final//25)*13,city_name), name="13")
# threads4.append(t13)
# t13.start()

# t14 = threading.Thread(target=zomato_url, args=((aa_final//25)*13,(aa_final//25)*14,city_name), name="14")
# threads4.append(t14)
# t14.start()

# t15 = threading.Thread(target=zomato_url, args=((aa_final//25)*14,(aa_final//25)*15,city_name), name="15")
# threads4.append(t15)
# t15.start()


# t16 = threading.Thread(target=zomato_url, args=((aa_final//25)*15,(aa_final//25)*16,city_name), name="16")
# threads4.append(t16)
# t16.start()

# t17 = threading.Thread(target=zomato_url, args=((aa_final//25)*16,(aa_final//25)*17,city_name), name="17")
# threads4.append(t17)
# t17.start()

# t18 = threading.Thread(target=zomato_url, args=((aa_final//25)*17,(aa_final//25)*18,city_name), name="18")
# threads4.append(t18)
# t18.start()

# t19 = threading.Thread(target=zomato_url, args=((aa_final//25)*18,(aa_final//25)*19,city_name), name="19")
# threads4.append(t19)
# t19.start()

# t20 = threading.Thread(target=zomato_url, args=((aa_final//25)*19,(aa_final//25)*20,city_name), name="20")
# threads4.append(t20)
# t20.start()

# t21 = threading.Thread(target=zomato_url, args=((aa_final//25)*20,(aa_final//25)*21,city_name), name="21")
# threads4.append(t21)
# t21.start()

# t22 = threading.Thread(target=zomato_url, args=((aa_final//25)*21,(aa_final//25)*22,city_name), name="22")
# threads4.append(t22)
# t22.start()

# t23 = threading.Thread(target=zomato_url, args=((aa_final//25)*22,(aa_final//25)*23,city_name), name="23")
# threads4.append(t23)
# t23.start()

# t24 = threading.Thread(target=zomato_url, args=((aa_final//25)*23,(aa_final//25)*24,city_name), name="24")
# threads4.append(t24)
# t24.start()

# t25 = threading.Thread(target=zomato_url, args=((aa_final//25)*24,aa_final+1,city_name), name="25")
# threads4.append(t25)
# t25.start()




# # t20 = threading.Thread(target=zomato, args=((aa//26)*20,aa+1,city_name))
# # threads1.append(t20)
# # t20.start()


    

# t.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
# t10.join()
# t11.join()
# t12.join()
# t13.join()
# t14.join()
# t15.join()
# t16.join()
# t17.join()
# t18.join()
# t19.join()
# t20.join()
# t21.join()
# t22.join()
# t23.join()
# t24.join()
# t25.join()



def zomato(start,stop,city_name):
    
    
    for jj in range(start,stop):
        
        url = "https://www.zomato.com/"+city_name+"/restaurants?sort=best&page="+str(jj)
        total=[]
        agent = {"User-Agent":'Chrome/77.0.3865.90'}
        page = requests.get(url, headers=agent)
        soup=BeautifulSoup(page.content, 'lxml')
        
        length=len(soup.find_all("div",{'class':'card search-snippet-card search-card'}))
        all_res=soup.find_all("div",{'class':'card search-snippet-card search-card'})
        soup2=soup.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
        ratings_len = len(soup.find_all("div",{"class":"flex align-center both-rating"}))
        ratings_both = soup.find_all("div",{"class":"flex align-center both-rating"})
        cost_for_2 = soup.find_all("span",{"class":"col-s-11 col-m-12 pl0"})
        ratings_color = soup.find_all("div",{"class":"single-rating flex"})
        
        cuisines = soup.find_all("span",{"class":"col-s-11 col-m-12 nowrap pl0"})
        address = soup.find_all("div",{"class":"col-m-16 search-result-address grey-text nowrap ln22"})
        #lat =soup.find("meta",{"property" : "place:location:latitude"})
        #lon =soup.find("meta",{"property" : "place:location:longitude"})
        #print(lat['content'])
        #print(lon['content'])
        
        
        
        
        parent = soup.find_all("div",{"class":"card search-snippet-card search-card"})
        
        
        
        
        for i in range(len(parent)):
            
            final_url.append(parent[i].find("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})['href'])
            if parent[i].find("a",{"class":"ui ta-right pt10 fontsize3 zred pb10 pr10"}):
                
                url_more_than_2.append('http://www.zomato.com'+str(parent[i].find_all("a",{"class":"ui ta-right pt10 fontsize3 zred pb10 pr10"})[0]['href']))
                
            else:
                if len(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})) == 1:
                    
                    
        
                    url_less_than_2.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[0]['href'])
                    
                if len(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})) == 2:
                    
                    url_less_than_2.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[0]['href'])
                    url_less_than_2.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[1]['href'])
        
        
        
        
                    
            
        
            
        for tt in range(length):
                
                d['name'] = soup2[tt]['title']
                d['link'] = soup2[tt]['href']
                
                try:
                    
                    if all_res[tt].find("div",{"class":"flex align-center both-rating"}) != None:
                        both = all_res[tt].find("div",{"class":"flex align-center both-rating"})
                        total_rat_rev=[i for i in re.split("[|() \n]",both.getText()) if i]
                        total.append(total_rat_rev)                
                        if ',' in  total_rat_rev[1]:
                            total_rat_rev[1]=total_rat_rev[1].replace(',','')
                        if ',' in  total_rat_rev[3]:    
                            total_rat_rev[3] = total_rat_rev[3].replace(',','')
                        if 'K' in  total_rat_rev[1]:
                            total_rat_rev[1]=total_rat_rev[1].replace('.','').strip().replace('K','00')
                        if 'K' in  total_rat_rev[3]:
                            total_rat_rev[3]=total_rat_rev[3].replace('.','').strip().replace('K','00')
                        if 'K' in  total_rat_rev[1]:
                            total_rat_rev[1]=total_rat_rev[1].replace('K','000').strip()
                        if 'K' in  total_rat_rev[3]:
                            total_rat_rev[3]=total_rat_rev[3].replace('K','000').strip()
                
                
                        
                        
                        
                        d['ratings'] = (float(total_rat_rev[0]) + float(total_rat_rev[2]))/2
                        d['ratings_dining'] = total_rat_rev[0]
                        d['ratings_delivery'] = total_rat_rev[2]
                        d['reviews_dining'] = total_rat_rev[1]
                        d['reviews_delivery'] = total_rat_rev[3]
                        d['reviews'] = (int(total_rat_rev[1]) + int(total_rat_rev[3]))//2
                
                            
                    elif all_res[tt].find("div",{"class":"flex align-center both-rating"}) == None:
                    
                        single = all_res[tt].find("div",{"class":"single-rating flex"})
                    
                        if '#1C1C1C' in str(single):
                            
                            dining = single
                            
                            for_k=dining.find("span",{"class":"review-count medium"}).getText()
                            k_var=re.sub('[Reviews()]','',dining.find("span",{"class":"review-count medium"}).getText()).strip()
                            if 'K' in k_var:
                                k_var= k_var.replace('.','').strip().replace('K','00').strip()
                                d['reviews_dining'] = k_var
                                d['reviews'] = k_var
                                d['reviews_delivery'] =''
                            
                                
                            else:
                                rev_dining = ''.join(re.findall('\d+',dining.find("span",{"class":"review-count medium"}).getText()))
                                d['reviews_dining'] = rev_dining
                                d['reviews'] = rev_dining
                                d['reviews_delivery'] =''
                             
                                
                        
                        
                            rat_dining=''.join(re.findall('\d.+',dining.find("span",{"class":"rating-value"}).getText()))
                            d['ratings_dining']= rat_dining
                            d['ratings'] = rat_dining
                            d['ratings_delivery'] = ''
                            
                            
                            
                    
                            
                                
                        
                        elif '#E23744' in str(single):
                            
                            delivery = single
                            
                        
                            
                    
                            for_k=ratings_color[1].find("span",{"class":"review-count medium"}).getText()
                            k_var=re.sub('[Reviews()]','',delivery.find("span",{"class":"review-count medium"}).getText()).strip()
                            if 'K' in k_var:
                            
                                k_var= k_var.replace('.','').strip().replace('K','00').strip()
                                d['reviews_delivery'] = k_var
                                d['reviews'] = k_var
                                d['reviews_dining']=''
                                
                                
                            
                            else:
                                
                                rev_delivery=''.join(re.findall('\d+',delivery.find("span",{"class":"review-count medium"}).getText()))
                
                                d['reviews_delivery'] = rev_delivery
                                d['reviews'] = rev_delivery
                                d['reviews_dining']=''
                                
                                
                                
                            
                        
                            
                        
                            rat_delivery=''.join(re.findall('\d.+',delivery.find("span",{"class":"rating-value"}).getText()))
                            d['ratings_delivery']=rat_delivery
                            d['ratings'] = rat_delivery
                            d['ratings_dining']=''

                            
                        
                            
                        else:
                            d['ratings']=''
                            d['ratings_delivery']=''
                            d['ratings_dining']=''
                            d['reviews']=''
                            d['reviews_delivery']=''
                            d['reviews_dining']=''
                        
                    
                
                except:
                    
                    d['ratings']=''
                    d['ratings_delivery']=''
                    d['ratings_dining']=''
                    d['reviews']=''
                    d['reviews_delivery']=''
                    d['reviews_dining']=''
                
                try:
                    if not cost_for_2:
                        
                        d['cost for 2'] = ""
                    else:
                        d['cost for 2'] = cost_for_2[tt].getText()[1:]
                except IndexError  :
        
                    d['cost for 2'] = ""
                    
        
                try:
        
                    d['cuisines'] = cuisines[tt].getText()
                except:
                    d['cuisines'] = ""
        
                try:
        
                    d['address'] = address[tt].getText()
                except:
                    d['address'] = ""




def more_than_2(start,stop):
    
    
           
    
    
    for jo in range(start,stop):
            url2 = url_more_than_2[jo]
            agent2 = {"User-Agent":'Chrome/77.0.3865.90'}
            page2 = requests.get(url2, headers=agent2)
            soup2=BeautifulSoup(page2.content, 'lxml')
            
            page3=soup2.find_all("div",{'class':'col-l-4 mtop pagination-number'})
            
            pg=int(str(list(page3[0])).split("<b>")[-1].split("<")[0])
            
            for io in range(1,pg+1):
                url3 = url2+ '&page='+str(io)
                agent3 = {"User-Agent":'Chrome/77.0.3865.90'}
                page33 = requests.get(url3, headers=agent3)
                soup33=BeautifulSoup(page33.content, 'lxml')
                
                length=soup33.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
                
                for tt in range(len(length)):
                    
                    url_less_than_2.append(length[tt]['href'])
    



       
                
def zomato_child(url_param,start,stop):
    
        
    for j in range(start,stop):

        url3 = url_param+ '&page='+str(j)
        agent3 = {"User-Agent":'Chrome/77.0.3865.90'}
        page33 = requests.get(url3, headers=agent3)
        soup33=BeautifulSoup(page33.content, 'lxml')
        
        length=soup33.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
        soup2=soup33.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
        
        ratings = soup33.find_all("div",{"class":"ta-right floating search_result_rating col-s-4 clearfix"})
        cost_for_2 = soup33.find_all("span",{"class":"col-s-11 col-m-12 pl0"})
        
        
        cuisines = soup33.find_all("span",{"class":"col-s-11 col-m-12 nowrap pl0"})
        address = soup33.find_all("div",{"class":"col-m-16 search-result-address grey-text nowrap ln22"})
        #lat =soup.find("meta",{"property" : "place:location:latitude"})
        #lon =soup.find("meta",{"property" : "place:location:longitude"})
        #print(lat['content'])
        #print(lon['content'])
        
        
            
        for tt in range(len(length)):
            final_url.append(length[tt]['href'])

            #if  list(ratings[tt].getText().split())[0] != "NEW":
                
             #   print(list(ratings[tt].getText().split())[0])
            

            d['name'] = soup2[tt]['title']
            d['link'] = soup2[tt]['href']
                
            try:

                d['cost for 2'] = cost_for_2[tt].getText()[1:]
            except :
                

                d['cost for 2'] = ""

            try:

                d['cuisines'] = cuisines[tt].getText()
            except:
                d['cuisines'] = ""

            try:

                d['ratings'] = (list(ratings[tt].getText().split())[0])
            except:

                d['ratings'] = ""
            try:
                d['reviews'] = (list(ratings[tt].getText().split())[1])
            except:
                d['reviews'] = ""



            try:

                d['address'] = address[tt].getText()
            except:
                d['address'] = ""

    
    
    
    #for getting all info of branch restaurants

      
    
    
    #    for i2 in range(1,branch_dict[i]+1):
            
            
            
            #url_loop = str(i) + '&page='+str(i2)
            #agent_loop = {"User-Agent":'Chrome/77.0.3865.90'}
            #page = requests.get(url_loop, headers=agent_loop)
            #soup_loop2=BeautifulSoup(page.content, 'lxml')
        
            #length_res_name=len(soup_loop2.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'}))
            #soup_find=soup_loop2.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
            #ratings_len = len(soup_loop2.find_all("div",{"class":"ta-right floating search_result_rating col-s-4 clearfix"}))
            #ratings = soup_loop2.find_all("div",{"class":"ta-right floating search_result_rating col-s-4 clearfix"})
            #cost_for_2 = soup.find_all("span",{"class":"col-s-11 col-m-12 pl0"})
        
        
            #cuisines = soup.find_all("span",{"class":"col-s-11 col-m-12 nowrap pl0"})
            #address = soup.find_all("div",{"class":"col-m-16 search-result-address grey-text nowrap ln22"})
            
            #print(length_res_name,url_loop,ratings_len,ratings[0])
    
 

#threads11 = []
#for n in range(len(branch_dict)):
    
 #   t111 = threading.Thread(target=zomato_child, args=(url_more_than_2[n],1,int(branch_dict[url_more_than_2[n]])))
  #  t111.start()
   # threads11.append(t111)

# # Wait all threads to finish.
#for t111 in threads11:
 #   t111.join()








                





def lat_lon(start,stop):

    for l in range(start,stop):

        url = d['link'][l]
        agent = {"User-Agent":'Chrome/77.0.3865.90'}
        page = requests.get(url, headers=agent)
        soup_loop=BeautifulSoup(page.content, 'lxml')
        
        try:
            cost_all=soup_loop.find_all("h5")
            if  'Top Dishes' in str(cost_all) and 'Average' in str(cost_all):
        
                for cst in range(len(cost_all)):
            
                    if 'Top Dishes' in cost_all[cst].getText():
                        
                        test['fav']=cost_all[cst].findNext("p").getText()
                        
                
                        
                        
                    
                    if 'Average' in cost_all[cst].getText():
                        
                        cost_for_2=cost_all[cst].findNext("p").getText()
                        # d['cost for 2']=''.join(re.findall(r'\d+', cost_for_2))
                        
                        
                        
            elif cost_all and  'Average' in str(cost_all):
                for cst in range(len(cost_all)):
                    
                    if 'Average' in cost_all[cst].getText():
                        
                        cost_for_2=cost_all[cst].findNext("p").getText()
                        
                        # test['cost for 2']=''.join(re.findall(r'\d+', cost_for_2))
                        test['fav'] =''
                        
            
            
            
            elif cost_all and  'Top Dishes' in str(cost_all):
                for cst in range(len(cost_all)):
                    
                    
                    if 'Top Dishes' in cost_all[cst].getText():
                        
                        test['fav']=cost_all[cst].findNext("p").getText()
                        
                        # test['cost for 2'] = ''
            else:
                #test['cost for 2'] = ''
                test['fav'] =''
                
        except:
            # d['cost for 2'] = '' 
            test['fav'] = ''
   
        try:
            
            loc = soup_loop.find_all("script",{"data-rh":"true"})
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
        

        test['url'] = str(url)




        
if os.path.exists(city_name+'.csv') == True:
        print("from here")
        retrieve = pd.read_csv(city_name+'.csv')
        for l in range(len(retrieve['ratings'])):
            panda_dict['link'] = str(retrieve['link'][l])
            panda_dict['ratings'] = str(retrieve['ratings'][l])
            panda_dict['reviews'] = str(retrieve['reviews'][l])
            panda_dict['name'] = str(retrieve['name'][l])
            panda_dict['address'] = str(retrieve['address'][l]).strip()
            panda_dict['cost for 2'] = str(retrieve['cost for 2'][l])
            # panda_dict['lat'] = str(retrieve['lat'][l])
            # panda_dict['lon'] = str(retrieve['lon'][l])
            panda_dict['cuisines'] = str(retrieve['cuisines'][l])
            
            
        test_df_list = pd.DataFrame(panda_dict)


else:
    
    
    
    
    threads1=list()
    t = threading.Thread(target=zomato, args=(1,aa_final//25,city_name) , name="1")
    threads1.append(t)
    t.start()

    t2 = threading.Thread(target=zomato, args=(aa_final//25,(aa_final//25)*2,city_name), name="2")
    threads1.append(t2)
    t2.start()

    t3 = threading.Thread(target=zomato, args=((aa_final//25)*2,(aa_final//25)*3,city_name), name="3")
    threads1.append(t3)
    t3.start()

    t4 = threading.Thread(target=zomato, args=((aa_final//25)*3,(aa_final//25)*4,city_name), name="4")
    threads1.append(t4)
    t4.start()

    t5 = threading.Thread(target=zomato, args=((aa_final//25)*4,(aa_final//25)*5,city_name), name="5")
    threads1.append(t5)
    t5.start()


    t6 = threading.Thread(target=zomato, args=((aa_final//25)*5,(aa_final//25)*6,city_name), name="6")
    threads1.append(t6)
    t6.start()

    t7 = threading.Thread(target=zomato, args=((aa_final//25)*6,(aa_final//25)*7,city_name), name="7")
    threads1.append(t7)
    t7.start()

    t8 = threading.Thread(target=zomato, args=((aa_final//25)*7,(aa_final//25)*8,city_name), name="8")
    threads1.append(t8)
    t8.start()

    t9 = threading.Thread(target=zomato, args=((aa_final//25)*8,(aa_final//25)*9,city_name), name="9")
    threads1.append(t9)
    t9.start()

    t10 = threading.Thread(target=zomato, args=((aa_final//25)*9,(aa_final//25)*10,city_name), name="10")
    threads1.append(t10)
    t10.start()


    t11 = threading.Thread(target=zomato, args=((aa_final//25)*10,(aa_final//25)*11,city_name), name="11")
    threads1.append(t11)
    t11.start()

    t12 = threading.Thread(target=zomato, args=((aa_final//25)*11,(aa_final//25)*12,city_name), name="12")
    threads1.append(t12)
    t12.start()

    t13 = threading.Thread(target=zomato, args=((aa_final//25)*12,(aa_final//25)*13,city_name), name="13")
    threads1.append(t13)
    t13.start()

    t14 = threading.Thread(target=zomato, args=((aa_final//25)*13,(aa_final//25)*14,city_name), name="14")
    threads1.append(t14)
    t14.start()

    t15 = threading.Thread(target=zomato, args=((aa_final//25)*14,(aa_final//25)*15,city_name), name="15")
    threads1.append(t15)
    t15.start()


    t16 = threading.Thread(target=zomato, args=((aa_final//25)*15,(aa_final//25)*16,city_name), name="16")
    threads1.append(t16)
    t16.start()

    t17 = threading.Thread(target=zomato, args=((aa_final//25)*16,(aa_final//25)*17,city_name), name="17")
    threads1.append(t17)
    t17.start()

    t18 = threading.Thread(target=zomato, args=((aa_final//25)*17,(aa_final//25)*18,city_name), name="18")
    threads1.append(t18)
    t18.start()

    t19 = threading.Thread(target=zomato, args=((aa_final//25)*18,(aa_final//25)*19,city_name), name="19")
    threads1.append(t19)
    t19.start()

    t20 = threading.Thread(target=zomato, args=((aa_final//25)*19,(aa_final//25)*20,city_name), name="20")
    threads1.append(t20)
    t20.start()

    t21 = threading.Thread(target=zomato, args=((aa_final//25)*20,(aa_final//25)*21,city_name), name="21")
    threads1.append(t21)
    t21.start()
    
    t22 = threading.Thread(target=zomato, args=((aa_final//25)*21,(aa_final//25)*22,city_name), name="22")
    threads1.append(t22)
    t22.start()
    
    t23 = threading.Thread(target=zomato, args=((aa_final//25)*22,(aa_final//25)*23,city_name), name="23")
    threads1.append(t23)
    t23.start()
    
    t24 = threading.Thread(target=zomato, args=((aa_final//25)*23,(aa_final//25)*24,city_name), name="24")
    threads1.append(t24)
    t24.start()
    
    t25 = threading.Thread(target=zomato, args=((aa_final//25)*24,aa_final,city_name), name="25")
    threads1.append(t25)
    t25.start()
    
    url_more_than_2 = list(set(url_more_than_2))
    length_more = len(url_more_than_2)
    
        
    threads_more=list()
    x = threading.Thread(target=more_than_2, args=(0,length_more//26))
    threads_more.append(x)
    x.start()
    
    x2 = threading.Thread(target=more_than_2, args=(length_more//26,(length_more//26)*2))
    threads_more.append(x2)
    x2.start()
    
    x3 = threading.Thread(target=more_than_2, args=((length_more//26)*2,(length_more//26)*3))
    threads_more.append(x3)
    x3.start()
    
    x4 = threading.Thread(target=more_than_2, args=((length_more//26)*3,(length_more//26)*4))
    threads_more.append(x4)
    x4.start()
    
    x5 = threading.Thread(target=more_than_2, args=((length_more//26)*4,(length_more//26)*5))
    threads_more.append(x5)
    x5.start()
    
    
    x6 = threading.Thread(target=more_than_2, args=((length_more//26)*5,(length_more//26)*6))
    threads_more.append(x6)
    x6.start()
    
    x7 = threading.Thread(target=more_than_2, args=((length_more//26)*6,(length_more//26)*7))
    threads_more.append(x7)
    x7.start()
    
    x8 = threading.Thread(target=more_than_2, args=((length_more//26)*7,(length_more//26)*8))
    threads_more.append(x8)
    x8.start()
    
    x9 = threading.Thread(target=more_than_2, args=((length_more//26)*8,(length_more//26)*9))
    threads_more.append(x9)
    x9.start()
    
    x10 = threading.Thread(target=more_than_2, args=((length_more//26)*9,(length_more//26)*10))
    threads_more.append(x10)
    x10.start()
    
    
    x11 = threading.Thread(target=more_than_2, args=((length_more//26)*10,(length_more//26)*11))
    threads_more.append(x11)
    x11.start()
    
    x12 = threading.Thread(target=more_than_2, args=((length_more//26)*11,(length_more//26)*12))
    threads_more.append(x12)
    x12.start()
    
    x13 = threading.Thread(target=more_than_2, args=((length_more//26)*12,(length_more//26)*13))
    threads_more.append(x13)
    x13.start()
    
    x14 = threading.Thread(target=more_than_2, args=((length_more//26)*13,(length_more//26)*14))
    threads_more.append(x14)
    x14.start()
    
    x15 = threading.Thread(target=more_than_2, args=((length_more//26)*14,(length_more//26)*15))
    threads_more.append(x15)
    x15.start()
    
    
    x16 = threading.Thread(target=more_than_2, args=((length_more//26)*15,(length_more//26)*16))
    threads_more.append(x16)
    x16.start()
    
    x17a = threading.Thread(target=more_than_2, args=((length_more//26)*16,(length_more//26)*17))
    threads_more.append(x17a)
    x17a.start()
    
    x17 = threading.Thread(target=more_than_2, args=((length_more//26)*17,(length_more//26)*18))
    threads_more.append(x17)
    x17.start()
    
    x18 = threading.Thread(target=more_than_2, args=((length_more//26)*18,(length_more//26)*19))
    threads_more.append(x18)
    x18.start()
    
    x19 = threading.Thread(target=more_than_2, args=((length_more//26)*19,(length_more//26)*20))
    threads_more.append(x19)
    x19.start()
    
    
    x20 = threading.Thread(target=more_than_2, args=((length_more//26)*20,(length_more//26)*21))
    threads_more.append(x20)
    x20.start()
    
    
    x21 = threading.Thread(target=more_than_2, args=((length_more//26)*21,(length_more//26)*22))
    threads_more.append(x21)
    x21.start()
    
    x22 = threading.Thread(target=more_than_2, args=((length_more//26)*22,(length_more//26)*23))
    threads_more.append(x22)
    x22.start()
    
    x23 = threading.Thread(target=more_than_2, args=((length_more//26)*23,(length_more//26)*24))
    threads_more.append(x23)
    x23.start()
    
    x24 = threading.Thread(target=more_than_2, args=((length_more//26)*24,(length_more//26)*25))
    threads_more.append(x24)
    x24.start()
    
    x25 = threading.Thread(target=more_than_2, args=((length_more//26)*25,(length_more//26)*26))
    threads_more.append(x25)
    x25.start()
    
    
    x26 = threading.Thread(target=more_than_2, args=((length_more//26)*26,length_more))
    threads_more.append(x26)
    x26.start()
    
    



    # t20 = threading.Thread(target=zomato, args=((aa//26)*20,aa+1,city_name))
    # threads1.append(t20)
    # t20.start()


    
    
    t.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    
    
    
    
    x.join()
    x2.join()
    x3.join()
    x4.join()
    x5.join()
    x6.join()
    x7.join()
    x8.join()
    x9.join()
    x10.join()
    x11.join()
    x12.join()
    x13.join()
    x14.join()
    x15.join()
    x16.join()
    x17.join()
    x17a.join()
    x18.join()
    x19.join()
    x20.join()
    x21.join()
    x22.join()
    x23.join()
    x24.join()
    x25.join()
    x26.join()
    
    
    
    
  
    
def fetch_less_than_2(start,stop,unique_list):
    
    for u in range(start,stop):
        
        
    
        temp_str=[]
        
        url_ui = unique_list[u]
        agent_ui = {"User-Agent":'Chrome/77.0.3865.90'}
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
            
            all_rev = soup_ui.find_all("p",{"class":re.compile("sc-1hez2tp-0 lhdg1m-7.*")})
            all_rat = soup_ui.find_all("section",{"class":re.compile("lhdg1m-0 eVTFyk.*")})
            
            if len(all_rev) == 2:
                dining = ''.join(re.findall('[\d K]',all_rev[0].getText())).strip()
                delivery= ''.join(re.findall('[\d K]',all_rev[1].getText())).strip()
                if ',' in  dining:
                        dining=dining.replace(',','')
                if 'K' in  dining:
                    dining=dining.replace('.','').strip().replace('K','00')
                if 'K' in  dining:
                    dining=dining.replace('K','000').strip()
                if ',' in  delivery:
                        delivery=delivery.replace(',','')
                if 'K' in  delivery:
                    delivery=delivery.replace('.','').strip().replace('K','00')
                if 'K' in  delivery:
                    delivery=delivery.replace('K','000').strip()
                
                
                if len(dining) >=1 and len(delivery) >=1:
                    
                    d['reviews'] = (int(dining) + int(delivery))//2
                    d['reviews_dining']=int(dining)
                    d['reviews_delivery']=int(delivery)
                elif len(dining) >=1:
                    
                    d['reviews'] = int(dining)
                    d['reviews_dining']=int(dining)
                    d['reviews_delivery']=''
                elif len(delivery) >=1:
                    
                    d['reviews'] = int(delivery)
                    d['reviews_dining']=''
                    d['reviews_delivery']=int(delivery)
                else:
                    
                    d['reviews']=''
                    d['reviews_delivery']=''
                    d['reviews_dining']=''
            else:
                d['reviews']=''
                d['reviews_delivery']=''
                d['reviews_dining']=''
                
                    
                
            if len(all_rat) == 2:
                
                dining_rat = ''.join(re.findall('[\d .]',all_rat[0]['value']))
                delivery_rat=''.join(re.findall('[\d .]',all_rat[1]['value']))
                
                
                
                
                if len(dining_rat) >=1 and len(delivery_rat) >=1:
                    
                    
                    
                    d['ratings'] = (float(dining_rat)+ float(delivery_rat))/2
                    d['ratings_delivery']= delivery_rat
                    d['ratings_dining'] = dining_rat
                elif len(dining_rat) >=1:
                    
                    d['ratings'] = float(dining_rat)
                    d['ratings_delivery'] = ''
                    d['ratings_dining'] = float(dining_rat)
                elif len(delivery_rat) >=1:
                    
                    d['ratings'] = float(delivery_rat)
                    d['ratings_delivery']=float(delivery_rat)
                    d['ratings_dining']=''
                    
                else:
                    
                    d['ratings']=''
                    d['ratings_delivery']=''
                    d['ratings_dining']=''
                    
            else:
                d['ratings']=''
                d['ratings_delivery']=''
                d['ratings_dining']=''
                
                
                
                
                
                
            
            
        except :
            
            d['ratings']=''
            d['reviews']=''
            d['ratings_delivery']=''
            d['ratings_dining']=''
            d['reviews_delivery']=''
            d['reviews_dining']=''
            
            
        try:
            cost_all=soup_ui.find_all("h5")
            if  'Top Dishes' in str(cost_all) and 'Average' in str(cost_all):
        
                for cst in range(len(cost_all)):
            
                    if 'Top Dishes' in cost_all[cst].getText():
                    
                        test['fav']=cost_all[cst].findNext("p").getText()
                        
                
                        
                        
                    
                    if 'Average' in cost_all[cst].getText():
                
                        cost_for_2=cost_all[cst].findNext("p").getText()
                        d['cost for 2']=''.join(re.findall(r'\d+', cost_for_2))
                        # test['cost for 2']=''.join(re.findall(r'\d+', cost_for_2))
                        
                        
            elif cost_all and  'Average' in str(cost_all):
                for cst in range(len(cost_all)):
                    
                    if 'Average' in cost_all[cst].getText():
                        
                        cost_for_2=cost_all[cst].findNext("p").getText()
                        d['cost for 2']=''.join(re.findall(r'\d+', cost_for_2))
                        # test['cost for 2']=''.join(re.findall(r'\d+', cost_for_2))
                        test['fav'] =''
                        
            
            
            
            elif cost_all and  'Top Dishes' in str(cost_all):
                for cst in range(len(cost_all)):
                    
                    
                    if 'Top Dishes' in cost_all[cst].getText():
                    
                        test['fav']=cost_all[cst].findNext("p").getText()
                        # test['cost for 2'] = ''
                        d['cost for 2'] = ''
                    
            else:
                # test['cost for 2'] = ''
                test['fav'] =''
                d['cost for 2']=''
                
        except:
            d['cost for 2'] = '' 
            # test['cost for 2']=''
            test['fav'] = ''

        
            
            
            
            
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
    
        
    #for n in range(len(branch_dict)):
        
     #   start_new_thread(zomato_child, (url_more_than_2[n],1,int(branch_dict[url_more_than_2[n]])))
    #threads11=[]  
    
    #executor = ThreadPoolExecutor(len(branch_dict))
    #for n in range(len(branch_dict)):
        
    
     #   executor.submit(zomato_child,(url_more_than_2[n],1,int(branch_dict[url_more_than_2[n]])))
        
        
        #t111 = threading.Thread(target=zomato_child, args=(url_more_than_2[n],1,int(branch_dict[url_more_than_2[n]])))
       # t111.start()
        
      #  threads11.append(t111)

    # # Wait all threads to finish.
    #for t111 in threads11:
        
     #   t111.join()
    
    #for i in branch_dict:
        
   #     zomato_child(i,1,branch_dict[i]+1)
    
    #threads11=[]  
    #for n in range(len(branch_dict)):
        #temp = 't_'+str(n)
       # temp = threading.Thread(target=zomato_child, args=(url_more_than_2[n],1,int(branch_dict[url_more_than_2[n]])))
      #  temp.start()
     #   threads11.append(temp)
    
    #for jj in threads11:
        #jj.join()
        

    
    


#test_df_list= pd.DataFrame.from_dict(d)

#test_df_list.sort_values(by=['ratings'],ascending=False)

#test_df_list.to_csv(city_name+'.csv',index=False)

    
       
        





# p = Pool(15)
# p.map(zomato, d['link'])
# p.terminate()
# p.join()

if os.path.exists(city_name+'lat_lon'+'.csv') == True:
        print("from here latitude longitude")
        retrieve1 = pd.read_csv(city_name+'lat_lon'+'.csv')
        for l in range(len(retrieve1['url'])):
            # panda_dict['ratings'] = str(retrieve['ratings'][l])
            # panda_dict['reviews'] = str(retrieve['reviews'][l])
            # panda_dict['name'] = str(retrieve['name'][l])
            # panda_dict['address'] = str(retrieve['address'][l])
            # panda_dict['cost for 2'] = str(retrieve['cost for 2'][l])
            panda_dict1['lat'] = str(retrieve1['lat'][l])
            panda_dict1['url'] = str(retrieve1['url'][l])
            panda_dict1['lon'] = str(retrieve1['lon'][l])
            panda_dict1['fav'] = str(retrieve1['fav'][l])
            # panda_dict['cuisines'] = str(retrieve['cuisines'][l])
        test_df = pd.DataFrame(panda_dict1)

else:
    
    url_less_than_2 = list(set(url_less_than_2))    
    
    length_ = len(url_less_than_2)


    open_again = final_url
    res_len=len(open_again)
    

    threads=list()
    x = threading.Thread(target=lat_lon, args=(0,res_len//26))
    threads.append(x)
    x.start()

    x2 = threading.Thread(target=lat_lon, args=(res_len//26,(res_len//26)*2))
    threads.append(x2)
    x2.start()

    x3 = threading.Thread(target=lat_lon, args=((res_len//26)*2,(res_len//26)*3))
    threads.append(x3)
    x3.start()

    x4 = threading.Thread(target=lat_lon, args=((res_len//26)*3,(res_len//26)*4))
    threads.append(x4)
    x4.start()

    x5 = threading.Thread(target=lat_lon, args=((res_len//26)*4,(res_len//26)*5))
    threads.append(x5)
    x5.start()


    x6 = threading.Thread(target=lat_lon, args=((res_len//26)*5,(res_len//26)*6))
    threads.append(x6)
    x6.start()

    x7 = threading.Thread(target=lat_lon, args=((res_len//26)*6,(res_len//26)*7))
    threads.append(x7)
    x7.start()

    x8 = threading.Thread(target=lat_lon, args=((res_len//26)*7,(res_len//26)*8))
    threads.append(x8)
    x8.start()

    x9 = threading.Thread(target=lat_lon, args=((res_len//26)*8,(res_len//26)*9))
    threads.append(x9)
    x9.start()

    x10 = threading.Thread(target=lat_lon, args=((res_len//26)*9,(res_len//26)*10))
    threads.append(x10)
    x10.start()


    x11 = threading.Thread(target=lat_lon, args=((res_len//26)*10,(res_len//26)*11))
    threads.append(x11)
    x11.start()

    x12 = threading.Thread(target=lat_lon, args=((res_len//26)*11,(res_len//26)*12))
    threads.append(x12)
    x12.start()

    x13 = threading.Thread(target=lat_lon, args=((res_len//26)*12,(res_len//26)*13))
    threads.append(x13)
    x13.start()

    x14 = threading.Thread(target=lat_lon, args=((res_len//26)*13,(res_len//26)*14))
    threads.append(x14)
    x14.start()

    x15 = threading.Thread(target=lat_lon, args=((res_len//26)*14,(res_len//26)*15))
    threads.append(x15)
    x15.start()


    x16 = threading.Thread(target=lat_lon, args=((res_len//26)*15,(res_len//26)*16))
    threads.append(x16)
    x16.start()

    x17a = threading.Thread(target=lat_lon, args=((res_len//26)*16,(res_len//26)*17))
    threads.append(x17a)
    x17a.start()

    x17 = threading.Thread(target=lat_lon, args=((res_len//26)*17,(res_len//26)*18))
    threads.append(x17)
    x17.start()

    x18 = threading.Thread(target=lat_lon, args=((res_len//26)*18,(res_len//26)*19))
    threads.append(x18)
    x18.start()

    x19 = threading.Thread(target=lat_lon, args=((res_len//26)*19,(res_len//26)*20))
    threads.append(x19)
    x19.start()


    x20 = threading.Thread(target=lat_lon, args=((res_len//26)*20,(res_len//26)*21))
    threads.append(x20)
    x20.start()


    x21 = threading.Thread(target=lat_lon, args=((res_len//26)*21,(res_len//26)*22))
    threads.append(x21)
    x21.start()

    x22 = threading.Thread(target=lat_lon, args=((res_len//26)*22,(res_len//26)*23))
    threads.append(x22)
    x22.start()

    x23 = threading.Thread(target=lat_lon, args=((res_len//26)*23,(res_len//26)*24))
    threads.append(x23)
    x23.start()

    x24 = threading.Thread(target=lat_lon, args=((res_len//26)*24,(res_len//26)*25))
    threads.append(x24)
    x24.start()

    x25 = threading.Thread(target=lat_lon, args=((res_len//26)*25,(res_len//26)*26))
    threads.append(x25)
    x25.start()


    x26 = threading.Thread(target=lat_lon, args=((res_len//26)*26,res_len))
    threads.append(x26)
    x26.start()
    
        
    threads_less=list()
    x_ = threading.Thread(target=fetch_less_than_2, args=(0,length_//26,url_less_than_2))
    threads_less.append(x_)
    x_.start()
    
    x2_ = threading.Thread(target=fetch_less_than_2, args=(length_//26,(length_//26)*2,url_less_than_2))
    threads_less.append(x2_)
    x2_.start()
    
    x3_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*2,(length_//26)*3,url_less_than_2))
    threads_less.append(x3_)
    x3_.start()
    
    x4_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*3,(length_//26)*4,url_less_than_2))
    threads_less.append(x4_)
    x4_.start()
    
    x5_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*4,(length_//26)*5,url_less_than_2))
    threads_less.append(x5_)
    x5_.start()
    
    
    x6_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*5,(length_//26)*6,url_less_than_2))
    threads_less.append(x6_)
    x6_.start()
    
    x7_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*6,(length_//26)*7,url_less_than_2))
    threads_less.append(x7_)
    x7_.start()
    
    x8_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*7,(length_//26)*8,url_less_than_2))
    threads_less.append(x8_)
    x8_.start()
    
    x9_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*8,(length_//26)*9,url_less_than_2))
    threads_less.append(x9_)
    x9_.start()
    
    x10_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*9,(length_//26)*10,url_less_than_2))
    threads_less.append(x10_)
    x10_.start()
    
    
    x11_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*10,(length_//26)*11,url_less_than_2))
    threads_less.append(x11_)
    x11_.start()
    
    x12_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*11,(length_//26)*12,url_less_than_2))
    threads_less.append(x12_)
    x12_.start()
    
    x13_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*12,(length_//26)*13,url_less_than_2))
    threads_less.append(x13_)
    x13_.start()
    
    x14_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*13,(length_//26)*14,url_less_than_2))
    threads_less.append(x14_)
    x14_.start()
    
    x15_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*14,(length_//26)*15,url_less_than_2))
    threads_less.append(x15_)
    x15_.start()
    
    
    x16_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*15,(length_//26)*16,url_less_than_2))
    threads_less.append(x16_)
    x16_.start()
    
    x17a_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*16,(length_//26)*17,url_less_than_2))
    threads_less.append(x17a_)
    x17a_.start()
    
    x17_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*17,(length_//26)*18,url_less_than_2))
    threads_less.append(x17_)
    x17_.start()
    
    x18_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*18,(length_//26)*19,url_less_than_2))
    threads_less.append(x18_)
    x18_.start()
    
    x19_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*19,(length_//26)*20,url_less_than_2))
    threads_less.append(x19_)
    x19_.start()
    
    
    x20_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*20,(length_//26)*21,url_less_than_2))
    threads_less.append(x20_)
    x20_.start()
    
    
    x21_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*21,(length_//26)*22,url_less_than_2))
    threads_less.append(x21_)
    x21_.start()
    
    x22_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*22,(length_//26)*23,url_less_than_2))
    threads_less.append(x22_)
    x22_.start()
    
    x23_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*23,(length_//26)*24,url_less_than_2))
    threads_less.append(x23_)
    x23_.start()
    
    x24_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*24,(length_//26)*25,url_less_than_2))
    threads_less.append(x24_)
    x24_.start()
    
    x25_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*25,(length_//26)*26,url_less_than_2))
    threads_less.append(x25_)
    x25_.start()
    
    
    x26_ = threading.Thread(target=fetch_less_than_2, args=((length_//26)*26,length_,url_less_than_2))
    threads_less.append(x26_)
    x26_.start()


    # x27 = threading.Thread(target=zomato, args=((aa//50)*27,(aa//50)*28,city_name))
    # threads.append(x27)
    # x27.start()

    # x28 = threading.Thread(target=zomato, args=((aa//50)*28,(aa//50)*29,city_name))
    # threads.append(x28)
    # x28.start()

    # x29 = threading.Thread(target=zomato, args=((aa//50)*29,(aa//50)*30,city_name))
    # threads.append(x29)
    # x29.start()

    # x30 = threading.Thread(target=zomato, args=((aa//50)*30,(aa//50)*31,city_name))
    # threads.append(x30)
    # x30.start()


    # x31 = threading.Thread(target=zomato, args=((aa//50)*31,(aa//50)*32,city_name))
    # threads.append(x31)
    # x31.start()

    # x32 = threading.Thread(target=zomato, args=((aa//50)*32,(aa//50)*33,city_name))
    # threads.append(x32)
    # x32.start()

    # x33 = threading.Thread(target=zomato, args=((aa//50)*33,(aa//50)*34,city_name))
    # threads.append(x33)
    # x33.start()

    # x34 = threading.Thread(target=zomato, args=((aa//50)*34,(aa//50)*35,city_name))
    # threads.append(x34)
    # x34.start()

    # x35 = threading.Thread(target=zomato, args=((aa//50)*35,(aa//50)*36,city_name))
    # threads.append(x35)
    # x35.start()


    # x36 = threading.Thread(target=zomato, args=((aa//50)*36,(aa//50)*37,city_name))
    # threads.append(x36)
    # x36.start()



    # x37 = threading.Thread(target=zomato, args=((aa//50)*37,(aa//50)*38,city_name))
    # threads.append(x37)
    # x37.start()

    # x38 = threading.Thread(target=zomato, args=((aa//50)*39,(aa//50)*39,city_name))
    # threads.append(x38)
    # x38.start()

    # x39 = threading.Thread(target=zomato, args=((aa//50)*39,(aa//50)*40,city_name))
    # threads.append(x39)
    # x39.start()


    # x40 = threading.Thread(target=zomato,  args=((aa//50)*40,(aa//50)*41,city_name))
    # threads.append(x40)
    # x40.start()

    # x41 = threading.Thread(target=zomato, args=((aa//50)*41,(aa//50)*42,city_name))
    # threads.append(x41)
    # x41.start()

    # x42 = threading.Thread(target=zomato, args=((aa//50)*42,(aa//50)*43,city_name))
    # threads.append(x42)
    # x42.start()

    # x43 = threading.Thread(target=zomato, args=((aa//50)*43,(aa//50)*44,city_name))
    # threads.append(x43)
    # x43.start()

    # x44 = threading.Thread(target=zomato, args=((aa//50)*44,(aa//50)*45,city_name))
    # threads.append(x44)
    # x44.start()

    # x45 = threading.Thread(target=zomato, args=((aa//50)*45,(aa//50)*46,city_name))
    # threads.append(x45)
    # x45.start()


    # x46 = threading.Thread(target=zomato, args=((aa//50)*46,(aa//50)*47,city_name))
    # threads.append(x46)
    # x46.start()



    # x47 = threading.Thread(target=zomato, args=((aa//50)*47,(aa//50)*48,city_name))
    # threads.append(x47)
    # x47.start()

    # x48 = threading.Thread(target=zomato, args=((aa//50)*48,(aa//50)*49,city_name))
    # threads.append(x48)
    # x48.start()

    # x49 = threading.Thread(target=zomato, args=((aa//50)*49,(aa//50)*50,city_name))
    # threads.append(x49)
    # x49.start()


    # x50 = threading.Thread(target=zomato, args=((aa//50)*50,aa+1,city_name))
    # threads.append(x50)
    # x50.start()


    x.join()
    x2.join()
    x3.join()
    x4.join()
    x5.join()
    x6.join()
    x7.join()
    x8.join()
    x9.join()
    x10.join()
    x11.join()
    x12.join()
    x13.join()
    x14.join()
    x15.join()
    x16.join()
    x17.join()
    x17a.join()
    x18.join()
    x19.join()
    x20.join()
    x21.join()
    x22.join()
    x23.join()
    x24.join()
    x25.join()
    x26.join()
    
    x_.join()
    x2_.join()
    x3_.join()
    x4_.join()
    x5_.join()
    x6_.join()
    x7_.join()
    x8_.join()
    x9_.join()
    x10_.join()
    x11_.join()
    x12_.join()
    x13_.join()
    x14_.join()
    x15_.join()
    x16_.join()
    x17_.join()
    x17a_.join()
    x18_.join()
    x19_.join()
    x20_.join()
    x21_.join()
    x22_.join()
    x23_.join()
    x24_.join()
    x25_.join()
    x26_.join()

    # x27.join()
    # x28.join()
    # x29.join()
    # x30.join()
    # x31.join()
    # x32.join()
    # x33.join()
    # x34.join()
    # x35.join()
    # x36.join()
    # x37.join()
    # x38.join()
    # x39.join()
    # x40.join()
    # x41.join()
    # x42.join()
    # x43.join()
    # x44.join()
    # x45.join()
    # x46.join()
    # x47.join()
    # x48.join()
    # x49.join()
    # x50.join()
    #print(len(d['name']),len(d['link']),len(d['cost for 2']),len(d['cuisines']),len(d['ratings']),len(d['reviews']),len(d['address']),len(d['lat']),len(d['lon']))

    
    #print(len(test['url']),len(test['lat']),len(test['lon']),len(test['fav']),res_len)
    
    
    
    #for surat initially 
    #issue : length of one of the key (usually cost for 2) was more than the total num. of restaurants
    
    d_len={}
    inter =[]
    d_len_f = {}
    ind=[]
    for tr in d.keys():
        d_len[tr] = len(d[tr])
        
    count = collections.Counter(list(d_len.values()))
    
        
    
    for change in range(len(d_len)-1):
        
        if d_len[list(d_len.keys())[change]] != d_len[list(d_len.keys())[change+1]]:
            
            d_len_f[list(d_len.keys())[change]] = d_len[list(d_len.keys())[change]]
    
    
    if len(d_len_f) != 0:
        
    
        d_len_f = {k: v for k, v in sorted(d_len_f.items(), key=lambda item: item[1],reverse= True)}    
        
        positive = d_len_f[list(d_len_f.keys())[0]] - d_len_f[list(d_len_f.keys())[1]]
        
        
        inter = d[list(d_len_f.keys())[0]]
        
        
        for t in range(len(inter)):
            if inter[t] == '':
                ind.append(t)
                
        ind.sort(reverse=True)
        
        ind  = ind[:positive]
        
        for index in sorted(ind, reverse=True):
            del inter[index]
    else:
        print("Pass")
        
        
    test_len={}
    inter_test =[]
    test_len_f = {}
    ind_test=[]
    for trr in test.keys():
        test_len[trr] = len(test[trr])
    
    for change1 in range(len(test_len)-1):
        
        if test_len[list(test_len.keys())[change1]] != test_len[list(test_len.keys())[change1+1]]:
            
            test_len_f[list(test_len.keys())[change1]] = test_len[list(test_len.keys())[change1]]
    
    
    if len(test_len_f) != 0:
        
    
        test_len_f = {k: v for k, v in sorted(test_len_f.items(), key=lambda item: item[1],reverse= True)}    
        positive1 = test_len_f[list(test_len_f.keys())[0]] - test_len_f[list(test_len_f.keys())[1]]
        
        
        inter_test = test[list(test_len_f.keys())[0]]
        
        
        for t1 in range(len(inter_test)):
            if inter_test[t1] == '':
                ind_test.append(t1)
                
        ind_test.sort(reverse=True)
        
        ind_test  = ind_test[:positive1]
        
        for index1 in sorted(ind_test, reverse=True):
            del inter_test[index1]
    else:
        print("Pass2")
        
    
            
     
        
    
    
    
        
        
        
            
        
            
        
        
        
        
    test_df_list = pd.DataFrame(d)
    
    test_df_list.to_csv(city_name+'.csv',index=False)
    
    
    test_df= pd.DataFrame.from_dict(test)
    test_df.to_csv(city_name+'lat_lon'+'.csv',index=False)
    
    
    
    
    
    
    
        



    
    
    
    
#print(len(test_df.url),len(test_df_list.ratings))
    

#print(test_df.url)
#print(test_df_list.link)

#inner_join = pd.concat([test_df.set_index('url'),test_df_list.set_index('link')], ignore_index=True, axis=1,join='inner').reset_index()
#inner_join.to_csv('test111.csv')

print("hhiiii")
left_join= test_df.merge(test_df_list,left_on = test_df['url'], right_on =  test_df_list['link'] , how='right').reset_index()

#for i2 in range(len(left_join)):
 #   if(left_join['reviews'][i2] == 'nan'):
  #      print(left_join['reviews'][i2])
        
#left_join.astype({'reviews' : 'int'}).dtypes


#new for ajmer and others
for ii in left_join['index']:
    
    
    if not str(left_join['reviews'][ii]).replace('.', '', 1).isdigit():
        
        left_join['reviews'].loc[ii] = ''
    else:
        left_join['reviews'].loc[ii] = int(float(str(left_join['reviews'][ii])))
        


for ii in left_join['index']:
    
    if not str(left_join['cost for 2'].loc[ii]).isdigit():
        
        
    
        left_join['cost for 2'].loc[ii] = str(re.sub("[^0-9]","",left_join['cost for 2'].loc[ii]))
    
    
    



for ii in left_join['index']:
    
    
    if ',' in str(left_join['reviews'][ii]):
        
        
        
        left_join['reviews'][ii] =  str(left_join['reviews'][ii]).replace(',','')
        
    if  not str(left_join['reviews'][ii]).isdigit():
        
        left_join['reviews'].loc[ii] = ''






for ii in left_join['index']:
    
    
    if not str(left_join['ratings'][ii]).replace('.', '', 1).isdigit():
        
        left_join['ratings'].loc[ii] = ''




            

for i in range(len(left_join)):
    if 'approx' in str(left_join['fav'].iloc[i]):
        left_join['fav'].iloc[i] = ''            




for ii in left_join['index']:
    
    
    if ',' in str(left_join['cost for 2'][ii]):
        
        
        
        left_join['cost for 2'][ii] =  str(left_join['cost for 2'][ii]).replace(',','')
        
        if  not str(left_join['cost for 2'][ii]).isdigit():
            left_join['cost for 2'].loc[ii] = ''





for i in left_join.columns:
    
    left_join[i].astype('str').apply(lambda x: print(left_join[i].name) if  'Decor' in x else 'pass')

      

query_lat_lon = left_join.query('lat == "0.0" | lat == "nan" | lon == "0.0" | lat == "" | lon == ""  | lon=="nan"')

left_join=left_join.drop(query_lat_lon.index)

left_join['lat'] = left_join['lat'].astype(str).astype(float)
left_join['lon'] = left_join['lon'].astype(str).astype(float)

query = left_join.query('ratings=="" | ratings=="-" | reviews=="" | ratings=="NEW" | reviews=="nan" | ratings=="Opening" | ratings=="Closed" | ratings=="Soon" | ratings=="Temporarily"  | lat >= 90 | lat <= -90 | `cost for 2` == "" |fav=="nan" ')



left_join=left_join.drop(query.index)

left_join['reviews'] = left_join['reviews'].astype(str).astype(int)
left_join['ratings'] = left_join['ratings'].astype(str).astype(float)


if len(inp_rev) > 0:
    
    query2 = left_join.query('reviews < '+inp_rev)
    left_join=left_join.drop(query2.index)
if len(inp_rat) > 0:
    
    query3 = left_join.query('ratings < '+inp_rat)
    left_join=left_join.drop(query3.index)
    
if len(inp_rat_max) > 0:
    
    query3 = left_join.query('ratings > '+inp_rat_max)
    left_join=left_join.drop(query3.index)



#print(left_join)

left_join = left_join.sort_values(by = ['ratings'],ascending = True)

        



#some check condition initially for mumbai
query_ind =[]
for io in left_join.index:
    if not str(left_join.lat[io]).replace('.', '', 1).isdigit():
        query_ind.append(io)

left_join=left_join.drop(query_ind)


cuisine_del=[]
inp_cui_str=str(' '.join(args['cuisines'])).title()

#inp_cui_str = list(str(','.join(inp_cui)).title())
#print(str(inp_cui_str)+"")
for c in left_join['index']:
    if not inp_cui_str in left_join['cuisines'][c]:
        
        cuisine_del.append(left_join['index'][c])
    
left_join = left_join.drop(cuisine_del)

left_join.to_csv('test111.csv' , mode = 'w+')
#print(left_join[(left_join.reviews == 569)])

suggest('test111.csv',city_name=city_name)

print("--- %s seconds ---" % (time.time() - start_time))
