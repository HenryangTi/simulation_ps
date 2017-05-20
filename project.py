import random
import math
import matplotlib.pyplot as plt
this = random.seed(10000)
for nb_servers in range(3,11):
    T = 0
    N = 0
    power = 2000 / nb_servers
    f = 1.25 + (0.31 * ((power / 200) - 1))
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
    Tend = 100000
    job_list = []
    next_arrival_time = arrival()
    next_departure_time = float('Inf')
    service_time = service_t()
    mean_res = []
    total_time = []
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
            next_departure_time = master_clock + \
                len(job_list) * last_time_phrase
            next_arrival_time = master_clock
            # calculate next arrivel time with product of a1k and a2k
            for i in range(nb_servers):
                next_arrival_time += (- math.log(1 - random.random()) / Lambda) * random.uniform(0.75, 1.17)
                service_time = service_t()
        else:
            min_phrase = find_min(job_list)
            count = 0
            temp = []
            index1 = 60000
            for j in job_list:
                if j[1] == min_phrase[1]:
                    temp.append([j[0], j[1]])
                    count += 1
            for k in temp:
                variance = k[0]
                job_list.remove(k)
                T = T + master_clock - variance
                N = N + 1
                #print(master_clock - variance)
                total_time.append(T)
                mean_res.append(T/N)
            if len(job_list) == 0:
                next_departure_time = float('Inf')
            else:
                for m in job_list:
                    m[1] = m[1] - gap / (len(job_list) + count)
                    last_time_phrase = find_min(job_list)[1]
                next_departure_time = master_clock + len(job_list) * last_time_phrase
    job_num = []
    print('Number_of_running_servers:', nb_servers)
    print('Response time:', T / N)
    for i in range(len(mean_res)):
        job_num.append(i)
    plt.plot(job_num, mean_res, '-or')
    plt.show()

    #plt.plot()
    
    #plt.show()
