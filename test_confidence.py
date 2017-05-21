#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:31:00 2017

@author: sdawedsafa
"""
import math
import scipy as sp
import scipy.stats
import mean_confidence_test as mct
import random

def test_confidence(servers, seed_n):
    time_box = []
    cd = 0
    for i in range(seed_n):
        #print(i)
        cd += 1
        tend = 100000 + cd*500
        #print(time_box)
        time_box.append(mct.main(servers, i, tend))
        #print(time_box)
    #print(time_box)
    
    mean_time = sum(time_box) / seed_n
    print("server",servers,"mean_time",mean_time)
    
    #print(mean_time)
    temp = 0
    for i in time_box:
        temp += ((mean_time - i) ** 2)
    sta_devi = math.sqrt(temp / (seed_n ))
    alpha = 1 - (1 - 0.95) / 2
    t = sp.stats.t.ppf(alpha, seed_n - 1)
    low_boundary = mean_time - t * sta_devi / math.sqrt(seed_n)
    high_boundary = mean_time + t * sta_devi / math.sqrt(seed_n)
    print("server",servers,"standard deviation",sta_devi)
    return [low_boundary, high_boundary]

for i in range(3,11):
    print("server",i,test_confidence(i, 10))