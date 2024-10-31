# Author: Ryan Connolly
# Date: September 11, 2024
# Description: Given a duration of time, this program computes 
# the velocity, average velocity, and displacement of an object using user input.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Initialize the radius:
time = float(input("Please enter the duration of time for the calculation in seconds: "))
# Calculate the properties of the object:

velocity = initialVelocity + acceleration*time
averageV = initialVelocity + (0.5)*(acceleration*time)
displacement = initialVelocity*time + (0.5)*(acceleration)*(time**2)

# Print the results:
print(f"time = {time} \n")
print(f"velocity         = {velocity:.2f}")
print(f"average velocity = {averageV:.1f}")
print(f"displacement     = {displacement:.1f}")  
