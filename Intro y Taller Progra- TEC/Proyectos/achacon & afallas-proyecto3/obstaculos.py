import pygame

class Mine(pygame.sprite.Sprite):
    """Clase para las minas (obstaculos)"""
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("Image/Mina.png")
        self.rect = self.image.get_rect()
