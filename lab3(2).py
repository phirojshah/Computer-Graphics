from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to plot points in all four quadrants
def plot_ellipse_points(x_center, y_center, x, y):
    glBegin(GL_POINTS)
    # Quadrant 1: Top-right
    glVertex2i(x_center + x, y_center + y)
    # Quadrant 2: Bottom-right
    glVertex2i(x_center + x, y_center - y)
    # Quadrant 3: Bottom-left
    glVertex2i(x_center - x, y_center - y)
    # Quadrant 4: Top-left
    glVertex2i(x_center - x, y_center + y)
    glEnd()

# Midpoint Ellipse Drawing Algorithm
def midpoint_ellipse(x_center, y_center, rx, ry):
    x = 0
    y = ry
    rx2 = rx * rx  # rx^2
    ry2 = ry * ry  # ry^2
    tworx2 = 2 * rx2
    twory2 = 2 * ry2

    # Decision parameter for Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    dx = twory2 * x
    dy = tworx2 * y

    # Region 1: Slope < 1
    while dx < dy:
        plot_ellipse_points(x_center, y_center, x, y)
        if p1 < 0:  # Move horizontally
            x += 1
            dx += twory2
            p1 += dx + ry2
        else:  # Move diagonally
            x += 1
            y -= 1
            dx += twory2
            dy -= tworx2
            p1 += dx - dy + ry2

    # Decision parameter for Region 2
    p2 = (ry2 * (x + 0.5) * (x + 0.5)) + (rx2 * (y - 1) * (y - 1)) - (rx2 * ry2)

    # Region 2: Slope >= 1
    while y >= 0:
        plot_ellipse_points(x_center, y_center, x, y)
        if p2 > 0:  # Move vertically
            y -= 1
            dy -= tworx2
            p2 += rx2 - dy
        else:  # Move diagonally
            x += 1
            y -= 1
            dx += twory2
            dy -= tworx2
            p2 += dx - dy + rx2

# Draw coordinate axes
def draw_axes():
    glBegin(GL_LINES)
    # X-axis (Red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(-400, 0)
    glVertex2i(400, 0)
    # Y-axis (Green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(0, -300)
    glVertex2i(0, 300)
    glEnd()

# Display callback function
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1.0, 1.0, 1.0)  # Set ellipse color to white
    draw_axes()  # Draw axes
    midpoint_ellipse(0, 0, 100, 200)  # Adjust rx to 100 and ry to 200 for a vertical ellipse
    glFlush()


# OpenGL initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black
    glColor3f(1.0, 1.0, 1.0)  # Set drawing color to white
    glPointSize(2.0)  # Set point size
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)  # Set up a 2D orthographic viewing region

# Main function
def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffer and RGB mode
    glutInitWindowSize(800, 600)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position on screen
    glutCreateWindow(b"Midpoint Ellipse Drawing Algorithm")  # Create window with title
    init()  # Initialize OpenGL settings
    glutDisplayFunc(display)  # Set display callback
    glutMainLoop()  # Enter the GLUT main loop

# Run the program
if __name__ == "__main__":
    main()
