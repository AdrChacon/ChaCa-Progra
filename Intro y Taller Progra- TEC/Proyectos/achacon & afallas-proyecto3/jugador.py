import pygame, math, random
from proyectiles import *

##pygame.init()

def rot_center(image,rect,angle):
    """Esta funcion controla la rotacion de la imagen y el bloque que
    representan al jugador"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

class Jugador(pygame.sprite.Sprite):
    """Los jugadores: Aqui se definen las funciones y propiedades que controlan
    a los vehiculos de los jugadores"""
    def __init__(self, image, x, y):
        """Aqui se definen varias propiedades de los jugadores, como la imagen,
        la velocidad, aceleracion, direccion, la x y la y, velocidad maxima/minima
        velocidad de viraje y cantidad de balas"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.speed = 0
        self.acceleration = 0.5
        self.deacceleration = 1
        self.direction = 0
        self.max_speed = 8
        self.min_speed = -2
        self.x = x
        self.y = y
        self.steering = 10
        self.softening = 0.5
        self.balas = 4
        self.last = pygame.time.get_ticks()
        self.cooldown = 2000

    def soften(self):
        """Esta funcion evita que los jugadores se detengan bruscamente cuando
        dejan de presionar el boton de avanzar"""
        if self.speed > 0:
            self.speed -= self.softening
        if self.speed < 0:
            self.speed += self.softening

    def accelerate(self):
        """Funcion que maneja la aceleracion para el vehiculo del jugador"""
        if self.speed < self.max_speed:
            self.speed = self.speed + self.acceleration

    def deaccelerate(self):
        """Funcion que maneja la desaceleracion para el vehiculo del jugador"""
        if self.speed > self.min_speed:
            self.speed = self.speed - self.deacceleration
    def steerleft(self):
        """Esta funcion maneja el viraje hacia la izquierda"""
        self.direction = self.direction+self.steering
        if self.direction > 360:
            self.direction = 0
        self.image, self.rect = rot_center(self.image_orig,self.rect,self.direction)
    def steerright(self):
        """Esta el viraje hacia la derecha"""
        self.direction = self.direction-self.steering
        if self.direction < 0:
            self.direction = 360
        self.image, self.rect = rot_center(self.image_orig,self.rect,self.direction)
    def update(self):
        """Esta funcion modifica la x y la y del jugador, con esto se maneja
        la magnitud y direccion del movimiento"""
        self.x = self.x + self.speed * math.cos(math.radians(270-self.direction))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.direction))
        self.rect.x = self.x
        self.rect.y = self.y
