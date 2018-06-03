import pygame, math

# Modulo Proyectiles
def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image,angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self, display, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bala.png')
        self.image_orig = self.image
        self.rect = self.image.get_rect()
        self.speed = 15
        self.direction = direction
        self.pantalla = display
        self.x = x
        self.y = y

    def boom(self):
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.direction)
        self.x = self.x + self.speed * math.cos(math.radians(270-self.direction))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.direction))
