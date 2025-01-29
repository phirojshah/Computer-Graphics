import glfw
import OpenGL.GL as gl
import numpy as np
import math

# Base OpenGL class for setting up the window
class OpenGLTransformer:
    def __init__(self, width=800, height=600):
        if not glfw.init():
            raise Exception("GLFW can't be initialized!")

        self.width = width
        self.height = height
        self.window = glfw.create_window(width, height, "2D Transformations", None, None)

        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can't be created!")

        glfw.make_context_current(self.window)
        gl.glOrtho(-400, 400, -300, 300, -1, 1)  # Setting up a 2D coordinate system

# Combined Transformer class
class CombinedTransformer(OpenGLTransformer):
    def __init__(self, points, width=800, height=600):
        super().__init__(width, height)
        self.original_points = np.array(points)
        self.transformed_points = self.original_points.copy()

    # Draw the coordinate axes
    def draw_axes(self):
        gl.glBegin(gl.GL_LINES)
        gl.glColor3f(1.0, 1.0, 1.0)  # White
        # X-axis
        gl.glVertex2f(-400, 0)
        gl.glVertex2f(400, 0)
        # Y-axis
        gl.glVertex2f(0, -300)
        gl.glVertex2f(0, 300)
        gl.glEnd()

    # Draw a polygon (triangle in this case)
    def draw_polygon(self, points, color):
        gl.glColor3f(*color)
        gl.glBegin(gl.GL_LINE_LOOP)
        for point in points:
            gl.glVertex2f(point[0], point[1])
        gl.glEnd()

    # Apply translation
    def translate(self, tx, ty):
        translation_matrix = np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ])
        self.apply_transformation(translation_matrix)

    # Apply rotation
    def rotate(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        rotation_matrix = np.array([
            [math.cos(angle_radians), -math.sin(angle_radians), 0],
            [math.sin(angle_radians), math.cos(angle_radians), 0],
            [0, 0, 1]
        ])
        self.apply_transformation(rotation_matrix)

    # Apply scaling
    def scale(self, sx, sy):
        scaling_matrix = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ])
        self.apply_transformation(scaling_matrix)

    # General transformation application
    def apply_transformation(self, transformation_matrix):
        homogeneous_points = np.column_stack((self.transformed_points, np.ones(len(self.transformed_points))))
        transformed_homogeneous = (transformation_matrix @ homogeneous_points.T).T
        self.transformed_points = transformed_homogeneous[:, :2]

    # Main loop
    def run(self):
        while not glfw.window_should_close(self.window):
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            # Draw axes
            self.draw_axes()

            # Draw original and transformed shapes
            self.draw_polygon(self.original_points, (0, 0, 1))  # Blue: Original shape
            self.draw_polygon(self.transformed_points, (1, 0, 0))  # Red: Transformed shape

            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()

# Main function
def main():
    # Define the initial triangle vertices
    triangle_points = [[0, 0], [100, 0], [50, 100]]

    transformer = CombinedTransformer(triangle_points)

    while True:
        print("\nChoose a transformation:")
        print("1. Translation")
        print("2. Rotation")
        print("3. Scaling")
        print("4. Reset")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:  # Translation
            tx = float(input("Enter translation in X (tx): "))
            ty = float(input("Enter translation in Y (ty): "))
            transformer.translate(tx, ty)
        elif choice == 2:  # Rotation
            angle = float(input("Enter rotation angle in degrees: "))
            transformer.rotate(angle)
        elif choice == 3:  # Scaling
            sx = float(input("Enter scaling factor in X (sx): "))
            sy = float(input("Enter scaling factor in Y (sy): "))
            transformer.scale(sx, sy)
        elif choice == 4:  # Reset
            transformer.transformed_points = transformer.original_points.copy()
        elif choice == 5:  # Exit
            break
        else:
            print("Invalid choice! Please try again.")
            continue

        transformer.run()  # Refresh the display after transformation

if __name__ == "__main__":
    main()
