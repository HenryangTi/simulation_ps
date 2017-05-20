#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:52:48 2017

@author: sdawedsafa
"""

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
this_seed = random.seed(1000)
r_lambda = 7.2
stack = [random.random() for i in range(100000)]
bins = 60
x = [(random.uniform(0.75,1.17)) for i in stack]
n, bins, patches = plt.hist(x, bins, normed = 1, facecolor = 'blue', alpha = 0.4)
plt.title("Histogram of exponentially distributed number")
plt.xlabel('Distributed values')
plt.ylabel('Frequency')
plt.show()