from OpenGL.GL import *

def draw_cube(x, y, z, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glPushMatrix()
    glTranslatef(x, y, z)
    
    glBegin(GL_QUADS)
    
    # Top face
    glTexCoord2f(0, 0); glVertex3f(-20,  0.5, -20)
    glTexCoord2f(1, 0); glVertex3f( 20,  0.5, -20)
    glTexCoord2f(1, 1); glVertex3f( 20,  0.5,  20)
    glTexCoord2f(0, 1); glVertex3f(-20,  0.5,  20)
    
    glEnd()
    glPopMatrix()

def draw_box(x, y, z, width, height, depth, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glPushMatrix()
    glTranslatef(x, y, z)
    
    w = width / 2
    h = height / 2
    d = depth / 2

    glBegin(GL_QUADS)

    # Fața de sus
    glTexCoord2f(0, 0); glVertex3f(-w,  h, -d)
    glTexCoord2f(1, 0); glVertex3f( w,  h, -d)
    glTexCoord2f(1, 1); glVertex3f( w,  h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w,  h,  d)

    # Fața de jos
    glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f( w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f( w, -h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w, -h,  d)

    # Fața frontală
    glTexCoord2f(0, 0); glVertex3f(-w, -h,  d)
    glTexCoord2f(1, 0); glVertex3f( w, -h,  d)
    glTexCoord2f(1, 1); glVertex3f( w,  h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w,  h,  d)

    # Fața spate
    glTexCoord2f(0, 0); glVertex3f( w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f(-w,  h, -d)
    glTexCoord2f(0, 1); glVertex3f( w,  h, -d)

    # Fața stângă
    glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
    glTexCoord2f(1, 0); glVertex3f(-w, -h,  d)
    glTexCoord2f(1, 1); glVertex3f(-w,  h,  d)
    glTexCoord2f(0, 1); glVertex3f(-w,  h, -d)

    # Fața dreaptă
    glTexCoord2f(0, 0); glVertex3f( w, -h,  d)
    glTexCoord2f(1, 0); glVertex3f( w, -h, -d)
    glTexCoord2f(1, 1); glVertex3f( w,  h, -d)
    glTexCoord2f(0, 1); glVertex3f( w,  h,  d)

    glEnd()
    
    glPopMatrix()

def draw_road(texture):
            draw_box(-17, -0.5, 0,6,0,40, texture)
            draw_box(0, -0.5, -17,28,0,6, texture)
            draw_box(0, -0.5, 17,28,0,6, texture)
            draw_box(17, -0.5, 0,6,0,40, texture)



def draw_alley(texture):
        draw_box(-12,-0.5,-10.5,4,0.1,7,texture)
        draw_box(-12,-0.5,-3.5,4,0.1,7,texture)
        draw_box(-12,-0.5,3.5,4,0.1,7,texture)
        draw_box(-12,-0.5,10.5,4,0.1,7,texture)

        draw_box(-7.5,-0.5,-12,5,0.1,4,texture)
        draw_box(-2.5,-0.5,-12,5,0.1,4,texture)
        draw_box(2.5,-0.5,-12,5,0.1,4,texture)
        draw_box(7.5,-0.5,-12,5,0.1,4,texture)

        draw_box(-7.5,-0.5,12,5,0.1,4,texture)
        draw_box(-2.5,-0.5,12,5,0.1,4,texture)
        draw_box(2.5,-0.5,12,5,0.1,4,texture)
        draw_box(7.5,-0.5,12,5,0.1,4,texture)



        draw_box(12,-0.5,-10.5,4,0.1,7,texture)
        draw_box(12,-0.5,-3.5,4,0.1,7,texture)
        draw_box(12,-0.5,3.5,4,0.1,7,texture)
        draw_box(12,-0.5,10.5,4,0.1,7,texture)

def draw_center_grass(texture):
    step_x = 20 / 4  # Împărțim pe lățime în 4
    step_z = 20 / 2  # Împărțim pe lungime în 2
    
    for i in range(4):
        for j in range(2):
            x = -10 + i * step_x + step_x / 2
            z = -10 + j * step_z + step_z / 2
            draw_box(x, -0.5, z, step_x, 0, step_z, texture)



def draw_skybox_sides(texture):
    size = 20
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glBegin(GL_QUADS)

    # Fața față
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f(size, size, -size)
    glTexCoord2f(0, 1); glVertex3f(-size, size, -size)

    # Fața spate
    glTexCoord2f(0, 0); glVertex3f(size, -size, size)
    glTexCoord2f(1, 0); glVertex3f(-size, -size, size)
    glTexCoord2f(1, 1); glVertex3f(-size, size, size)
    glTexCoord2f(0, 1); glVertex3f(size, size, size)

    # Fața stânga
    glTexCoord2f(0, 0); glVertex3f(-size, -size, size)
    glTexCoord2f(1, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f(-size, size, -size)
    glTexCoord2f(0, 1); glVertex3f(-size, size, size)

    # Fața dreapta
    glTexCoord2f(0, 0); glVertex3f(size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(size, -size, size)
    glTexCoord2f(1, 1); glVertex3f(size, size, size)
    glTexCoord2f(0, 1); glVertex3f(size, size, -size)

    glEnd()

def draw_skybox_upper(texture):
    size = 20
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glBegin(GL_QUADS)

    # Fața sus
    glTexCoord2f(0, 0); glVertex3f(-size, size, -size)
    glTexCoord2f(1, 0); glVertex3f(size, size, -size)
    glTexCoord2f(1, 1); glVertex3f(size, size, size)
    glTexCoord2f(0, 1); glVertex3f(-size, size, size)

    # Fața jos
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f(size, -size, size)
    glTexCoord2f(0, 1); glVertex3f(-size, -size, size)

    glEnd()

def draw_box2(x, y, z, width, height, depth, texture):
    """ Desenează o cutie (dreptunghi 3D) la poziția (x, y, z) cu dimensiuni date. """
    glBindTexture(GL_TEXTURE_2D, texture)
    
    x1, x2 = x - width / 2, x + width / 2
    y1, y2 = y, y + height
    z1, z2 = z - depth / 2, z + depth / 2

    glBegin(GL_QUADS)

    # Fața față
    glTexCoord2f(0, 0); glVertex3f(x1, y1, z1)
    glTexCoord2f(1, 0); glVertex3f(x2, y1, z1)
    glTexCoord2f(1, 1); glVertex3f(x2, y2, z1)
    glTexCoord2f(0, 1); glVertex3f(x1, y2, z1)

    # Fața spate
    glTexCoord2f(0, 0); glVertex3f(x2, y1, z2)
    glTexCoord2f(1, 0); glVertex3f(x1, y1, z2)
    glTexCoord2f(1, 1); glVertex3f(x1, y2, z2)
    glTexCoord2f(0, 1); glVertex3f(x2, y2, z2)

    # Fața stânga
    glTexCoord2f(0, 0); glVertex3f(x1, y1, z2)
    glTexCoord2f(1, 0); glVertex3f(x1, y1, z1)
    glTexCoord2f(1, 1); glVertex3f(x1, y2, z1)
    glTexCoord2f(0, 1); glVertex3f(x1, y2, z2)

    # Fața dreapta
    glTexCoord2f(0, 0); glVertex3f(x2, y1, z1)
    glTexCoord2f(1, 0); glVertex3f(x2, y1, z2)
    glTexCoord2f(1, 1); glVertex3f(x2, y2, z2)
    glTexCoord2f(0, 1); glVertex3f(x2, y2, z1)

    # Fața sus
    glTexCoord2f(0, 0); glVertex3f(x1, y2, z1)
    glTexCoord2f(1, 0); glVertex3f(x2, y2, z1)
    glTexCoord2f(1, 1); glVertex3f(x2, y2, z2)
    glTexCoord2f(0, 1); glVertex3f(x1, y2, z2)

    # Fața jos
    glTexCoord2f(0, 0); glVertex3f(x1, y1, z1)
    glTexCoord2f(1, 0); glVertex3f(x2, y1, z1)
    glTexCoord2f(1, 1); glVertex3f(x2, y1, z2)
    glTexCoord2f(0, 1); glVertex3f(x1, y1, z2)

    glEnd()

def draw_house(x, y, z, width, height, depth, wall_texture, roof_texture, door_texture, window_texture):
    # Corpul casei
    draw_box2(x, y, z, width, height, depth, wall_texture)

    # Acoperiș - în formă de triunghi
    glBindTexture(GL_TEXTURE_2D, roof_texture)
    glBegin(GL_TRIANGLES)
    
    # Fața față acoperiș
    glTexCoord2f(0.5, 1); glVertex3f(x, y + height + 2, z - depth / 2)
    glTexCoord2f(0, 0); glVertex3f(x - width / 2, y + height, z - depth / 2)
    glTexCoord2f(1, 0); glVertex3f(x + width / 2, y + height, z - depth / 2)

    # Fața spate acoperiș
    glTexCoord2f(0.5, 1); glVertex3f(x, y + height + 2, z + depth / 2)
    glTexCoord2f(0, 0); glVertex3f(x - width / 2, y + height, z + depth / 2)
    glTexCoord2f(1, 0); glVertex3f(x + width / 2, y + height, z + depth / 2)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, roof_texture)
    glBegin(GL_QUADS)

    # Acoperiș lateral stânga
    glTexCoord2f(0, 0); glVertex3f(x - width / 2, y + height, z - depth / 2)
    glTexCoord2f(1, 0); glVertex3f(x - width / 2, y + height, z + depth / 2)
    glTexCoord2f(1, 1); glVertex3f(x, y + height + 2, z + depth / 2)
    glTexCoord2f(0, 1); glVertex3f(x, y + height + 2, z - depth / 2)

    # Acoperiș lateral dreapta
    glTexCoord2f(0, 0); glVertex3f(x + width / 2, y + height, z - depth / 2)
    glTexCoord2f(1, 0); glVertex3f(x + width / 2, y + height, z + depth / 2)
    glTexCoord2f(1, 1); glVertex3f(x, y + height + 2, z + depth / 2)
    glTexCoord2f(0, 1); glVertex3f(x, y + height + 2, z - depth / 2)

    glEnd()

    # Ușa (centrată pe fața din față, ridicată)
    door_height = (2 / 3) * height
    draw_box2(x, y - height / 6 + height * 0.1, z - depth / 2 - 0.01, width / 5, door_height, 0.1, door_texture)

    # Geamuri (mai sus)
    window_size = width / 5
    window_y = y + height / 3  # Ridicate mai sus

    draw_box2(x - width / 3, window_y, z - depth / 2 - 0.01, window_size, window_size, 0.1, window_texture)
    draw_box2(x + width / 3, window_y, z - depth / 2 - 0.01, window_size, window_size, 0.1, window_texture)


