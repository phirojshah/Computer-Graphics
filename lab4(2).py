from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import math

# Window dimensions
width, height = 800, 800


# Function to rotate a point (x, y) around the origin by a given angle
def rotate_point(x, y, angle):
    rad = math.radians(angle)
    cos_theta = math.cos(rad)
    sin_theta = math.sin(rad)
    
    # Apply 2D rotation matrix
    x_new = x * cos_theta - y * sin_theta
    y_new = x * sin_theta + y * cos_theta
    return x_new, y_new


# Draw a blade (rectangle) with rotation
def draw_blade(x, y, width, height, angle):
    # Define rectangle points
    vertices = [
        (-width / 2, 0),  # Bottom left
        (width / 2, 0),   # Bottom right
        (width / 2, height),  # Top right
        (-width / 2, height),  # Top left
    ]
    
    # Apply rotation and draw
    glBegin(GL_POLYGON)
    glColor3f(0.4, 0.7, 1.0)  # Sky blue for blades
    for vx, vy in vertices:
        vx_rot, vy_rot = rotate_point(vx + x, vy + y, angle)
        glVertex2f(vx_rot, vy_rot)
    glEnd()


# Draw the windmill with blades and the stand
def draw_windmill(x, y, blade_angle):
    # Draw the stand (windmill base)
    glColor3f(0.8, 0.6, 0.4)  # Light brown/tan for the stand
    glBegin(GL_POLYGON)
    glVertex2f(x - 0.05, y - 0.5)  # Bottom left
    glVertex2f(x + 0.05, y - 0.5)  # Bottom right
    glVertex2f(x + 0.05, y)        # Top right
    glVertex2f(x - 0.05, y)        # Top left
    glEnd()

    # Draw the center (hub) of the windmill
    glColor3f(1.0, 0.8, 0.0)  # Golden yellow hub
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = math.radians(i)
        cx = x + 0.05 * math.cos(theta)
        cy = y + 0.05 * math.sin(theta)
        glVertex2f(cx, cy)
    glEnd()

    # Draw blades (4 blades at 90-degree intervals)
    for i in range(4):
        angle = blade_angle + i * 90
        draw_blade(x, y, 0.02, 0.3, angle)


# Main drawing function to clear the screen and render the windmill
def draw(blade_angle):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()  # Reset the modelview matrix
    draw_windmill(0, 0, blade_angle)  # Draw the windmill at the center
    glFlush()


# Main function to set up the window and run the simulation
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a window
    window = glfw.create_window(width, height, "Windmill Simulation with Appealing Colors", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    gluOrtho2D(-1, 1, -1, 1)  # Set up a 2D orthographic projection

    # Initial rotation angle
    blade_angle = 0

    # Speed factor (adjust for different speeds)
    speed = 2  # Adjust this value to change speed (e.g., 1 for slow, 5 for fast)

    # Main rendering loop
    while not glfw.window_should_close(window):
        glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
        glClear(GL_COLOR_BUFFER_BIT)

        # Update angle for the blade
        blade_angle += speed  # Speed determines how fast the blades rotate
        if blade_angle >= 360:
            blade_angle -= 360

        # Draw the windmill
        draw(blade_angle)

        # Swap buffers and poll for events
        glfw.swap_buffers(window)
        glfw.poll_events()

        # Listen for key presses to adjust speed
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            speed += 1  # Increase speed
        elif glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            speed = max(1, speed - 1)  # Decrease speed but keep it >= 1

    glfw.terminate()


# Run the main function
if __name__ == "__main__":
    main()
