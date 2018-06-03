import pygame, math

Negro = (0,0,0)
Blanco = (255,255,255)

# Modulo Menu

##pantalla = pygame.display.set_mode()

def text_objects(text, font):
        textSurface = font.render(text, True, Negro)
        return textSurface, textSurface.get_rect()


class Menu(pygame.sprite.Sprite):
    def __init__(self, Dw, Dh, pantalla):
        """Aqui se definen varios atributos de los menus"""
        pygame.sprite.Sprite.__init__(self)
        self.Dw = Dw
        self.Dh = Dh
        self.LargeText = pygame.font.Font('freesansbold.ttf', 90)
        self.smallText = pygame.font.Font('freesansbold.ttf', 20)
        self.pantalla = pantalla

    def title(self, text):
        """Funcion para los titulos"""
        TextSurfL, TextRectL = text_objects(text, (self.LargeText))
        TextRectL.center = ((self.Dw/2),(self.Dh*0.2))
        self.pantalla.blit(TextSurfL, TextRectL)

    def infoText(self, text):
        """Funcion para el texto informativo"""
        TextSurfS, TextRectS = text_objects(text, (self.smallText))
        TextRectS.center = ((self.Dw/2),(self.Dh*0.2))
        self.pantalla.blit(TextSurfS, TextRectS)

    
    def button(self, text, x, y, w, h, ic, ac, action=None , params=None):
        """Funcion para los botones"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.pantalla, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                if params != None:
                    action(params)
                else:
                    action()
        else:
            pygame.draw.rect(self.pantalla, ic, (x,y,w,h))
        TextSurfS, TextRectS = text_objects(text, self.smallText)
        TextRectS.center = ((x+w/2),(y+h/2))
        self.pantalla.blit(TextSurfS, TextRectS)
