import sys
import math 
data = [50,3,60,49,19,88,13,2,71,6]
sq_data = []
F_summ = sum(data)
mean = F_summ/len(data)
print(mean)
i = 0
while i < len(data):
    diff = data[i] - mean
    sq_data.append(diff**2)
    i+=1
S_summ = sum(sq_data)
variance = S_summ/len(data)-1
print(variance)
deviation = math.sqrt(variance)
print(deviation)