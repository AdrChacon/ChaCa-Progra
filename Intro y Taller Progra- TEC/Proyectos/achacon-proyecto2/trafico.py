import pygame, random, math

# Modulo para el trafico
def rot_center(image,rect,angle):
    """Esta funcion controla la rotacion de la imagen y el bloque que
    representan al vehiculo dummy"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

class Dummy(pygame.sprite.Sprite):
    """Esta es la clase para los drones"""
    def __init__(self, angle, x, y):
        """Aqui se definen varios atributos como la velocidad, el angulo, la imagen
        y la magnitud de los giros"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Image/Trafico.png")
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.speed = 2
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
        if self.direction == 90:
            self.x = self.x + self.speed
            self.y = self.y
            self.rect.x = self.x
            self.rect.y = self.y
        if self.direction == 180:
            self.x = self.x
            self.y = self.y + self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        if self.direction == 270:
            self.x = self.x - self.speed
            self.y = self.y
            self.rect.x = self.x
            self.rect.y = self.y
