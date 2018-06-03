import pygame, math

# Modulo Mapa

class Mapa(pygame.sprite.Sprite):
    """En esta clase se definen las propiedades y algunas funciones
    relacionadas con las pistas del juego"""
    def __init__(self, image, x, y, st_position, st_line, mapnum):
        """Aqui se definen varias propiedades de cada mapa, como
        la imagen, la x y la y para que el mapa este centrado,
        la posicion inicial de los jugadores"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.start = pygame.image.load('Linea.png')
        self.halfline = pygame.image.load('LineaMitad.png')
        self.x = x
        self.y = y
        self.P1start_position = st_position
        self.P2start_position = st_position[0]+50,st_position[1]
        self.startline = st_line
        self.half = 670-st_line[0], st_line[1]
        self.mapnum = mapnum
