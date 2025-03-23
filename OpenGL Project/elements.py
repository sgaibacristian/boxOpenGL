from OpenGL.GL import *
from OpenGL.GLU import *

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
def draw_center_alley(texture):
             draw_box(-5,-0.5,0,10,0.1,4,texture)
             draw_box(5,-0.5,0,10,0.1,4,texture)
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

def draw_house(x, y, z, width, height, depth, wall_texture, roof_texture, door_texture, window_texture, rotation):
    glPushMatrix()  # Salvează matricea de transformare curentă
    glTranslatef(x, y, z)  # Mută casa la poziția inițială
    glRotatef(rotation, 0, 1, 0)  # Rotește în jurul axei Y
    glTranslatef(-x, -y, -z)  # Revine la poziția corectă după rotație

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

    glPopMatrix()  # Restaurează matricea originală

def draw_street_lamp(x, y, z, base_texture, pole_texture, lamp_texture, light_id):
    # Baza stâlpului
    glBindTexture(GL_TEXTURE_2D, base_texture)
    draw_box(x, y, z, 0.75, 0.25, 0.75, base_texture)

    # Corpul stâlpului
    glBindTexture(GL_TEXTURE_2D, pole_texture)
    draw_box(x, y + 1.25, z, 0.15, 4, 0.15, pole_texture)

    # Brațul stâlpului
    glPushMatrix()
    glTranslatef(x, y + 3.25, z)
    glBindTexture(GL_TEXTURE_2D, pole_texture)
    draw_box(0, 0, 0, 0.1, 0.1, 1.5, pole_texture)
    glPopMatrix()

    # Lămpile (sfere)
    lamp_positions = [
        (x, y + 3.0, z - 0.75),
        (x, y + 3.0, z + 0.75)
    ]

    glBindTexture(GL_TEXTURE_2D, lamp_texture)

    for pos in lamp_positions:
        glPushMatrix()
        glTranslatef(*pos)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)

        # **Facem sfera luminoasă**
        glMaterialfv(GL_FRONT, GL_EMISSION, [1.0, 1.0, 0.6, 1.0])  # Sferă luminoasă
        gluSphere(quadric, 0.35, 20, 20)
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0, 1.0])  # Revenim la normal

        gluDeleteQuadric(quadric)
        glPopMatrix()

        # Setăm lumina exact în sferă și direcționată în jos
        if light_id <= GL_LIGHT7:
            glEnable(light_id)
            light_pos = [pos[0], pos[1], pos[2], 1.0]  # Poziție exactă în sferă
            light_dir = [0.0, -1.0, 0.0]  # Lumina direcționată direct în jos

            # **Configurare lumină mai intensă**
            light_diffuse = [1.5, 1.5, 1.2, 1.0]  # Intensitate crescută
            light_specular = [1.0, 1.0, 0.8, 1.0]  # Reflexii puternice
            light_ambient = [0.05, 0.05, 0, 0.05]  # Puțină lumină ambientală

            glLightfv(light_id, GL_POSITION, light_pos)
            glLightfv(light_id, GL_DIFFUSE, light_diffuse)
            glLightfv(light_id, GL_SPECULAR, light_specular)
            glLightfv(light_id, GL_AMBIENT, light_ambient)

            # **Configurăm lumina ca spot light, dar mai puțin direcționată**
            glLightf(light_id, GL_SPOT_CUTOFF, 40.0)  # Răspândire puțin mai largă
            glLightfv(light_id, GL_SPOT_DIRECTION, light_dir)
            glLightf(light_id, GL_SPOT_EXPONENT, 5.0)  # Mai puțin concentrată

            # Atenuare moderată
            glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0.3)

            light_id += 1  # Următoarea lumină


def draw_street_lamps(base_texture, mid_texture, sphere_texture):
    light_id = GL_LIGHT1  # Începem de la GL_LIGHT1

    positions = [
        (9, -0.5, 3),
        (0, -0.5, 3),
        (-9, -0.5, 3),
        (9, -0.5, -3),
        (0, -0.5, -3),
        (-9, -0.5, -3),
    ]

    for pos in positions:
        draw_street_lamp(*pos, base_texture, mid_texture, sphere_texture, light_id)
        light_id += 2  # Fiecare stâlp are două lămpi


def draw_bench(x, y, z, bench_texture, rotate_180=False):
    glPushMatrix()

    # Aplică rotația doar dacă e necesar
    if rotate_180:
        glTranslatef(x, y, z)
        glRotatef(180, 0, 1, 0)
        glTranslatef(-x, -y, -z)

    # Scaunul băncii
    glBindTexture(GL_TEXTURE_2D, bench_texture)
    draw_box(x, y, z, 3.0, 0.2, 0.8, bench_texture)

    # Spătarul băncii
    glBindTexture(GL_TEXTURE_2D, bench_texture)
    draw_box(x, y + 0.4, z - 0.3, 3.0, 0.6, 0.2, bench_texture)

    # Picioarele băncii (negre) - fără textură
    glColor3f(0, 0, 0)  # Negru
    draw_box(x - 1.25, y - 0.6, z, 0.15, 1.2, 0.15, 0)
    draw_box(x + 1.25, y - 0.6, z, 0.15, 1.2, 0.15, 0)

    # Resetare culoare la alb pentru alte obiecte
    glColor3f(1, 1, 1)

    glPopMatrix()


def draw_houses(wall_texture,roof_texture,window_texture):
    draw_house(-8, -0.5,-8,4,3,4,wall_texture,roof_texture,window_texture,window_texture,0)
    draw_house(0, -0.5,-8,4,3,4,wall_texture,roof_texture,window_texture,window_texture,0)
    draw_house(8, -0.5,-8,4,3,4,wall_texture,roof_texture,window_texture,window_texture,0)

    draw_house(-8, -0.5,8,4,3,4,wall_texture,roof_texture,window_texture,window_texture,180)
    draw_house(0, -0.5,8,4,3,4,wall_texture,roof_texture,window_texture,window_texture,180)
    draw_house(8, -0.5,8,4,3,4,wall_texture,roof_texture,window_texture,window_texture,180)

def draw_benches(bench_texture):
    draw_bench(4, 0, -3, bench_texture)
    draw_bench(-4, 0, -3, bench_texture )
    draw_bench(4, 0, 3, bench_texture, True)
    draw_bench(-4, 0, 3, bench_texture, True)

def draw_trash_can(x, y, z, can_texture):
    # Coșul de gunoi (cilindru)
    glBindTexture(GL_TEXTURE_2D, can_texture)
    glPushMatrix()
    glTranslatef(x, y, z)  # Lăsăm cilindrul direct pe sol
    glRotatef(-90, 1, 0, 0)  # Rotește cilindrul pentru a sta vertical

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, 0.25, 0.25, 1.2, 20, 20)  # Cilindru de bază
    gluDeleteQuadric(quadric)

    glPopMatrix()

