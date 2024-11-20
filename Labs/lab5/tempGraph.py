# Author: Ryan Connolly
# Date: October 5, 2024
# Description: This program generates random temps for a series of cities, stores them in lists, and creates a graph using the lists. 

import matplotlib.pyplot as plt 
import random

time = [1,2,3,4,5,6,7,8,9,10,11,12]

ny = []
la = []
london = []

for i in range(len(time)):
    ny.append(random.randint(10,30))
    la.append(random.randint(10,30))
    london.append(random.randint(10,30))
    
plt.plot(time, ny)
plt.plot(time, la)
plt.plot(time, london)

plt.title("Temperatures in New York, Los Angeles, and London At Given Times")
plt.xlabel("Hours")
plt.ylabel("Temps")
plt.legend

plt.show()