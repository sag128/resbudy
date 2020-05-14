#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:02:41 2020

@author: sagar
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
import collections
import googlemaps
import scratch_8

class Dictlist(dict):

    def __setitem__(self, key, value):

        try:
            self[key]
        except KeyError:

            super(Dictlist, self).__setitem__(key, [])

        self[key].append(value) 

def suggest(filename,city_name):
    
    
    
    cluster_ind = Dictlist()
    df1 = pd.read_csv(filename)
    
    df1 = df1.reset_index()
    coords = df1[['lat', 'lon']].values
    
    
    
    kms_per_radian = 6378
    epsilon = 0.5 / kms_per_radian
    db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels))
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
    print('Number of clusters: {}'.format(num_clusters))
    
    def get_centermost_point(cluster):
        centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
        centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
        return tuple(centermost_point)
    centermost_points = clusters.map(get_centermost_point)
    
    
    size = []
    avg_size=int()
    lats, lons = zip(*centermost_points)
    
    for i2 in range(len(clusters)):
        
        size.append(len(clusters[i2]))
    
    
    
        
    
    rep_points = pd.DataFrame({'lon':lons, 'lat':lats,'size':size})
    
    query = rep_points.query('size<'+str(int(avg_size)))
    rep_points = rep_points.drop(query.index)
    
    rep_points.to_csv('center.csv')
    rs = rep_points.apply(lambda row: df1[(df1['lat']==row['lat']) & (df1['lon']==row['lon'])].iloc[0], axis=1)
    
    for iu in range(len(rep_points.index)):
        cluster_ind[rep_points.index[iu]] = np.where(cluster_labels == rep_points.index[iu])[0]
    
    
    fig, ax = plt.subplots(figsize=[20, 6])
    rs_scatter = ax.scatter(rs['lon'], rs['lat'], c='#99cc99', edgecolor='None', alpha=0.7, s=120)
    df_scatter = ax.scatter(df1['lon'], df1['lat'], c='k', alpha=0.9, s=3)
    ax.set_title('Full data set vs DBSCAN reduced set')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend([df_scatter, rs_scatter], ['Full set', 'Reduced set'], loc='upper right')
    #plt.show()
    
    plt.savefig(city_name,format='png')
    
    '''df = pd.read_csv("/home/sagar/Downloads/Pincode_30052019.csv",encoding='unicode_escape')
    
    all_pinc = []
    
    for i in range(len(df['Circle Name'])):
        if  'bengaluru' in str(df['Division Name'][i]).lower() :
            all_pinc.append(df['Pincode'][i])
        
        
    c= collections.Counter(all_pinc)
    all_pinc = []
    
    all_pinc = [x for x in c.keys()]
    
    
    gmaps = googlemaps.Client(key='AIzaSyCG1qxSc7TOZ4pbOnEVMHcYX3asFT6naUw')
    print(gmaps.geocode('380013'))
    '''
    
    tt=[]
    cluster_final = Dictlist()
    for t in cluster_ind:
        for m in cluster_ind[t][0]:
            tt.append(df1.iloc[m])
        cluster_final[t] = tt
        tt=[]
        
    cluster_final_pd = Dictlist()
    avg_rating_list,avg_review_list,avg_cost_list=[],[],[]
    for y in cluster_final:
        avg_ratings,avg_reviews,avg_cost = 0,0,0
        for u in range(len(cluster_final[y][0])):
            avg_cost = avg_cost + cluster_final[y][0][u]['cost for 2']
            avg_reviews = avg_reviews +  cluster_final[y][0][u]['reviews']
            avg_ratings = avg_ratings + cluster_final[y][0][u]['ratings']
            print(len(cluster_final[y][0]))
        cluster_final_pd[y] = [round(avg_ratings/len(cluster_final[y][0]),1),round(avg_reviews/len(cluster_final[y][0]),2),round(avg_cost/len(cluster_final[y][0]),1)]
    
    
    for ii in cluster_final_pd.keys():
        
        avg_rating_list.append(cluster_final_pd[ii][0][0])
        avg_review_list.append(cluster_final_pd[ii][0][1])
        avg_cost_list.append(cluster_final_pd[ii][0][2])
        
        
    df2 = pd.DataFrame({'cluster':rep_points.index,'size':rep_points['size'],'rating':avg_rating_list,'reviews':avg_review_list,'cost': avg_cost_list,'lat':rep_points['lat'],'lon':rep_points['lon']})            
    
    for io in df2['size']:
        avg_size = avg_size + io
    
    avg_size = avg_size / len(size)
    avg_size = avg_size*2
    print(avg_size)
    query2 = df2.query('size<'+str(int(avg_size)))
    
    df2 = df2.drop(query2.index)
    
    df2 = df2.sort_values(['rating','size'],ascending=(True,False))
    
    
    
    
    df2= df2.reset_index()
    
    df2.to_csv('center_final.csv')
            
    
    
    
    scratch_8.fig(filename)
    scratch_8.fig2('center_final.csv')

  
