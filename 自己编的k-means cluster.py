#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:10:42 2017

@author: wangjun
"""

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math 

data=pd.read_csv("shanchu10.csv")
x1=data["chuwin"]
x2=data["chudraw"]
num=len(x1)
startna=rd.randint(1,num)
startnb=rd.randint(1,num)

k=2
starta1=x1[startna]
starta2=x2[startna]
startb1=x1[startnb]
startb2=x2[startnb]

ca=[]
cb=[]

for i in range(1,len(x1),1):
    disa=math.sqrt((x1[i]-starta1)**2+(x2[i]-starta2)**2)
    disb=math.sqrt((x1[i]-startb1)**2+(x2[i]-startb2)**2)
    if disa>=disb:
        ca.append(i)
        ca=ca
    else:
        cb.append(i)
        cb=cb






clustera1=x1[ca]
clustera2=x2[ca]
clusterb1=x1[cb]
clusterb2=x2[cb]

dc1=1
while (dc1==0):
    
    centernewa1=clustera1.mean()
    centernewa2=clustera2.mean()
    centernewb1=clusterb1.mean()
    centernewb2=clusterb2.mean()
    
    
    a=clustera1.mean()
    b=clustera2.mean()
    c=clusterb1.mean()
    d=clusterb2.mean()
    
    newna=0
    disnew=math.sqrt((clustera1[0]-centernewa1)**2+(clustera2[0]-centernewa2)**2)
    for i in range(1,len(ca),1):
        disi=math.sqrt((clustera1[i]-centernewa1)**2+(clustera2[i]-centernewa2)**2)
        if disi>disnew:
            newna=i
    newnb=0
    disnewb=math.sqrt((clusterb1[0]-centernewb1)**2+(clusterb2[0]-centernewb2)**2)
    for i in range(1,len(cb),1):
        disib=math.sqrt((clusterb1[i]-centernewb1)**2+(clusterb2[i]-centernewb2)**2)
        if disib>disnewb:
            newnb=i
            
    starta1=clustera1[newna]
    starta2=clustera2[newna]
    startb1=clusterb1[newnb]
    startb2=clusterb2[newnb]
    
    for i in range(1,len(x1),1):
      disa=math.sqrt((x1[i]-starta1)**2+(x2[i]-starta2)**2)
      disb=math.sqrt((x1[i]-startb1)**2+(x2[i]-startb2)**2)
      if disa>=disb:
        ca.append(i)
        ca=ca
      else:
        cb.append(i)
        cb=cb
        
        
    clustera1=x1[ca]
    clustera2=x2[ca]
    clusterb1=x1[cb]
    clusterb2=x2[cb]
    
    a1=clustera1.mean()
    b1=clustera2.mean()
    c1=clusterb1.mean()
    d1=clusterb2.mean()
    
    dc1==(a1-a)**2+(b1-b)**2+(c1-c)**2+(d1-d)**2
    
    
    
    
    

fig2 = plt.figure(1,figsize=(8,8))
plt.plot(clustera1,clustera2,'bx',clusterb1,clusterb2,'rs')


        


