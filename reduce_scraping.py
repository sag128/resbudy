#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 06:23:53 2020

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

ap = argparse.ArgumentParser()
ap.add_argument("-ci", "--city", type=str, default="ahmedabad", nargs='+',
    help="city name eg. Ahmedabad (required)")
args = vars(ap.parse_args())
    



class Dictlist(dict):

    def __setitem__(self, key, value):

        try:
            self[key]
        except KeyError:

            super(Dictlist, self).__setitem__(key, [])

        self[key].append(value) 

d=Dictlist()
test= Dictlist()
panda_dict = Dictlist()
panda_dict1 = Dictlist()
city_name = ' '.join(args['city']).lower()





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
        
       



agent = {"User-Agent":'Chrome/61.0.3163.100'}
page = requests.get(url, headers=agent)
soup=BeautifulSoup(page.content, 'lxml')

l2=len(soup.find_all("div",{'class':'col-l-4 mtop pagination-number'}))

page=soup.find_all("div",{'class':'col-l-4 mtop pagination-number'})

aa=int(str(list(page[0])).split("<b>")[-1].split("<")[0])
res_len=int()


d2=Dictlist()

aa2=[]

def final_page(start,stop,city_name2):
    

    for i in range(start,stop):
            
        
            url = 'https://www.zomato.com/'+city_name2+'/restaurants?sort=best&page='+str(i)
            agent = {"User-Agent":'Chrome/61.0.3163.100'}
            page = requests.get(url, headers=agent)
            soup=BeautifulSoup(page.content, 'lxml')
                    
            try:
                
                test = soup.find("div",{"class":"ui cards"})
                
                
                t=collections.Counter(test.getText().split())
    
                if t['NEW'] + t['-'] >= 15:
                    aa2.append(i)
                    break
            except:
                print("pass")
                    

    
    #for j in range(len(test)):
        
     #   d2['ratings'] = test[j].getText().split()[0]
        

   
