import glfw
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self):
        self.x, self.y, self.z = 0, 1.5, 10
        self.yaw, self.pitch = 0, 0
        self.speed = 0.1
        self.movement = {glfw.KEY_W: False, glfw.KEY_S: False, glfw.KEY_A: False, glfw.KEY_D: False}
    
    def update(self):
        glLoadIdentity()
        direction_x = np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        direction_y = np.sin(np.radians(self.pitch))
        direction_z = np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))

        target_x = self.x + direction_x
        target_y = self.y + direction_y
        target_z = self.z + direction_z

        gluLookAt(self.x, self.y, self.z, target_x, target_y, target_z, 0, 1, 0)

        move_x, move_z = 0, 0
        forward_x = np.cos(np.radians(self.yaw))
        forward_z = np.sin(np.radians(self.yaw))
        right_x = np.cos(np.radians(self.yaw - 90))
        right_z = np.sin(np.radians(self.yaw - 90))

        if self.movement[glfw.KEY_W]:
            move_x += forward_x * self.speed
            move_z += forward_z * self.speed
        if self.movement[glfw.KEY_S]:
            move_x -= forward_x * self.speed
            move_z -= forward_z * self.speed
        if self.movement[glfw.KEY_A]:
            move_x += right_x * self.speed
            move_z += right_z * self.speed
        if self.movement[glfw.KEY_D]:
            move_x -= right_x * self.speed
            move_z -= right_z * self.speed

        new_x = self.x + move_x
        new_z = self.z + move_z
        limit = 19

        if -limit < new_x < limit:
            self.x = new_x
        if -limit < new_z < limit:
            self.z = new_z

camera = Camera()
