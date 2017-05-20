#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 19:17:25 2017

@author: sdawedsafa
"""

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
this_seed = random.seed(1000)
container = [random.random() for i in range(10000)]
bins = 50
beta = 0.86
alpha1 = 0.43
alpha2 = 0.98
gamma = (1 - beta) / (pow(alpha2, (1 - beta)) - pow(alpha1, (1 - beta)))
x = [pow((random.random() * (1 - beta) / gamma) + pow(alpha1, (1 - beta)), (1 / (1 - beta))) for i in container]
n, bins, patches = plt.hist(x, bins, normed = 1, facecolor = 'blue', alpha = 0.4)
plt.title("Histogram of service time")
plt.xlabel('Distributed values')
plt.ylabel('Frequency')
plt.show()




