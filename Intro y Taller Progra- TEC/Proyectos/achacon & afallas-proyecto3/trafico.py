import pygame, random, math

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

# Modulo para el trafico
def rot_center(image,rect,angle):
    """Esta funcion controla la rotacion de la imagen y el bloque que
    representan al vehiculo dummy"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

class Dummy(pygame.sprite.Sprite):
    """Esta es la clase para los drones"""
    def __init__(self, screen, angle, x, y):
        """Aqui se definen varios atributos como la velocidad, el angulo, la imagen
        y la magnitud de los giros"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Image/Trafico.png")
        self.pantalla = screen
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.speed = 1
        self.direction = angle
        self.steering = 90
        self.x = x
        self.y = y

    def steerleft(self):
        """Giros hacia la izquierda"""
        self.direction = self.direction+self.steering
        if self.direction > 360:
            self.direction = 0+90
        self.image, self.rect = rot_center(self.image_orig,self.rect,self.direction)

    def steerright(self):
        """Giros hacia la derecha"""
        self.direction = self.direction-self.steering
        if self.direction < 0:
            self.direction = 360-90
        self.image, self.rect = rot_center(self.image_orig,self.rect,self.direction)

    def update(self,last_x, last_y):
        """Movimiento de los drones"""
        if self.direction == 0 or self.direction == 360:
            self.x = self.x
            self.y = self.y - self.speed
            self.rect.x = self.x
            self.rect.y = self.y
            if self.pantalla.get_at((self.x, self.y)) == Derecha_Horizontal:
                self.steerleft()
            if self.pantalla.get_at((self.x, self.y)) == Izquierda_Horizontal:
                self.steerright()
        if self.direction == 90:
            self.x = self.x + self.speed
            self.y = self.y
            self.rect.x = self.x
            self.rect.y = self.y
            if self.pantalla.get_at((self.x, self.y)) == Derecha_Vertical:
                self.steerleft()
            if self.pantalla.get_at((self.x, self.y)) == Izquierda_Vertical:
                self.steerright()
        if self.direction == 180:
            self.x = self.x
            self.y = self.y + self.speed
            self.rect.x = self.x
            self.rect.y = self.y
            if self.pantalla.get_at((self.x, self.y)) == Derecha_Horizontal:
                self.steerleft()
            if self.pantalla.get_at((self.x, self.y)) == Izquierda_Horizontal:
                self.steerright()
        if self.direction == 270:
            self.x = self.x - self.speed
            self.y = self.y
            self.rect.x = self.x
            self.rect.y = self.y
            if self.pantalla.get_at((self.x, self.y)) == Derecha_Vertical:
                self.steerleft()
            if self.pantalla.get_at((self.x, self.y)) == Izquierda_Vertical:
                self.steerright()
