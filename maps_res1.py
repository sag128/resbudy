# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 04:38:10 2019

@author: sagar
"""
'''
order of execution
0. accessing city sorting functionality and cuisines by cmd via argparse
1. all imports
2. getting cuisines according to different city
3. test case code (commented)
4. fetching coordinates for borders
5. fetching coordinates to fill grid
5.1 fetch cached data if data available for the same queried city
6. adding coordinates to final list tot_lat and lon with border coordinates first
7. initializing one time vars
8. function to find restaurants by cuisines or in general for fixed radius
8.1. fetching cached data if the query already exists
9. credibility criteria i.e. min. 100 reviews should exist per restaurant
10. sorting from rating low to high
10.1. removing duplicate data
11. different types of sorts as per price range also user can choose minimum number of reviews for restaurant to be credible (optional)
12. flushing data to excel using pandas which will be used for caching if same query is called
'''
import random
import numpy as np
import json
import sys
import googlemaps
import math
import time
from geopy.distance import geodesic
from geopy.distance import great_circle
import geopy
import geopy.distance
from geopy import Point
from geopy.distance import vincenty
import pandas as pd
from pyzomato import Pyzomato
import collections
import argparse
import os.path
from scratch_8 import fig
from scratch_8 import fig2


ap = argparse.ArgumentParser()
ap.add_argument("-ci", "--city", type=str, default="Ahmedabad", nargs='+',
    help="city name eg. Ahmedabad (required)")
ap.add_argument("-cu", "--cuisine", type=str, default="", nargs='+',
    help="cuisine (optional) eg North Indian")

ap.add_argument("-r", "--radius", type=int, default=500,
    help="restaurant searching radius (optional)")


ap.add_argument("-p", "--price", type=int, default=2,
    help="price level 0-lowest 3-highest 2-recommended (optional)")

args = vars(ap.parse_args())



f_name=' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'.csv'
print(f_name)








#cuisines=[]
#p = Pyzomato('1198b7e27d9572b3d26a8ecbc066def3')
#city_id=p.getCityDetails(q='Baroda ,India')['location_suggestions'][0]['id']
#all_cuisines=p.getCuisines(city_id)

#for cu in range(len(all_cuisines['cuisines'])):
 #   cuisines.append(all_cuisines['cuisines'][cu]['cuisine']['cuisine_name'])





#test case

all_cities=[]

tes= open('all.txt', 'r') 
test=tes.readlines()
    
for x in range(len(test)):
    all_cities.append(test[x].strip(' " , \n  '))
    
    
#to find for duplicated cities
all_counter=collections.Counter(all_cities)


#non duplicated states and villages
all_keys = list(all_counter.keys())

    




    
tot_lat,tot_lon=[],[]

gmaps = googlemaps.Client(key='AIzaSyCG1qxSc7TOZ4pbOnEVMHcYX3asFT6naUw')
all1=gmaps.geocode(' '.join(args['city']).capitalize()+' ,' +' India')

#for cached data
if os.path.exists(' '.join(args['city']).capitalize()+'.txt') == True:
    print("Already")
    city=open(' '.join(args['city']).capitalize()+'.txt','r')
    c=city.readlines()
    for city_len in range(len(c)):
        tot_lat.append(float(str(c[city_len].strip(" , ' \n")).split(',')[0]))
        tot_lon.append(float(str(c[city_len].strip(" , ' \n")).split(',')[1]))
else:
    


    #initial lat,lon
    nelat,nelon,swlat,swlon,centerlat,centerlon=all1[0]['geometry']['bounds']['northeast']['lat'],all1[0]['geometry']['bounds']['northeast']['lng'],all1[0]['geometry']['bounds']['southwest']['lat'],all1[0]['geometry']['bounds']['southwest']['lng'],all1[0]['geometry']['location']['lat'],all1[0]['geometry']['location']['lng']
        
    nwlat,nwlon=nelat,swlon
    selat,selon=swlat,nelon
        
        
    list_nelat,list_nelon,list_swlat,list_swlon,list_nwlat,list_nwlon,list_selat,list_selon=[],[],[],[],[],[],[],[]
        
        
    list_nelat.append(nelat)
    list_nelon.append(nelon)
    list_swlat.append(swlat)
    list_swlon.append(swlon)
    list_nwlat.append(nwlat)
    list_nwlon.append(nwlon)
    list_selat.append(selat)
    list_selon.append(selon)
        
    #for northeast
        
    #while 1:
            
            
        
    #   new_lat = float(list_nelat[-1])  + (0.5 / 6378) * (-180 / math.pi)
    #  new_lon = float(list_nelon[-1]) + (0.5/ 6378) * (-180 / math.pi) / math.cos(float(list_nelat[-1]) * math.pi/180)
    # list_nelat.append(new_lat)
    #list_nelon.append(new_lon)
            
    #if geodesic((list_nelat[-1],list_nelon[-1]), (centerlat,centerlon)).m <= 1000:
    #   break
        
    #for southwest issue persists in sw
        
        
        
    #while 1:
    #   new_lat = float(list_swlat[-1])  + (0.5 / 6378) * (180 / math.pi)
    #  new_lon = float(list_swlon[-1]) + (0.5/ 6378) * (180 / math.pi) / math.cos(float(list_swlat[-1]) * math.pi/180)
            
            
    #list_swlat.append(new_lat)
    #list_swlon.append(new_lon)
            
            
    # if geodesic((list_swlat[-1],list_swlon[-1]), (centerlat,centerlon)).m <= 1000:
    #    break
        
        
    #for northwest
                
        
    #while 1:
            
            
        
    #   new_lat = float(list_nwlat[-1])  + (0.5 / 6378) * (180 / math.pi)
    #  new_lon = float(list_nwlon[-1]) + (0.5/ 6378) * (-180 / math.pi) / math.cos(float(list_nwlat[-1]) * math.pi/180)
            
            
    # list_nwlat.append(new_lat)
    #list_nwlon.append(new_lon)
            
            
    #if geodesic((list_nwlat[-1],list_nwlon[-1]), (centerlat,centerlon)).m <= 1000:
    #   break
        
        
        
    #for southeast
                
        
    #while 1:
            
            
        
    #   new_lat = float(list_selat[-1])  + (0.5 / 6378) * (-180 / math.pi)
    #  new_lon = float(list_selon[-1]) + (0.5/ 6378) * (180 / math.pi) / math.cos(float(list_selat[-1]) * math.pi/180)
            
            
    # list_selat.append(new_lat)
    #list_selon.append(new_lon)
            
            
    #if geodesic((list_selat[-1],list_selon[-1]), (centerlat,centerlon)).m <= 1000:
    #   break
        
        
        
        
    #generating coorinates using geopy
        
    #for sw     
        
    #distKm = 1
        
    #while 1:
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
    #   new_swlat,new_swlon= geodesic(kilometers=distKm).destination(Point(list_swlat[-1], list_swlon[-1]), 45).format_decimal().split(',')
    #  list_swlat.append(float(new_swlat))
    # list_swlon.append(float(new_swlon))
            
    # if geodesic((list_swlat[-1],list_swlon[-1]), (centerlat,centerlon)).m <= 1000:
    #    break
                
        
    #for ne
        
        
    #while 1:
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
    #   new_nelat,new_nelon= geodesic(kilometers=distKm).destination(Point(list_nelat[-1], list_nelon[-1]), 225).format_decimal().split(',')
    #  list_nelat.append(float(new_nelat))
    # list_nelon.append(float(new_nelon))
            
    #if geodesic((list_nelat[-1],list_nelon[-1]), (centerlat,centerlon)).m <= 1000:
    #   break
        
        
        
    #for nw
            
        
        
    #while 1:
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
    #   new_nwlat,new_nwlon= geodesic(kilometers=distKm).destination(Point(list_nwlat[-1], list_nwlon[-1]), 135).format_decimal().split(',')
    #  list_nwlat.append(float(new_nwlat))
    # list_nwlon.append(float(new_nwlon))
            
    #if geodesic((list_nwlat[-1],list_nwlon[-1]), (centerlat,centerlon)).m <= 1000:
    #   break
        
        
    #for se
            
        
        
    #while 1:
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
    #   new_selat,new_selon= geodesic(kilometers=distKm).destination(Point(list_selat[-1], list_selon[-1]), 315).format_decimal().split(',')
    #  list_selat.append(float(new_selat))
    # list_selon.append(float(new_selon))
            
    #if geodesic((list_selat[-1],list_selon[-1]), (centerlat,centerlon)).m <= 1000:
    #   break
        
        
        
        
    #ne to nw store in nw x and y both change
             
        
    #exec only once
        
        
        
             
    while 1:
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
        new_nwlat,new_nwlon= geodesic(kilometers=1).destination(Point(list_nwlat[-1], list_nwlon[-1]), 90).format_decimal().split(',')
        list_nwlat.append(float(new_nwlat))
        list_nwlon.append(float(new_nwlon))
            
        if geodesic((list_nwlat[-1],list_nwlon[-1]), (nelat,nelon)).m <= 1000:
            break
        
        
        
    #se to sw store in se both x and y change
        
    while 1:
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
        new_selat,new_selon= geodesic(kilometers=1).destination(Point(list_selat[-1], list_selon[-1]), 270).format_decimal().split(',')
        list_selat.append(float(new_selat))
        list_selon.append(float(new_selon))
            
        if geodesic((list_selat[-1],list_selon[-1]), (swlat,swlon)).m <= 1000:
            break
        
    #ne to se store in ne only x changes
        
        
            
    while 1:
            
        new_nelat,new_nelon= geodesic(kilometers=1).destination(Point(list_nelat[-1], list_nelon[-1]), 180).format_decimal().split(',')
        list_nelat.append(float(new_nelat))
        list_nelon.append(float(new_nelon))
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
            
        if geodesic((list_nelat[-1],list_nelon[-1]), (selat,selon)).m <= 1000:
            break
            
    #sw to nw store in sw only x  changes
        
    while 1:
            
        new_swlat,new_swlon= geodesic(kilometers=1).destination(Point(list_swlat[-1], list_swlon[-1]), 0).format_decimal().split(',')
        list_swlat.append(float(new_swlat))
        list_swlon.append(float(new_swlon))
            
        
        
    #print ('center', lat1, lon1)
    #print ('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())
    #print ('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())
    #print ('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())
    #print ('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal())
            
            
            
        if geodesic((list_swlat[-1],list_swlon[-1]), (nwlat,nwlon)).m <= 1000:
            break
    try:
        
        del list_nelat[0]
        del list_nwlat[0]
        del list_selat[0]
        del list_swlat[0]
            
        del list_nelon[0]
        del list_nwlon[0]
        del list_selon[0]
        del list_swlon[0]
    except:
        pass
    tot_lat,tot_lon=[],[]
    lat=[]
    lon=[]
    i,j=0,0
        
    diff = geodesic((nelat,nelon), (selat,selon)).km
        
        
    if math.fabs(diff - math.ceil(diff)) >= 0.5:
            
        
            
        
            
        diff = int(diff // 1)
    else:
            
        diff = int(math.ceil(diff))
            
        
    
    for kilo in range(1,diff+1):
            
            
        for nenw in range(len(list_nwlat)):
                
            i+=1
            nenw_lat,nenw_lon = geodesic(kilometers=kilo).destination(Point(list_nwlat[nenw], list_nwlon[nenw]), 180).format_decimal().split(',')
            tot_lat.append(float(nenw_lat))
            tot_lon.append(float(nenw_lon))
                    
                            
                            
                            
            if geodesic((nenw_lat,nenw_lon), (list_selat[nenw],list_selon[nenw])).m <= 100:
                    
                break
                
    for le in range(len(list_nelat)):
            
        tot_lat.append(list_nelat[le])
        tot_lon.append(list_nelon[le])
        tot_lat.append(list_swlat[le])
        tot_lon.append(list_swlon[le])
        
        
    for le2 in range(len(list_nwlat)):
        tot_lat.append(list_nwlat[le2])
        tot_lon.append(list_nwlon[le2])
        tot_lat.append(list_selat[le2])
        tot_lon.append(list_selon[le2])
        
    with open(' '.join(args['city']).capitalize()+".txt", "w+") as f:
            
        for a in range(len(tot_lat)):
            print(tot_lat[a], tot_lon[a], sep=",", file=f)
        print(len(tot_lat))
        
    
    
    
        
    
        
        
        
    #for x in range(1,len(list_selat)):
     #   list_swlat.append(list_selat[x])
    
    #for y in range(1,len(list_nwlon)):
     #   list_swlon.append(list_nwlon[x])


#test cases around 2.33% error i.e. 27 to 28 out of 1198 entities
    
#for m in range(10):
 #   try:
        
        
    
  #      time.sleep(15)
   #     testpy('Agra')
    #    print(m,all_cities[m])
    #except:
     #   print('failed')
      #  pass
        
#for generating other coordinates to fill the grid

# coordinates of ne to nw stored in nw and se to sw stored in se

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)    
    
        
        
    
#at max 60 results per coordinate
        
#these 4 vars will be exec only once
res_list=[]
unique_address=[]    
emptylist=[]
final_dict={}
dup_lat,dup_lon=[],[]
to_del,final_to_del=[],[]
total_final=[]
panda_dict = Dictlist()
dataframe={}
unique_res,unique_address=[],[]
retrieve=[]

def final_res(lat,lon):
    
    k="AIzaSyCG1qxSc7TOZ4pbOnEVMHcYX3asFT6naUw"
    
    gmaps = googlemaps.Client(key=k)
    #print('current execution for'+ str(lat)+"  "+str(lon))
    params = {
        'query': ''.join(args['cuisine']),
        'location': (lat,lon), #sample coordinate
        'radius':args['radius'],
        'type':'restaurant'
        
        
        
        
        
    }
    #if previously data was fetched then noo need for fetching again
    if os.path.exists(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'.csv') == True:
        print("from here")
        retrieve = pd.read_csv(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'.csv')
        for l in range(len(retrieve['rating'])):
            panda_dict['rating'] = float(retrieve['rating'][l])
            panda_dict['reviews'] = retrieve['reviews'][l]
            panda_dict['name'] = retrieve['name'][l]
            panda_dict['address'] = retrieve['address'][l]
            panda_dict['price_level'] = str(retrieve['price_level'][l])
            panda_dict['lat'] = retrieve['lat'][l]
            panda_dict['lon'] = retrieve['lon'][l]
            
    else:
            
            
        
        x0,x1,x2={},{},{}
        try:
            
            
        
            x0 = gmaps.places(**params)
            #print (len(x0['results'])) # outputs 20 (which is maximum per 1 page result)
            #print (x0['results'][0]['name'])
            emptylist.append(x0)
                
                
                
                
            params['page_token'] = x0['next_page_token']
                
            time.sleep(2)
            x1 = gmaps.places(**params)
                
            #print (len(x1['results']))
            #print (x1['results'][0]['name'])
            emptylist.append(x1)
            params['page_token'] = x1['next_page_token']
                
            time.sleep(2)
            x2 = gmaps.places(**params)
                
            #print (len(x2['results']))
            #print (x2['results'][0]['name'])
            emptylist.append(x2)
        except:
            pass
            
            
                
        
        
        
        #def repeat(loc_inc,start):
            
        
            #new_loc = [23.0519095, 72.5760132]
         #   new_loc = ['23.036766',' 72.5218824']
            
          #  time.sleep(2)
           # emptylist.append(gmaps.places('north indian restaurant',location=new_loc,radius=0.5))
        
        
        #repeat(0,0)
        
        #walking in the given boundary
        
        #finding average difference
        #lat_diff,lon_diff=0,023.036765,72.5218823
        #for diff in range(len(lat)-1):
         #   lat_diff+=math.fabs(float(lat[diff]) - float(lat[diff+1]))
        #avg_lat_diff=lat_diff/len(lat)
            
        
        #for diff2 in range(len(lon)-1):
         #   lon_diff+=math.fabs(float(lon[diff2]) - float(lon[diff2+1]))
        #avg_lon_diff=lon_diff/len(lon)
        
        #derived_lat_lon=[]
        #general formula
        #def lat_lon(lat,lon):
         #   new_lat = float(lat)  + (0.5 / 6378) * (-180 / math.pi)
          #  new_lon = float(lon) + (0.5 / 6378) * (180 / math.pi) / math.cos(float(lat) * math.pi/180)
           # derived_lat_lon.append([str(new_lat),str(new_lon)])
        
        #for i in range(len(abac)):
            
         #   lat_lon(lat[i],lon[i])
        
        #float_lat,float_lon=[],[]
        
        #for iter_lat_lon in range(len(lat)):
         #   float_lat.append(float(lat[iter_lat_lon]))
          #  float_lon.append(float(lon[iter_lat_lon]))
            
        
        #test=[]
        #for calc in range(len(float_lat)-1):
            
         #   if str(geodesic((float_lat[calc],float_lon[calc]),(float_lat[calc+1],float_lon[calc+1]))) >= '1.8 km':
          #      test.append((str((float_lat[calc],float_lon[calc])),str((float_lat[calc+1],float_lon[calc+1]))))
                
                
            
            
            
            
            
            
            
            
        
        count,c2=0,0
        for coor in range(len(emptylist)):
            for m in range(len(emptylist[coor]['results'])):
                
                
                res_lat,res_lon=emptylist[coor]['results'][m]['geometry']['location']['lat'],emptylist[coor]['results'][m]['geometry']['location']['lng']
                
                    
                
                
                #print(emptylist[coor]['results'][m]['name'],c2,geodesic((lat,lon), (res_lat,res_lon)).m)
                res_list.append(emptylist[coor]['results'][m])
                    
                c2+=1
                
        #for coor in range(len(emptylist)):
         #   for m in range(20):
          #      res_lat,res_lon=emptylist[coor]['results'][m]['geometry']['location']['lat'],emptylist[coor]['results'][m]['geometry']['location']['lng']
           #     if geodesic((lat,lon), (res_lat,res_lon)).m <=2000:
            #        print(emptylist[coor]['results'][m]['name'],c2,geodesic((23.036765, 72.5218823), (res_lat,res_lon)).m)
                    
                
                
        
        
        #final dict
        
        for mm in range(len(res_list)):
            final_dict[(res_list[mm]['rating'],res_list[mm]['user_ratings_total'])]  = res_list[mm]
    

def clean():
    final_list=[]
    

    #to be executed seperately
    
    sorted_final_dict=sorted(final_dict.items(), key = lambda x: (-x[0][1], x[0][0]))
    
    
    
    for fin in range(len(sorted_final_dict)):
        
        if sorted_final_dict[fin][0][1] >= 100:
            
            
            final_list.append(sorted_final_dict[fin])
    
    #for rating low to high for considerable volume        
    final_list = sorted(final_list, key = lambda x: x[0][0])
    
        
    #for unique restaurant check via coordinates
    
    
    for oo in range(len(final_list)):
        unique_res.append((float(final_list[oo][1]['geometry']['location']['lat']),float(final_list[oo][1]['geometry']['location']['lng'])))
    
    tcounter=collections.Counter(unique_res)
    
    io=list(tcounter.keys())
    
    #for duplicates identification
    
    
    for tq in io:
        if tcounter[tq] >=2:
            dup_lat.append(tq[0])
            dup_lon.append(tq[1])
    
    for dup in range(len(dup_lat)):
        
        for er in range(len(final_list)):
            
            if final_list[er][1]['geometry']['location']['lat'] == dup_lat[dup] and final_list[er][1]['geometry']['location']['lng'] == dup_lon[dup]:
                to_del.append(er)
        
        
    #all process after sorting
    # to delete index numbers from final_list
    #here 1st is always higher in terms of reviews than the others
    
    
    for u in range(1,len(to_del),2):
        final_to_del.append(to_del[u])
                
    
    
    for y  in range(len(final_list)):
        if y not in final_to_del:
            total_final.append(final_list[y])
        else:
            pass
        
    
    #just double checking
            
    for oo2 in range(len(total_final)):
        unique_address.append((float(total_final[oo2][1]['geometry']['location']['lat']),float(total_final[oo2][1]['geometry']['location']['lng'])))
        
    double_check=collections.Counter(unique_address)
    
            
    #this is the final one
    
    for ti in range(len(total_final)):
        panda_dict['rating'] = float(total_final[ti][0][0])
        panda_dict['reviews'] = total_final[ti][0][1]
        panda_dict['name'] = total_final[ti][1]['name']
        panda_dict['address'] = total_final[ti][1]['formatted_address']
        if 'price_level' in total_final[ti][1]:
            
            panda_dict['price_level'] = total_final[ti][1]['price_level']
        else:
            panda_dict['price_level'] = 2
        panda_dict['lat'] = total_final[ti][1]['geometry']['location']['lat']
        panda_dict['lon'] = total_final[ti][1]['geometry']['location']['lng']
        panda_dict['icon'] = total_final[ti][1]['icon']
        
    dataframe=pd.DataFrame(panda_dict)
    
    dataframe.to_csv(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'.csv',index=False)

#if previously data was fetched then noo need for fetching again
if os.path.exists(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'.csv') == True:
    
    print("from here")
    retrieve = pd.read_csv(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'.csv')
    for l in range(len(retrieve['rating'])):
        panda_dict['rating'] = float(retrieve['rating'][l])
        panda_dict['reviews'] = retrieve['reviews'][l]
        panda_dict['name'] = retrieve['name'][l]
        panda_dict['address'] = retrieve['address'][l]
        panda_dict['price_level'] = str(retrieve['price_level'][l])
        panda_dict['lat'] = retrieve['lat'][l]
        panda_dict['lon'] = retrieve['lon'][l]
        panda_dict['icon'] =retrieve['icon'][l]
        
else:

    for ji in range(len(tot_lat)):
        
        final_res(tot_lat[ji],tot_lon[ji])       
    clean()

final_lat=[]
final_lon=[]
for e in range(len(retrieve)):
    final_lat.append(retrieve['lat'][e])
    final_lon.append(retrieve['lon'][e])
    
#for text suggestion
tott=[]
length = int(len(retrieve) * 0.2)
for f in range(length-1):
    for f2 in range(length-1):
        
        if f!=f2:
            
            if geodesic((retrieve['lat'][f],retrieve['lon'][f]), (retrieve['lat'][f2],retrieve['lon'][f2])).m <= 2000:
                
                tott.append((retrieve['lat'][f],retrieve['lon'][f]))
                tott.append((retrieve['lat'][f2],retrieve['lon'][f2]))
#for te in  range(len(tott)):
 #   for te2 in range(len(tott)):
        
    
  #      if (list(set(tott))[te]) == (list(set(tott))[te2])[::-1]:
   #         print(tott.index((list(set(tott))[te2])[::-1]))
            
        
pin=[]
for ii in range(length):
    pin.append(panda_dict['address'][ii][-6:])

pin_c = collections.Counter(pin)
pin_c=sorted(pin_c.items(),key=lambda x:x[1],reverse=True)

 

#lat1=[tott[x][0] for x in range(len(tott))]
#lon1=[tott[y][1] for y in range(len(tott))]
    
#dataframe1=pd.DataFrame({'lat':lat1,'lon':lon1})
    
#dataframe1.to_csv('final'+'.csv',index=False)
pin_coord_lat,pin_coord_lng=[],[]
len_pin_c=len(pin_c)//6
pin_coord_lat=[gmaps.geocode(pin_c[t][0])[0]['geometry']['location']['lat'] for t in range(len_pin_c) ]
pin_coord_lng=[gmaps.geocode(pin_c[tt][0])[0]['geometry']['location']['lng'] for tt in range(len_pin_c) ]

for iot in range(len_pin_c):
    for iot1 in range(length):
        if pin_c[iot][0] in panda_dict['address'][iot1]:
            print(panda_dict['name'][iot1]+' for '+pin_c[iot][0])
            




dataframe1=pd.DataFrame({'lat':pin_coord_lat,'lon':pin_coord_lng})
dataframe1.to_csv(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'_final'+'.csv',index=True)
    

fig(f_name)
print(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'_final'+'.csv')
fig2(' '.join(args['city']).capitalize()+'_'+' '.join(args['cuisine']).capitalize()+'_'+str(args['radius'])+'_final'+'.csv')
        
