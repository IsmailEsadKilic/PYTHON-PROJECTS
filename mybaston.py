import turtle
import numpy as np
from PIL import Image

# Load the image
im = Image.open('agamsi.png')

# Convert the image to grayscale
im = im.convert('L')

# Convert the image to a 2D numpy array
data = np.array(im)

# Initialize the turtle
turtle.setup(800, 800)
turtle.tracer(0)
turtle.speed(0)
turtle.penup()

# Define the color function
def get_color(value):
    # Map the grayscale value to a turtle color
    color = int(value / 256 * 7)
    colors = ['white', 'gray', 'brown', 'red', 'orange', 'yellow', 'green', 'blue']
    return colors[color]

# Draw the image with turtle
for y in range(data.shape[0]):
    for x in range(data.shape[1]):
        # Move to the position
        turtle.goto(x - data.shape[1] / 2, data.shape[0] / 2 - y)
        # Set the color
        turtle.color(get_color(data[y, x]))
        # Draw a dot
        turtle.dot()
        print(f"{y},{x}")

# Update the screen
turtle.update()

# Keep the window open until the user closes it
turtle.mainloop()