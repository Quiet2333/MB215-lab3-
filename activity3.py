# Import the math module
import math

# Ask user for the diameter of the cylinder's circular end
diameter = float(input("Enter the diameter of the cylinder's circular end: "))

# Ask user for the height of the cylinder
height = float(input("Enter the height of the cylinder: "))

# Consider the initial value of pi and then round it to 2 decimal places
pi = round(3.141592, 2)

# Calculate the radius of the cylinder's circular end
radius = diameter / 2

# Calculate the volume of the cylinder using the formula
volume = pi * (radius ** 2) * height

# Output the calculated volume
print("The volume of the cylinder is:", volume)
