N = 10
lambda, mu = 2, 3

arrival = zeros(N) #absolute time of arrival
departure = zeros(N) #absolute time of departure
waiting_time = zeros(N)

for k in 2:N
    time_to_arrival_k = rand(Exponential(1. / lambda)) #time between arrival k-1 and k
    service_time_k = rand(Exponential(1. / mu))
    arrival[k] = arrival[k - 1] + time_to_arrival_k
    departure[k] = max(arrival[k], departure[k - 1]) + service_time_k
    waiting_time[k] = departure[k] - arrival[k]
end
print(waiting_time)
