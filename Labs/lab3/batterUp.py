# Author: Ryan Connolly
# Date: September 21, 2024
# Description: This program will simulate a batters hit using the random module.

import random

distance = random.randint(0,450)

if distance > 400:
    print(f"The batter hit {distance} feet. He hit a home run and scored for the team!")
elif distance <= 400 and distance >= 135:
    print(f"The batter hit {distance} feet. He hit into the outfield and made it to 3rd base!")
elif distance <= 134 and distance >= 10:
    print(f"The batter hit {distance} feet. He hit into the infield and made it to 2nd base!")
elif distance <= 9 and distance >= 1:
    print(f"The batter hit {distance} feet. He bunted the ball and made it to first!")
elif distance == 0:
    print("Strike! :()")
    
    