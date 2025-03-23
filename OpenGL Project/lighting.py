from OpenGL.GL import *
from OpenGL.GLU import *
from elements import *
def setup_sunlight():
    glEnable(GL_LIGHTING)  # Activează iluminarea globală
    glEnable(GL_LIGHT0)    # Activează sursa de lumină principală

    # Poziția luminii (un colț al skybox-ului, dar puțin mai în interior)
    light_position = [15.0, 18.0, -15.0, 0.0]  # Ultimul parametru 0.0 => directională
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Direcția luminii (bate în jos și ușor spre centru)
    light_direction = [-1.0, -0.5, 1.0, 0.0]  # Direcție oblică spre scenă
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, light_direction)

    # Setări pentru intensitatea luminii
    light_ambient = [0.2, 0.2, 0.2, 1.0]   # Lumină difuză soft
    light_diffuse = [1.0, 0.9, 0.7, 1.0]   # Alb-gălbui, ca soarele
    light_specular = [1.0, 1.0, 1.0, 1.0]  # Reflexii puternice

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # Activează iluminarea pentru materiale
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    print("☀️ Lumina solară configurată corect!")
