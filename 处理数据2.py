#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:29:21 2017

@author: wangjun
"""

import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

dataall=pd.read_csv("dataclean.csv")

dataall["result"]=dataall["HomeName"]

for i in range(0,len(dataall["HomeName"]),1):
    if dataall["HomeGoals"][i]>dataall["AwayGoals"][i]:
        dataall["result"][i]=2
    elif dataall["HomeGoals"][i]==dataall["AwayGoals"][i]:
        dataall["result"][i]=1
    else:
        dataall["result"][i]=0


