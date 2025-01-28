import glfw
from OpenGL.GL import *
from math import pi, cos, sin

# Initialize GLFW and set up window
def initialize_glfw():
    # Initialize the library
    if not glfw.init():
        raise Exception("Failed to initialize GLFW")

    # Get primary monitor and its video mode (resolution)
    primary_monitor = glfw.get_primary_monitor()
    video_mode = glfw.get_video_mode(primary_monitor)

    # Print resolution of the display
    print(f"Resolution: {video_mode.size.width} * {video_mode.size.height}")

    # Create a fullscreen window with the resolution
    window = glfw.create_window(video_mode.size.width, video_mode.size.height, "Nepal Tourism Board Logo", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")

    return window

# Function to draw a circle
def draw_circle(radius, segments):
    glBegin(GL_TRIANGLE_FAN) #circle by drawing multiple connected triangles.
    glVertex2f(0, 0)  # Center point
    for i in range(segments + 1):
        theta = 2.0 * pi * i / segments
        x = radius * cos(theta)
        y = radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

# Function to draw a rectangle centered at (x, y)
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x - width / 2, y - height / 2)
    glVertex2f(x + width / 2, y - height / 2)
    glVertex2f(x + width / 2, y + height / 2)
    glVertex2f(x - width / 2, y + height / 2)
    glEnd()

# Function to draw filled arc
def draw_filled_arc(outer_radius, inner_radius, start_angle, end_angle, segments):
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(segments + 1):
        angle = start_angle + (end_angle - start_angle) * i / segments
        outer_x = outer_radius * cos(angle)
        outer_y = outer_radius * sin(angle)
        glVertex2f(outer_x, outer_y)
        inner_x = inner_radius * cos(angle)
        inner_y = inner_radius * sin(angle)
        glVertex2f(inner_x, inner_y)
    glEnd()

# Function to draw the "N" logo with arcs
def draw_logo():
    glColor3f(1.0, 0.0, 0.0)  # Red color
    draw_rect(-60.0, 0.0, 50.0, 200.0)  # Left vertical of "N"
    draw_rect(60.0, 0.0, 50.0, 200.0)  # Right vertical of "N"
    draw_rect(0.0, 0.0, 360.0, 40.0)  # Horizontal line of "N"

    # Diagonal part of "N"
    glBegin(GL_QUADS)
    glVertex2f(-85.0, 100.0)
    glVertex2f(-35.0, 100.0)
    glVertex2f(85.0, -100.0)
    glVertex2f(35.0, -100.0)
    glEnd()

    # Draw surrounding arcs
    draw_filled_arc(180.0, 150.0, pi / 6, pi, 500)
    draw_filled_arc(180.0, 150.0, 7 * pi / 6, 2 * pi, 500)

# Main loop to set up OpenGL context and render logo
def main():
    window = initialize_glfw()
    glfw.make_context_current(window)

    # Set background to white
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Set up 2D orthographic projection
    width, height = glfw.get_window_size(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-width / 2.0, width / 2.0, -height / 2.0, height / 2.0, -1.0, 1.0)

    # Main rendering loop
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)  # Clear screen

        # Draw the logo
        draw_logo()

        glfw.swap_buffers(window)  # Swap buffers for double buffering
        glfw.poll_events()  # Poll for events

    glfw.terminate()  # Terminate when done

if __name__ == "__main__":
    main()
