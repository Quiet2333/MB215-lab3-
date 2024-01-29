# Import Turtle graphics library
import turtle

# Set up your drawing parameters
ITERATIONS = 36  # The number of times to repeat the pattern
ANGLE = 10  # The angle to turn after each shape is drawn
SIZE = 100  # The size parameter for the shapes

# Set up the Turtle screen and turtle
screen = turtle.Screen()
pattern_turtle = turtle.Turtle()
pattern_turtle.speed('fastest')  # Speed up the drawing

# Optionally, customize the turtle's appearance
pattern_turtle.color("blue")

# Loop to draw the pattern
for i in range(ITERATIONS):
    # Draw your geometric shape here
    # E.g., to draw a hexagon:
    for _ in range(6):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(60)  # 60 degrees to make a hexagon

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLE)

    # Optionally, change the size or color at certain intervals
    if (i + 1) % 6 == 0:
        pattern_turtle.color("red")  # Change color after every 6 hexagons
    else:
        pattern_turtle.color("blue")

# Complete the program with a command to keep the window open
screen.mainloop()  # This will keep the window open until manually closed
