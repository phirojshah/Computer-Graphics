from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables for input points
point1 = None
point2 = None

def bresenham_line(x0, y0, x1, y1):
    """
    Draws a line using Bresenham's Line Drawing Algorithm with the decision parameter.
    
    Args:
        x0, y0: Starting coordinates of the line
        x1, y1: Ending coordinates of the line
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1  # Direction for x
    sy = 1 if y0 < y1 else -1  # Direction for y

    if dx > dy:  # Case: |m| < 1
        p = 2 * dy - dx  # Initial decision parameter
        while x0 != x1:
            glBegin(GL_POINTS)
            glVertex2f(x0, y0)
            glEnd()

        if p < 0:  # If P_k < 0
            p += 2 * dy  # Update P_k+1 = P_k + 2Δy
            x0 += sx  # x_i+1 = x_i + 1
        else:  # If P_k >= 0
            p += 2 * dy - 2 * dx  # Update P_k+1 = P_k + 2Δy - 2Δx
            y0 += sy  # y_i+1 = y_i + 1
            x0 += sx  # x_i+1 = x_i + 1


    else:  # Case: |m| >= 1
        p = 2 * dx - dy  # Initial decision parameter
    while y0 != y1:
        glBegin(GL_POINTS)
        glVertex2f(x0, y0)
        glEnd()

        if p < 0:  # If P_k < 0
            p += 2 * dx  # Update P_k+1 = P_k + 2Δx
            y0 += sy  # y_i+1 = y_i + 1
        else:  # If P_k >= 0
            p += 2 * dx - 2 * dy  # Update P_k+1 = P_k + 2Δx - 2Δy
            x0 += sx  # x_i+1 = x_i + 1
            y0 += sy  # y_i+1 = y_i + 1


    # Plot the final point
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    glEnd()

def display():
    """
    OpenGL display function to draw the line.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Line color: white

    # Draw the line using Bresenham's algorithm
    bresenham_line(*point1, *point2)

    glFlush()

def init():
    """
    Initialize OpenGL settings.
    """
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background: black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set up the orthographic projection
    max_x = max(point1[0], point2[0]) + 50
    max_y = max(point1[1], point2[1]) + 50
    gluOrtho2D(0, max_x, 0, max_y)

def main():
    """
    Main function to run the OpenGL program.
    """
    global point1, point2

    # User input for points
    print("Enter coordinates for the first point (x0, y0):")
    point1 = tuple(map(int, input("x0, y0: ").split(',')))
    print("Enter coordinates for the second point (x1, y1):")
    point2 = tuple(map(int, input("x1, y1: ").split(',')))

    # Initialize GLUT
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Bresenham Line Drawing Algorithm")

    # Initialize OpenGL settings
    init()

    # Register the display callback function
    glutDisplayFunc(display)

    # Enter the GLUT main loop
    glutMainLoop()

if __name__ == "__main__":
    main()
