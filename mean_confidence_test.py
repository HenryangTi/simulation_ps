#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 22:51:45 2017

@author: sdawedsafa
"""

import random
import math

def main(nb_servers, index, Tend):
# seed
    a = 0
    this = random.seed(10000)
    #print(index)
    index += 3000
    # Accounting parameters
    # nb_servers are how many servers on in each turn
    # T is the cumulative response time
    # N is number of completed customers at the end of the simulation
    # and the mean response time will be T/N
    #nb_servers = 7
    T = 0
    N = 0

    # Due to limited power, each PS server would have limited power
    # and for this, each PS server own a different frequency
    power = 2000 / nb_servers
    f = 1.25 + (0.31 * ((power / 200) - 1))

    # mean arrival rate lambda with 7.2, beta with 0.86, alpha1 with 0.43 and alpha2 with 0.98
    Lambda = 7.2
    beta = 0.86
    alpha1 = 0.43
    alpha2 = 0.98


    # Here gt is the probability density function of the service time t devide by f
    # The probability density function is derived function of service_time on range(alpha1, alpha2)
    # Hence here, we calculate the service_time replace with alpha2 and the low limit set to be alpha1, the
    # area of it is random from 0 to 1.
    gamma = (1 - beta) / (pow(alpha2, (1 - beta)) - pow(alpha1, (1 - beta)))
    service_time_next_arrival = pow((random.random() * (1 - beta) / gamma) + pow(alpha1, (1 - beta)), (1 / (1 - beta))) / f

    # Inter-arrival time is product of a1k and a2k
    # a1k is the exponentially distributed with lambda 7.2
    # a2k is uniform distributed range from 0.75 to 1.17
    def arrival():
        next_arrival_time = (- math.log(1 - random.random()) / Lambda) * random.uniform(0.75, 1.17)
        return next_arrival_time


    def service_t():
        ## service_t = pow((random.random() - beta * gamma * pow(alpha1, (- beta - 1)) / (- beta * gamma)), (1 / (- beta - 1)))
        service_t = pow((random.random() * (1 - beta) / gamma) + pow(alpha1, (1 - beta)), (1 / (1 - beta))) / f
        return service_t


    # This function help me to find out the minimal departure time and return it
    def find_min(target):
        a = float('inf')
        b = 0
        for i in range(len(target)):
            if target[i][1] < a:
                a = target[i][1]
                b = i
        return target[b]


    # The master clock start with 0
    # The master clock max limitation would be designed
    # Job list will record each time`s job with type of list contain[master_clock, depature_time]
    # Initial departure time is Infinite
    master_clock = 0
    #Tend = 10000
    job_list = []
    next_arrival_time = arrival()
    next_departure_time = float('Inf')
    service_time = service_t()
    while(master_clock < Tend):
        
        if next_arrival_time < next_departure_time:
            next_event_time = next_arrival_time
            next_event_type = 1
        else:
            next_event_time = next_departure_time
            next_event_type = 0

        # temp is to temporary record the master clock
        temp = master_clock

        master_clock = next_event_time
        # gap is for next event`s master clock
        gap = master_clock - temp

        # Arrival event
        if next_event_type == 1:
            if len(job_list) != 0:
                # every job list should decrease time for each time pass
                for i in job_list:
                    i[1] = i[1] - gap / len(job_list)
            # add new event to list and its service time
            job_list.append([master_clock, service_time])
            last_time_phrase = find_min(job_list)[1]
            next_departure_time = master_clock + len(job_list) * last_time_phrase
            next_arrival_time = master_clock
            # calculate next arrivel time with product of a1k and a2k
            for i in range(nb_servers):
                next_arrival_time += (- math.log(1 - random.random()) / Lambda) * random.uniform(0.75, 1.17)
                service_time = service_t()

        # Departure event
        else:
            # find out the minimal
            min_phrase = find_min(job_list)
            # count how many same time departure phrase
            count = 0
            # save same time job to temp list
            temp = []
            for j in job_list:
                if j[1] == min_phrase[1]:
                    temp.append([j[0], j[1]])
                    count += 1
            for k in temp:
                variance = k[0]
                job_list.remove(k)
                T = T + master_clock - variance
                N = N + 1
                if(a == index):
                    #print(a)
                    return T / N
                else:
                    
                    a += 1
                    #print(a)

            # if empty list, halt the loop by set next_departure_time to infinite
            if len(job_list) == 0:
                next_departure_time = float('Inf')
            # else, each job in list should minus time past, then set departure time to new time
            else:
                for m in job_list:
                    m[1] = m[1] - gap / (len(job_list) + count)
                    last_time_phrase = find_min(job_list)[1]
                next_departure_time = master_clock + len(job_list) * last_time_phrase


    # Test main function, modify output text and target
        #print('Number_of_running_servers:', nb_servers)
        #return T / N