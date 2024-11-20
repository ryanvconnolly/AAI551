# Author: Ryan Connolly
# Date: October 5, 2024
# Description: This program simulates an array of CRMD's on a 2D map, finds the location of the highest capture rate and the location with the lowest capture rate and then outputs the entire map grid.

import random 

MAP_DIMENSIONS = 8

mapMatrix = [[0 for _ in range(MAP_DIMENSIONS)] for _ in range(MAP_DIMENSIONS)]

for i in range(MAP_DIMENSIONS):
    for j in range(MAP_DIMENSIONS):
        mapMatrix[i][j] = random.randint(0,500)

highestX = 0
highestY = 0
lowestX = 0
lowestY = 0
highestRate = -1
lowestRate = 501

for i in range(MAP_DIMENSIONS):
    for j in range(MAP_DIMENSIONS):
        if mapMatrix[i][j] > highestRate:
                highestRate = mapMatrix[i][j]
                highestX = j
                highestY = i
        if mapMatrix[i][j] < lowestRate:
            lowestRate = mapMatrix[i][j]
            lowestX = j
            lowestY = i
            
print(f"The highest capture rate was {highestRate} at location {highestX+1},{highestY+1}.")
print(f"The lowest capture rate was {lowestRate} at location {lowestX+1},{lowestY+1}.")

print("Here is the map gird: ")
for row in mapMatrix:
    print(' '.join(f"{cell:3}" for cell in row))
