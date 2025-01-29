from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Constants
WINDOW_WIDTH = 800  # Width of the OpenGL window
WINDOW_HEIGHT = 600  # Height of the OpenGL window

# Data for the graph
frequencies = [30, 50, 20, 60, 40, 70, 10, 35, 45, 55]  # Sample data points

# Color for the line graph (normalized RGB values for OpenGL)
LINE_COLOR = (0.2, 0.6, 0.8)  # Light blue color

def dda_line(x1, y1, x2, y2, color):
    """
    Draws a line using the DDA (Digital Differential Analyzer) algorithm.
    Args:
        x1, y1: Starting coordinates of the line
        x2, y2: Ending coordinates of the line
        color: The color to draw the line in (tuple of RGB values)
    """
    # Calculate differences and the number of steps
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))  # Choose the larger of dx or dy for smooth plotting

    # Prevent division by zero in case of no steps
    if steps == 0:
        return

    # Calculate the increments for each step
    x_inc = dx / steps
    y_inc = dy / steps

    # Starting position
    x = x1
    y = y1

    # Loop through each step and draw a point
    for _ in range(int(steps)):
        glColor3f(*color)  # Set the color of the point
        glBegin(GL_POINTS)
        glVertex2f(int(x), int(y))  # Draw the point at the current position
        glEnd()
        x += x_inc  # Increment x by the calculated amount
        y += y_inc  # Increment y by the calculated amount

def draw_line_graph():
    """
    Draws a line graph by connecting data points using the DDA algorithm.
    """
    # Calculate spacing between points on the x-axis
    point_spacing = (WINDOW_WIDTH - 100) / (len(frequencies) - 1)  # Subtract margin

    # Determine scaling for y-axis based on maximum frequency
    max_freq = max(frequencies)
    y_scale = (WINDOW_HEIGHT - 100) / max_freq  # Subtract margin for top and bottom

    # Initial x and y positions
    x = 50  # Starting x-coordinate (with margin)
    prev_x, prev_y = x, 50 + frequencies[0] * y_scale  # Calculate the first point's position

    # Loop through frequencies and draw lines between consecutive points
    for freq in frequencies[1:]:
        x += point_spacing  # Move to the next x-coordinate
        y = 50 + freq * y_scale  # Calculate the scaled y-coordinate
        dda_line(prev_x, prev_y, x, y, LINE_COLOR)  # Draw a line from the previous point to the current point
        prev_x, prev_y = x, y  # Update the previous point for the next line segment

def display():
    """
    OpenGL display callback function.
    Clears the screen and draws the line graph.
    """
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_line_graph()  # Call the function to draw the graph
    glFlush()  # Ensure all OpenGL commands are executed

def init():
    """
    Initializes the OpenGL environment.
    Sets up the projection, background color, and coordinate system.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glMatrixMode(GL_PROJECTION)  # Set the matrix mode to projection
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Define the 2D orthographic projection

def main():
    """
    Main function to set up and run the OpenGL application.
    """
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set display mode (single buffer, RGB color)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  # Set window size
    glutCreateWindow(b"Line Graph using DDA")  # Create the window with a title
    init()  # Initialize the OpenGL environment
    glutDisplayFunc(display)  # Register the display callback function
    glutMainLoop()  # Start the main event loop

# Run the application
if __name__ == "__main__":
    main()
