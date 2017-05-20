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

def test_confidence(servers, seed_n, tend):
    time_box = []
    for i in range(seed_n):
        #print(i)
        time_box.append(mct.main(servers, i, tend))
    mean_time = sum(time_box) / seed_n
    #print(mean_time)
    temp = 0
    for i in time_box:
        temp += ((mean_time - i) ** 2)
    sta_devi = math.sqrt(temp / (seed_n - 1))
    alpha = 1 - (1 - 0.95) / 2
    t = sp.stats.t.ppf(alpha, seed_n - 1)
    low_boundary = mean_time - t * sta_devi / math.sqrt(seed_n)
    high_boundary = mean_time + t * sta_devi / math.sqrt(seed_n)
    return [low_boundary, high_boundary]
if __name__ == '__main__':
    for i in range(3,11):
        print("server",i,test_confidence(i, 30, 10000))