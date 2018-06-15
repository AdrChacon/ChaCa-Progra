import pygame, math

# Colores

Negro = (0,0,0)
Blanco = (255,255,255)
Gris_claro = (180,180,180)
Azul_claro = (0,0,255)
Rojo_claro = (255,0,0)
Verde_claro = (0,255,0)
Gris_oscuro = (150,150,150)
Azul_oscuro = (0,0,200)
Rojo_oscuro = (200,0,0)
Verde_oscuro = (0,200,0)
Amarillo_arena = (255,255,165)
Gris_carretera = (115,115,115)
Linea_Mitad = (125,125,125)
Linea_Meta = (1,1,1)
Derecha_Horizontal = (195,195,195)
Derecha_Vertical = (210, 210, 210)
Izquierda_Horizontal = (96,96,96)
Izquierda_Vertical = (101,101,101)

# Modulo Proyectiles
def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image,angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self, display, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(pygame.image.load('Image/Bala.png'), angle)
        self.image_orig = self.image
        self.rect = self.image.get_rect()
        self.speed = 15
        self.direction = angle
        self.pantalla = display
        self.x = x +14
        self.y = y +14

    def update(self):
##        self.image, self.rect = rot_center(self.image_orig, self.rect, self.direction)
##        print(self.pantalla.get_at((int(self.x),int(self.y))))
        if self.pantalla.get_at((int(self.x),int(self.y))) == Amarillo_arena:
            self.kill()
        if self.x+15 > 800 or self.x-15 < 0:
            self.kill()
        if self.y+15 > 600 or self.y-15 < 0:
            self.kill()
        self.x = self.x + self.speed * math.cos(math.radians(270-self.direction))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.direction))
        self.rect.x = self.x
        self.rect.y = self.y
        self.pantalla.blit(self.image, (self.x,self.y))
