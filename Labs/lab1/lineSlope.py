# Author: Ryan Connolly
# Date: September 11, 2024
# Description: This program computes the slope of a line given 
# the end points of the line. The result is then printed to the screen.

# Initialize the end points.
startX = -2
startY = 1
endX = 5
endY = 36

# Compute the slope.
slope = (startY - endY) / (startX - endX)

# Print the results.
print(f"Starting point: ({startX}, {startY})")
print(f"Ending point: ({endX}, {endY})")
print(f"Slope of the line = {slope}")

