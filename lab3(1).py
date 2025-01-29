import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions (make it square to avoid distortion)
window_size = 600

# Function to plot points in all octants
def plot_circle_points(x_center, y_center, x, y):
    glBegin(GL_POINTS)
    # Plot points for all eight octants
    glVertex2i(x_center + x, y_center + y)  # Point in the 1st quadrant (top-right)
    glVertex2i(x_center - x, y_center + y)  # Point in the 2nd quadrant (top-left)
    glVertex2i(x_center + x, y_center - y)  # Point in the 4th quadrant (bottom-right)
    glVertex2i(x_center - x, y_center - y)  # Point in the 3rd quadrant (bottom-left)

    glVertex2i(x_center + y, y_center + x)  # Point in the 1st quadrant (mirrored over x=y)
    glVertex2i(x_center - y, y_center + x)  # Point in the 2nd quadrant (mirrored over x=y)
    glVertex2i(x_center + y, y_center - x)  # Point in the 4th quadrant (mirrored over x=y)
    glVertex2i(x_center - y, y_center - x)  # Point in the 3rd quadrant (mirrored over x=y)

    glEnd()

# Mid-Point Circle Drawing Algorithm
def midpoint_circle(x_center, y_center, radius):
    x = 0
    y = radius
    d = 1 - radius  # Initial decision parameter
    plot_circle_points(x_center, y_center, x, y)
    
    # Continue until x crosses y
    while x < y:
        if d < 0:
            # Choose the pixel to the right
            x=x+1
            d += 2 * x + 3
        else:
            # Choose the pixel diagonally below
            y -= 1
            x += 1
            d += 2 * (x - y) + 1
        plot_circle_points(x_center, y_center, x, y)

# Function to draw axes
def draw_axes():
    glBegin(GL_LINES)
    # X-axis (Red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(-300, 0)
    glVertex2i(300, 0)
    # Y-axis (Green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(0, -300)
    glVertex2i(0, 300)
    glEnd()

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw axes
    draw_axes()
    
    # Set circle color to white
    glColor3f(1.0, 1.0, 1.0)
    
    # Draw a circle centered at (0, 0) with radius 100
    midpoint_circle(0, 0, 100)
    
    glFlush()

# Initialize OpenGL settings
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    gluOrtho2D(-300, 300, -300, 300)  # Set orthographic projection (square)

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_size, window_size)  # Set window size (square)
    glutInitWindowPosition(100, 100)  # Set window position on screen
    glutCreateWindow(b"Symmetric Circle Drawing in OpenGL")
    init()
    glutDisplayFunc(display)  # Register display callback
    glutMainLoop()

if __name__ == "__main__":
    main()
