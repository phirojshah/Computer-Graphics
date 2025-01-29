from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Function to plot a point on the circle
def plot_circle_points(x_center, y_center, x, y):
    glBegin(GL_POINTS)
    # Plot points in all octants
    glVertex2i(x_center + x, y_center + y)  # Octant 1
    glVertex2i(x_center - x, y_center + y)  # Octant 2
    glVertex2i(x_center + x, y_center - y)  # Octant 3
    glVertex2i(x_center - x, y_center - y)  # Octant 4
    glVertex2i(x_center + y, y_center + x)  # Octant 5
    glVertex2i(x_center - y, y_center + x)  # Octant 6
    glVertex2i(x_center + y, y_center - x)  # Octant 7
    glVertex2i(x_center - y, y_center - x)  # Octant 8
    glEnd()

# Polar Circle Drawing Algorithm
def polar_circle(x_center, y_center, radius):
    theta = 0  # Start angle in radians
    end_angle = math.radians(360)  # Full circle
    step = 1 / radius  # Increment angle based on radius for smoothness
    
    while theta < end_angle:
        # Calculate x and y using polar coordinates
        x = int(radius * math.cos(theta))
        y = int(radius * math.sin(theta))
        plot_circle_points(x_center, y_center, x, y)
        theta += step

# Function to draw axes for reference
def draw_axes():
    glBegin(GL_LINES)
    # Draw X-axis
    glVertex2i(-400, 0)
    glVertex2i(400, 0)
    # Draw Y-axis
    glVertex2i(0, -300)
    glVertex2i(0, 300)
    glEnd()

# Display function to render the circle
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set drawing color to white
    draw_axes()  # Draw the axes
    polar_circle(0, 0, 150)  # Draw the circle with radius 150 centered at (0, 0)
    glFlush()

# Initialize the OpenGL environment
def main():
    glutInit()  # Initialize the GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Single buffer and RGB mode
    glutInitWindowSize(800, 600)  # Window size
    glutInitWindowPosition(100, 100)  # Window position
    glutCreateWindow("Circle Drawing using Polar Coordinates")  # Window title
    gluOrtho2D(-400, 400, -300, 300)  # Set the coordinate system
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black
    glutDisplayFunc(display)  # Register the display callback function
    glutMainLoop()  # Enter the main loop

if __name__ == "__main__":
    main()
