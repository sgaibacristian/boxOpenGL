import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from camera import Camera
from elements import draw_road, draw_skybox_sides, draw_alley,draw_center_grass,draw_house,draw_skybox_upper
from textures import load_texture
from input import setup_input

# Inițializare GLFW
if not glfw.init():
    raise Exception("failed to initialize glfw")

window = glfw.create_window(2560, 1600, "OpenGL", None, None)
if not window:
    glfw.terminate()
    raise Exception("failed to create window")

glfw.make_context_current(window)
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

# Setări OpenGL
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glEnable(GL_TEXTURE_2D)
glClearColor(0.5, 0.7, 1.0, 1.0)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, 800 / 600, 0.1, 100)
glMatrixMode(GL_MODELVIEW)

# init camera & textures
camera = Camera()
grass_texture = load_texture("grass.jpg")
sky_texture = load_texture("sky.jpg")
asphalt_texture = load_texture("asphalt.jpg")
concrete_texture = load_texture("sidewalk.jpg")
window_texture = load_texture("window.jpg")
wall_texture = load_texture("wall.jpg")
roof_texture = load_texture("roof.jpg")
sides_texture = load_texture("sidebox.jpg")
setup_input(window, camera)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    camera.update()
    draw_road(asphalt_texture)
    draw_alley(concrete_texture)
    draw_skybox_sides(sides_texture)
    draw_skybox_upper(sky_texture)
    draw_center_grass(grass_texture)
    draw_house(0, -0.5, 0, 4, 3, 4,wall_texture,roof_texture,window_texture,window_texture)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
