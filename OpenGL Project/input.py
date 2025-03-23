import glfw

previous_x, previous_y = 400, 300  

def setup_input(window, camera):
    """Setează input-ul și transmite camera"""
    glfw.set_key_callback(window, lambda w, k, s, a, m: key_callback(w, k, s, a, m, camera))
    glfw.set_cursor_pos_callback(window, lambda w, x, y: mouse_callback(w, x, y, camera))

def key_callback(window, key, scancode, action, mods, camera):
    if key in camera.movement:
        if action == glfw.PRESS:
            camera.movement[key] = True
        elif action == glfw.RELEASE:
            camera.movement[key] = False

def mouse_callback(window, xpos, ypos, camera):
    global previous_x, previous_y  
    dx = xpos - previous_x
    dy = previous_y - ypos
    previous_x, previous_y = xpos, ypos  
    camera.yaw += dx * 0.1  
    camera.pitch += dy * 0.1
    camera.pitch = max(-89, min(89, camera.pitch))
