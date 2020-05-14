#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:42:28 2020

@author: sagar
"""


import re
import requests
import threading
from bs4 import BeautifulSoup
import time
from io import StringIO
import argparse
import collections

ap = argparse.ArgumentParser()
ap.add_argument("-ci", "--city", type=str, default="ajmer", nargs='+',
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

#for storing all urls and then iterating and using threads 
# also using thread to store url in final_url remove dups
final_url = []
html_less_than_2 =[]

url_more_than_2 = []


#to fetch non empty result till x page number

#test= Dictlist()
panda_dict = Dictlist()
panda_dict1 = Dictlist()
city_name = ''.join(args['city']).lower()





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

aa_final = aa2[0]
print(sorted(aa2)[0])        






















#fn for scraping all urls from a city

def zomato(start,stop,city_name):
    


    tot =[]    

    branch_dict = {}                
    
    

    for i in range(start,stop):
        
    
        url = 'https://www.zomato.com/'+city_name+'/restaurants?sort=best&page='+str(i)
        agent = {"User-Agent":'Chrome/61.0.3163.100'}
        page = requests.get(url, headers=agent)
        soup=BeautifulSoup(page.content, 'lxml')
        
        #l2=soup.find_all("div",{'class':'ui col-l-16 fontsize5 grey-text'})
        #l3 = soup.find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})
        
        
        parent = soup.find_all("div",{"class":"card search-snippet-card search-card"})
        
        
        
        
        for i in range(len(parent)):
            final_url.append(parent[i].find("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})['href'])
            if parent[i].find("a",{"class":"ui ta-right pt10 fontsize3 zred pb10 pr10"}):
                
                url_more_than_2.append('http://www.zomato.com'+str(parent[i].find_all("a",{"class":"ui ta-right pt10 fontsize3 zred pb10 pr10"})[0]['href']))
                
            else:
                if len(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})) == 1:
                    
                    

                    final_url.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[0]['href'])
                    
                if len(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})) == 2:
                    
                    final_url.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[0]['href'])
                    final_url.append(parent[i].find_all("a",{"class":"ui col-l-16 search_chain_bottom_snippet"})[1]['href'])
                    
    
    #for i2 in range(len(html_less_than_2)):
        
    
     #   for i3 in range(len(html_less_than_2[i2])):
            
      #      url_less_than_2.append(html_less_than_2[i2][i3]['href'])
    
    
    #for getting all restaurants from list - url_more_than_2
    
    for u in range(len(url_more_than_2)):
        
    
        url2 = url_more_than_2[u]
        agent2 = {"User-Agent":'Chrome/61.0.3163.100'}
        page2 = requests.get(url2, headers=agent2)
        soup2=BeautifulSoup(page2.content, 'lxml')
        
        page3=soup2.find_all("div",{'class':'col-l-4 mtop pagination-number'})
        
        pg=int(str(list(page3[0])).split("<b>")[-1].split("<")[0])
        branch_dict[url2] = pg
        
    #funtion body
                
                
    def zomato_child(url_param,start,stop):
        
        for j in range(start,stop):
    
            url3 = url_param+ '&page='+str(j)
            agent3 = {"User-Agent":'Chrome/61.0.3163.100'}
            page33 = requests.get(url3, headers=agent3)
            soup33=BeautifulSoup(page33.content, 'lxml')
            
            length=soup33.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
            #soup2=soup33.find_all("a",{'class':'result-title hover_feedback zred bold ln24 fontsize0'})
            #ratings_len = len(soup33.find_all("div",{"class":"ta-right floating search_result_rating col-s-4 clearfix"}))
            #ratings = soup33.find_all("div",{"class":"ta-right floating search_result_rating col-s-4 clearfix"})
            #cost_for_2 = soup33.find_all("span",{"class":"col-s-11 col-m-12 pl0"})
            
            
            #cuisines = soup33.find_all("span",{"class":"col-s-11 col-m-12 nowrap pl0"})
            #address = soup33.find_all("div",{"class":"col-m-16 search-result-address grey-text nowrap ln22"})
            #lat =soup.find("meta",{"property" : "place:location:latitude"})
            #lon =soup.find("meta",{"property" : "place:location:longitude"})
            #print(lat['content'])
            #print(lon['content'])
            
            
                
            for tt in range(len(length)):
                final_url.append(length[tt]['href'])
    
                #if  list(ratings[tt].getText().split())[0] != "NEW":
                    
                    #print(list(ratings[tt].getText().split())[0])
                
    
                    #d['name'] = soup2[tt]['title']
                    #d['link'] = soup2[tt]['href']
                    
                    #try:
    
                     #   d['cost for 2'] = cost_for_2[tt].getText()[1:]
                    #except :
                        
    
                     #   d['cost for 2'] = ""
    
                    #try:
    
                     #   d['cuisines'] = cuisines[tt].getText()
                    #except:
                     #   d['cuisines'] = ""
    
                    #try:
    
                     #   d['ratings'] = (list(ratings[tt].getText().split())[0])
                    #except:
    
                     #   d['ratings'] = ""
                    #try:
                     #   d['reviews'] = (list(ratings[tt].getText().split())[1])
                    #except:
                     #   d['reviews'] = ""
    
    
    
                    #try:
    
                     #   d['address'] = address[tt].getText()
                    #except:
                     #   d['address'] = ""
    
    
    
    
    #for getting all info of branch restaurants
    
    for i in branch_dict:
        
        zomato_child(i,1,branch_dict[i]+1)
    
    
        #for i2 in range(1,branch_dict[i]+1):
            
            
            
            #url_loop = str(i) + '&page='+str(i2)
            #agent_loop = {"User-Agent":'Chrome/61.0.3163.100'}
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
    
 

    

#for total number of branches
#for i in range(len(l2)):
 #   tot.extend(re.findall(r'\b\d+\b',l2[i].getText()) )
    
#if total branches are less than or equal to 2

threads1=list()
t = threading.Thread(target=zomato, args=(1,3,'ajmer') , name="1")
threads1.append(t)
t.start()

t1 = threading.Thread(target=zomato, args=(3,5,'ajmer') , name="2")
threads1.append(t1)
t1.start()

t.join()
t1.join()  


unique = list(set(final_url))



#scraping data from new ui 

url_less_than_2_dictlist = Dictlist()
def fetch(start,stop):
    
    for u in range(start,stop):
        
    
        temp_str=[]
        
        url_ui = unique[u]
        agent_ui = {"User-Agent":'Chrome/61.0.3163.100'}
        page_ui = requests.get(url_ui, headers=agent_ui)
        soup_ui=BeautifulSoup(page_ui.content, 'lxml')
        
        name_ui=soup_ui.find("main")
        name = name_ui.find("h1")
        d['name']=name.getText()
        
        cuisines = name_ui.find_all("h5")
        for qq in range(len(cuisines)):
            if cuisines[qq].getText() == "Cuisines":
                loop_var_cuisines = qq
                
        cuisines = cuisines[loop_var_cuisines]
        cuisines = cuisines.findNextSibling()
        cuisines= cuisines.find_all('a')
        for i in range(len(cuisines)):
            temp_str.append(cuisines[i].getText())
        d['cuisines'] = ", ".join(temp_str)
        
     
        address = name_ui.find("p",{"class":"sc-1hez2tp-0 clKRrC"}).getText()
        d['address'] = address
        
        
        
        
        try:
            ratings = name_ui.find("article")
            d['ratings'] = ratings.getText()
            #print(ratings.getText())    
        except:
            ratings=''
            d['ratings'] = ratings
            #print(ratings)
        try:
            reviews = ratings.findNextSibling()
            d['reviews'] = reviews.getText()
            #print(reviews.getText())
        except:
            reviews = ''
            d['reviews'] = reviews
            #print(reviews)
        #print(url_ui)
            
        
        
        try:
            
            cost_all = name_ui.findAll("p",{"color":"#4F4F4F"})
            for cst in range(len(cost_all)):
                
                if '₹' in cost_all[cst].getText() and 'pint' not in cost_all[cst].getText():
                    
                    
                    
                    cost_for_two = cost_all[cst].getText()
                    
                    
                    cost_for_two = ''.join(re.findall(r'\d+', cost_for_two))
                    d['cost for 2'] = cost_for_two
                    print(cost_for_two+" hi")
            else:
                fav =cost_all[0].getText()
                if fav == cost_for_two:
                    d['fav'] = ''
                else:
                    d['fav'] = fav
                    
                
                
                
            
            
                
        except:
            d['cost for 2'] = ''
            
            
            
            
        try:
            
            loc = soup_ui.find_all("script",{"data-rh":"true"})
            loc = str(loc[1]).split("{")[1]
            loc = re.findall(r'\d+\.\d+', loc)
            
            
            d['lat']=loc[0]
            d['lon']=loc[1]
        except:
            d['lat']= ''
            d['lon']  = ''
        
            
            
            #if address available then get lat lon from google geolocation api from maps_res.py
            
            
        
        
    
    
    
    #test.append(StringIO.StringIO(cuisines))
#for j1 in distinct.keys():
 #   fetch(j1)
    
#fetch('https://www.zomato.com/ahmedabad/the-esplendido-cafe-navrangpura')


threads2=list()
t = threading.Thread(target=fetch, args=(0,len(unique)//2) , name="1")
threads2.append(t)
t.start()

t1 = threading.Thread(target=fetch, args=(len(unique)//2,len(unique)) , name="2")
threads2.append(t1)
t1.start()

t.join()
t1.join()  
