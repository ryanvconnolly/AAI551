# Author: Ryan Connolly
# Date: October 5, 2024
# Description: This program record the distances a projectile flies for a number of trials, keeping track of the 3 trials with the furthest distance using lists.

top3 = [0,0,0]
top3numbers = [0,0,0]
inputAdditional = "Y"
currentTrial = 1

distance = int(input(f"Hello! Enter for distance for trial {currentTrial}: "))
top3.append(distance)
top3.sort(reverse=True)
top3 = top3[:3]

currentTrial += 1

inputAdditional = input("Would you like to try again? (Y/N): ")

while inputAdditional == "Y":
    distance_temp = int(input(f"Okay! Now enter the distance for trial {currentTrial}: "))

    if distance_temp > top3[0]:
        top3.insert(0,distance_temp)
        top3 = top3[:3]
        top3numbers.insert(0, currentTrial)
    
    elif distance_temp > top3[1]:
        top3.insert(1,distance_temp)
        top3 = top3[:3]
        top3numbers.insert(1,currentTrial)
        top3numbers = top3numbers[:3]
        
    elif distance_temp > top3[2]:
        top3.insert(2,distance_temp)
        top3 = top3[:3]
        top3numbers.insert(2,currentTrial)
        top3numbers = top3numbers[:3]
        
    inputAdditional = input("Would you like to try again? (Y/N): ")
    
    currentTrial += 1
    
print("Okay! Your top 3 distances were: \n      Trial        Distance")
for trial, distance in zip(top3numbers, top3):
    print(f"\t{trial}        \t{distance}")