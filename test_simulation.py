import random
import math
arrive_table = [1, 2, 3, 5, 15]
Service_table = [2.1, 3.3, 1.1, 0.5, 1.7]
job_list = []
index = 0
total_table = []
T = 0
N = 0
def find_min(target):
    a = float('inf')
    b = 0
    for i in range(len(target)):
        if target[i][1] < a:
            a = target[i][1]
            b = i
    return target[b]

master_clock = 0
Tend = 100000
next_arrival_time = arrive_table[0]
next_departure_time = float('Inf')
service_time = round(Service_table[0],2)
while(master_clock < Tend):
    if next_arrival_time < next_departure_time:
        next_event_time = next_arrival_time
        next_event_type = 1
    else:
        next_event_time = next_departure_time
        next_event_type = 0
    temp = master_clock
    master_clock = next_event_time
    gap = master_clock - temp
    if next_event_type == 1:
        if len(job_list) != 0:
            for i in job_list:
                i[1] = i[1] - gap / len(job_list)
                i[1] = round(i[1],2)
        job_list.append([master_clock, service_time])
        last_time_phrase = find_min(job_list)[1]
        next_departure_time = master_clock + len(job_list) * last_time_phrase
        next_arrival_time = master_clock
        #print("hi",master_clock)
        if(index < len(arrive_table) ):
            #print(master_clock)
            index += 1
            if(index < len(arrive_table)):
                next_arrival_time = arrive_table[index]
                next_arrival_time = round(next_arrival_time,2)
        #print(next_arrival_time,master_clock)
                service_time = round(Service_table[index],2)
            else:
                next_arrival_time = float('inf')
                

            #print(service_time)
            if len(job_list) != 0:
                min_phrase = find_min(job_list)

            c = [i for i in job_list]
            total_table.append([master_clock,"arrive",next_arrival_time,round(next_departure_time,8),c])
        else:
            break

    else:
            # count how many same time departure phrase
            if(len(job_list) > 0):
                min_phrase = find_min(job_list)
            count = 0
            # save same time job to temp list
            temp = []
            for j in job_list:
                if j[1] == min_phrase[1]:
                    temp.append([j[0], j[1]])
                    count += 1
            for k in temp:
                variance = k[0]
                #print(k)
                job_list.remove(k)
                T = T + master_clock - variance
                N = N + 1

                print(N,round(T,2),round(T/N,3))
            if len(job_list) == 0:
                next_departure_time = float('Inf')
                #print(master_clock)
                b = [i for i in job_list]
                if(master_clock != float('inf')):
                    total_table.append([master_clock,"departure",next_arrival_time,next_departure_time,b])
            # else, each job in list should minus time past, then set departure time to new time
            else:
                for m in job_list:
                    m[1] = m[1] - gap / (len(job_list) + count)
                    m[1] = round(m[1],2)
                    last_time_phrase = find_min(job_list)[1]
                next_departure_time = master_clock + len(job_list) * last_time_phrase

                next_departure_time = round(next_departure_time,3)
                a = [i for i in job_list]
                if(master_clock != float('inf')):
                    total_table.append([round(master_clock,8),"departure",next_arrival_time,next_departure_time,a])
                #print("total_table",total_table)
                #print("hi",job_list)
for i in total_table:
   print(i)



