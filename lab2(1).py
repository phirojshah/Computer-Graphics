from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#Digital Differential Analyzer
# Global variables for points
point1 = None
point2 = None

def dda_line(x0, y0, x1, y1):
    """
    Draws a line using the DDA algorithm with OpenGL.
    """
    # Calculate the difference in x and y
    dx = x1 - x0
    dy = y1 - y0
    
    # Determine the larger magnitude for step size
    step_size = max(abs(dx), abs(dy))
    
    # Calculate increments using the larger magnitude
    x_inc = dx / step_size
    y_inc = dy / step_size
    
    # Initialize starting point
    x, y = x0, y0

    # Begin OpenGL drawing
    glBegin(GL_POINTS) #rendering points
    for _ in range(int(step_size) + 1):  # Include both start and end points
        glVertex2f(round(x), round(y))  # Plot the current point
        x += x_inc  # Increment x
        y += y_inc  # Increment y
    glEnd()

def display():
    """
    OpenGL display function to draw the line.
    """
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    # Draw the line using DDA
    dda_line(*point1, *point2)

    glFlush()  # Ensure the rendering commands are executed

def init():
    """
    Initialize the OpenGL environment.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set orthographic projection to accommodate the points
    max_x = max(point1[0], point2[0]) + 50
    max_y = max(point1[1], point2[1]) + 50
    gluOrtho2D(0, max_x, 0, max_y)

def main():
    """
    Main function to run the OpenGL application.
    """
    global point1, point2

    # Input points
    print("Enter coordinates for the first point (x1, y1):")
    point1 = tuple(map(int, input("x1, y1: ").split(',')))
    print("Enter coordinates for the second point (x2, y2):")
    point2 = tuple(map(int, input("x2, y2: ").split(',')))

    # Initialize GLUT
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"DDA Line Drawing with OpenGL")

    # Initialize OpenGL environment
    init()

    # Register display callback
    glutDisplayFunc(display)

    # Start the GLUT main loop
    glutMainLoop()

if __name__ == "__main__":
    main()
