import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from camera import Camera
from elements import *
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
glClearColor(0.0, 0.0, 0.0, 1.0)  # Cerul complet negru (noapte)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, 800 / 600, 0.1, 100)
glMatrixMode(GL_MODELVIEW)

# Inițializare cameră & texturi
camera = Camera()
grass_texture = load_texture("grass.jpg")
sky_texture = load_texture("sky.jpg")
asphalt_texture = load_texture("asphalt.jpg")
concrete_texture = load_texture("sidewalk.jpg")
window_texture = load_texture("window.jpg")
wall_texture = load_texture("wall.jpg")
roof_texture = load_texture("roof.jpg")
sides_texture = load_texture("sidebox.jpg")
metal_texture = load_texture("metal.jpg")
green_metal_texture = load_texture("green_metal.jpg")
bench_texture = load_texture("bench.jpg")
light_texture = load_texture("light.jpg")
can_texture = load_texture("can.jpg")

setup_input(window, camera)

# Activăm iluminarea
glEnable(GL_LIGHTING)
glDisable(GL_LIGHT0)  # Dezactivăm soarele
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.02, 0.02, 0.02, 1.0])  # Lumină ambientală minimă (aproape negru)

glEnable(GL_COLOR_MATERIAL)  # Permite obiectelor să aibă culori naturale

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    camera.update()
    draw_road(asphalt_texture)
    draw_alley(concrete_texture)
    draw_skybox_sides(sides_texture)
    draw_skybox_upper(sky_texture)
    draw_center_grass(grass_texture)
    draw_houses(wall_texture, roof_texture, window_texture)
    draw_center_alley(concrete_texture)
    draw_street_lamps(green_metal_texture, green_metal_texture, light_texture)
    draw_benches(bench_texture)
    draw_trash_can(1.5, -1, -3, can_texture)
    draw_trash_can(1.5, -0.5, 3, can_texture)
    draw_trash_can(-1.5, -0.5, -3, can_texture)
    draw_trash_can(-1.5, -0.5, 3, can_texture)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
