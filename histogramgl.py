from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BAR_WIDTH = 50
BAR_GAP = 0  # Reduced gap between bars to zero

# Data for histogram
frequencies = [30, 50, 20, 60, 40, 70, 10, 35, 45, 55]

# Colors for histogram lines (normalized to 0-1 for OpenGL)
LINE_COLORS = [
    (140/255, 19/255, 185/255), (52/255, 60/255, 147/255), (0/255, 128/255, 0/255), 
    (255/255, 69/255, 0/255), (255/255, 215/255, 0/255), (255/255, 20/255, 147/255),
    (0/255, 191/255, 255/255), (255/255, 105/255, 180/255), (128/255, 128/255, 128/255), 
    (0/255, 0/255, 0/255)
]

def bresenham_line(x1, y1, x2, y2, color):
    """
    Draws a line using Bresenham's Line Algorithm.
    Args:
        x1, y1: Starting coordinates of the line
        x2, y2: Ending coordinates of the line
        color: RGB tuple for the color of the line
    """
    dx = x2 - x1
    dy = y2 - y1
    dx1 = 2 * dx
    dy1 = 2 * dy
    two_dx1 = 2 * dx1
    two_dy1 = 2 * dy1

    if dx < 0:
        dx = -dx
        sx = -1
    else:
        sx = 1

    if dy < 0:
        dy = -dy
        sy = -1
    else:
        sy = 1

    if dx > dy:
        p = dy1 - dx
        while x1 != x2:
            glColor3f(*color)
            glBegin(GL_POINTS)
            glVertex2f(x1, y1)
            glEnd()
            x1 += sx
            if p >= 0:
                y1 += sy
                p -= two_dx1
            p += two_dy1
    else:
        p = dx1 - dy
        while y1 != y2:
            glColor3f(*color)
            glBegin(GL_POINTS)
            glVertex2f(x1, y1)
            glEnd()
            y1 += sy
            if p >= 0:
                x1 += sx
                p -= two_dy1
            p += two_dx1

def draw_histogram():
    """
    Draws the histogram bars using Bresenham's line algorithm.
    """
    x = 14  # Starting x-coordinate for the bars
    max_freq = max(frequencies)
    
    for freq, color in zip(frequencies, LINE_COLORS):
        # Scale the frequency to fit the window height
        bar_height = freq * (WINDOW_HEIGHT - 100) / max_freq
        # Draw the vertical line using Bresenham's algorithm (bar from bottom to top)
        bresenham_line(x, 50, x, 50 + bar_height, color)  
        x += BAR_WIDTH + BAR_GAP  # Space between bars

def init():
    """
    Initialize OpenGL environment.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background to white
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Set 2D orthographic projection

def display():
    """
    OpenGL display callback function.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    draw_histogram()  # Draw the histogram
    glFlush()  # Ensure the drawing is rendered

def main():
    """
    Main function to set up the OpenGL application.
    """
    glutInit(sys.argv)  # Initialize GLUT with the command line arguments
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Histogram using OpenGL and Bresenham's Line Algorithm")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