threads1=list()
t = threading.Thread(target=final_page, args=(1,aa//25,city_name) , name="1")
threads1.append(t)
t.start()

t2 = threading.Thread(target=final_page, args=(aa//25,(aa//25)*2,city_name), name="2")
threads1.append(t2)
t2.start()

t3 = threading.Thread(target=final_page, args=((aa//25)*2,(aa//25)*3,city_name), name="3")
threads1.append(t3)
t3.start()

t4 = threading.Thread(target=final_page, args=((aa//25)*3,(aa//25)*4,city_name), name="4")
threads1.append(t4)
t4.start()

t5 = threading.Thread(target=final_page, args=((aa//25)*4,(aa//25)*5,city_name), name="5")
threads1.append(t5)
t5.start()


t6 = threading.Thread(target=final_page, args=((aa//25)*5,(aa//25)*6,city_name), name="6")
threads1.append(t6)
t6.start()

t7 = threading.Thread(target=final_page, args=((aa//25)*6,(aa//25)*7,city_name), name="7")
threads1.append(t7)
t7.start()

t8 = threading.Thread(target=final_page, args=((aa//25)*7,(aa//25)*8,city_name), name="8")
threads1.append(t8)
t8.start()

t9 = threading.Thread(target=final_page, args=((aa//25)*8,(aa//25)*9,city_name), name="9")
threads1.append(t9)
t9.start()

t10 = threading.Thread(target=final_page, args=((aa//25)*9,(aa//25)*10,city_name), name="10")
threads1.append(t10)
t10.start()


t11 = threading.Thread(target=final_page, args=((aa//25)*10,(aa//25)*11,city_name), name="11")
threads1.append(t11)
t11.start()

t12 = threading.Thread(target=final_page, args=((aa//25)*11,(aa//25)*12,city_name), name="12")
threads1.append(t12)
t12.start()

t13 = threading.Thread(target=final_page, args=((aa//25)*12,(aa//25)*13,city_name), name="13")
threads1.append(t13)
t13.start()

t14 = threading.Thread(target=final_page, args=((aa//25)*13,(aa//25)*14,city_name), name="14")
threads1.append(t14)
t14.start()

t15 = threading.Thread(target= final_page, args=((aa//25)*14,(aa//25)*15,city_name), name="15")
threads1.append(t15)
t15.start()


t16 = threading.Thread(target=final_page, args=((aa//25)*15,(aa//25)*16,city_name), name="16")
threads1.append(t16)
t16.start()

t17 = threading.Thread(target=final_page, args=((aa//25)*16,(aa//25)*17,city_name), name="17")
threads1.append(t17)
t17.start()

t18 = threading.Thread(target=final_page, args=((aa//25)*17,(aa//25)*18,city_name), name="18")
threads1.append(t18)
t18.start()

t19 = threading.Thread(target=final_page, args=((aa//25)*18,(aa//25)*19,city_name), name="19")
threads1.append(t19)
t19.start()

t20 = threading.Thread(target=final_page, args=((aa//25)*19,(aa//25)*20,city_name), name="20")
threads1.append(t20)
t20.start()

t21 = threading.Thread(target=final_page, args=((aa//25)*20,(aa//25)*21,city_name), name="21")
threads1.append(t21)
t21.start()

t22 = threading.Thread(target=final_page, args=((aa//25)*21,(aa//25)*22,city_name), name="22")
threads1.append(t22)
t22.start()

t23 = threading.Thread(target=final_page, args=((aa//25)*22,(aa//25)*23,city_name), name="23")
threads1.append(t23)
t23.start()

t24 = threading.Thread(target=final_page, args=((aa//25)*23,(aa//25)*24,city_name), name="24")
threads1.append(t24)
t24.start()

t25 = threading.Thread(target=final_page, args=((aa//25)*24,aa+1,city_name), name="25")
threads1.append(t25)
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



















def zomato(start, stop):
    
    for ii in range(start,stop):
        test1=str()
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





aa = aa2[0]
print(sorted(aa2)[0])        
print("--- %s seconds ---" % (time.time() - start_time))

if os.path.exists(city_name+'.csv') == True:
        print("from here")
        retrieve = pd.read_csv(city_name+'.csv')
        for l in range(len(retrieve['ratings'])):
            panda_dict['link'] = str(retrieve['link'][l])
            panda_dict['ratings'] = str(retrieve['ratings'][l])
            panda_dict['reviews'] = str(retrieve['reviews'][l])
            panda_dict['name'] = str(retrieve['name'][l])
            panda_dict['address'] = str(retrieve['address'][l].strip())
            panda_dict['cost for 2'] = str(retrieve['cost for 2'][l])
            # panda_dict['lat'] = str(retrieve['lat'][l])
            # panda_dict['lon'] = str(retrieve['lon'][l])
            panda_dict['cuisines'] = str(retrieve['cuisines'][l])
            
            if(panda_dict['ratings'][l] == '-' or panda_dict['ratings'][l] == 'NEW' or panda_dict['ratings'][l] == ''):
                
                print(panda_dict['link'][l])
        test_df_list = pd.DataFrame(panda_dict)


else:
    threads1=list()
    t = threading.Thread(target=zomato, args=(1,aa//25) , name="1")
    threads1.append(t)
    t.start()

    t2 = threading.Thread(target=zomato, args=(aa//25,(aa//25)*2), name="2")
    threads1.append(t2)
    t2.start()

    t3 = threading.Thread(target=zomato, args=((aa//25)*2,(aa//25)*3), name="3")
    threads1.append(t3)
    t3.start()

    t4 = threading.Thread(target=zomato, args=((aa//25)*3,(aa//25)*4), name="4")
    threads1.append(t4)
    t4.start()

    t5 = threading.Thread(target=zomato, args=((aa//25)*4,(aa//25)*5), name="5")
    threads1.append(t5)
    t5.start()


    t6 = threading.Thread(target=zomato, args=((aa//25)*5,(aa//25)*6), name="6")
    threads1.append(t6)
    t6.start()

    t7 = threading.Thread(target=zomato, args=((aa//25)*6,(aa//25)*7), name="7")
    threads1.append(t7)
    t7.start()

    t8 = threading.Thread(target=zomato, args=((aa//25)*7,(aa//25)*8), name="8")
    threads1.append(t8)
    t8.start()

    t9 = threading.Thread(target=zomato, args=((aa//25)*8,(aa//25)*9), name="9")
    threads1.append(t9)
    t9.start()

    t10 = threading.Thread(target=zomato, args=((aa//25)*9,(aa//25)*10), name="10")
    threads1.append(t10)
    t10.start()


    t11 = threading.Thread(target=zomato, args=((aa//25)*10,(aa//25)*11), name="11")
    threads1.append(t11)
    t11.start()

    t12 = threading.Thread(target=zomato, args=((aa//25)*11,(aa//25)*12), name="12")
    threads1.append(t12)
    t12.start()

    t13 = threading.Thread(target=zomato, args=((aa//25)*12,(aa//25)*13), name="13")
    threads1.append(t13)
    t13.start()

    t14 = threading.Thread(target=zomato, args=((aa//25)*13,(aa//25)*14), name="14")
    threads1.append(t14)
    t14.start()

    t15 = threading.Thread(target=zomato, args=((aa//25)*14,(aa//25)*15), name="15")
    threads1.append(t15)
    t15.start()


    t16 = threading.Thread(target=zomato, args=((aa//25)*15,(aa//25)*16), name="16")
    threads1.append(t16)
    t16.start()

    t17 = threading.Thread(target=zomato, args=((aa//25)*16,(aa//25)*17), name="17")
    threads1.append(t17)
    t17.start()

    t18 = threading.Thread(target=zomato, args=((aa//25)*17,(aa//25)*18), name="18")
    threads1.append(t18)
    t18.start()

    t19 = threading.Thread(target=zomato, args=((aa//25)*18,(aa//25)*19), name="19")
    threads1.append(t19)
    t19.start()

    t20 = threading.Thread(target=zomato, args=((aa//25)*19,(aa//25)*20), name="20")
    threads1.append(t20)
    t20.start()

    t21 = threading.Thread(target=zomato, args=((aa//25)*20,(aa//25)*21), name="21")
    threads1.append(t21)
    t21.start()
    
    t22 = threading.Thread(target=zomato, args=((aa//25)*21,(aa//25)*22), name="22")
    threads1.append(t22)
    t22.start()
    
    t23 = threading.Thread(target=zomato, args=((aa//25)*22,(aa//25)*23), name="23")
    threads1.append(t23)
    t23.start()
    
    t24 = threading.Thread(target=zomato, args=((aa//25)*23,(aa//25)*24), name="24")
    threads1.append(t24)
    t24.start()
    
    t25 = threading.Thread(target=zomato, args=((aa//25)*24,aa+1), name="25")
    threads1.append(t25)
    t25.start()
    



    # t20 = threading.Thread(target=zomato, args=((aa//26)*20,aa+1))
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


    test_df_list= pd.DataFrame.from_dict(d)
    
    test_df_list.sort_values(by=['ratings'],ascending=False)

    test_df_list.to_csv(city_name+'.csv',index=False)



