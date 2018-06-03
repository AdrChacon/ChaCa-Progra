import pygame, math, json, random, time
from pygame.locals import *
from jugador import *
from menu import *
from proyectiles import *
from trafico import *
from mapa import *

pygame.init()

pygame.display.set_caption("Desert Mayhem")

# Definicion de colores

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


# Definicion de dimensiones de la pantalla

Largo_pantalla = 800
Alto_pantalla = 600
pantalla = pygame.display.set_mode((Largo_pantalla, Alto_pantalla))

# Definicion de reloj

Clock = pygame.time.Clock()

# Creacion de instancias

MenuIntro = Menu(Largo_pantalla, Alto_pantalla, pantalla)

# Lineas

HorizontalDerecha = pygame.image.load('LineaHRight.png')
HorizontalIzquierda = pygame.image.load('LineaHLeft.png')
VerticalDerecha = pygame.image.load('LineaVRight.png')
VerticalIzquierda = pygame.image.load('LineaVLeft.png')




def gameQuit():
    """Para salir del juego"""
    pygame.quit()
    quit()
    
def JugadorSprite(jugador,x,y):
    """Esta funcion maneja el dibujo de los jugadores en la pantalla del juego"""
    pantalla.blit(jugador.image, (x,y))

def PistaSprite(mapa ,x,y):
    """Esta funcion maneja el dibujo del mapa en la pantalla del juego"""
    pantalla.blit(mapa.image,(x,y))

def Dummyblit(Dummy, x, y):
    pantalla.blit(Dummy.image, (x,y))

def Meta(mapa):
    pantalla.blit(mapa.start, (mapa.startline[0],mapa.startline[1]))

def Mitad(mapa):
    pantalla.blit(mapa.halfline, (mapa.half[0]+35,mapa.half[1]))
    
##def Linea(mapa, )

def Mapa1():
    Pista = Mapa("PistaUno.png", 20,20, (30,280),(20,250), 1)
    Player_count(Pista)

def Mapa2():
    Pista = Mapa("PistaDos.png", 2,2, (16,366),(6,326), 2)
    Player_count(Pista)

def PlayerNames(jugadores, Pista):
    Names = True
    P2 = False
    if len(jugadores) == 2:
        P2 = True
    while Names:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                gameQuit()
        pantalla.fill(Blanco)
        
##    
    

def UnJugador(Arena):
    Pista = Arena[0]
    Jugador1 = Jugador("JugadorUno.png", Pista.P1start_position[0], Pista.P1start_position[1])
    P2 = False
    game_loop([Jugador1], Pista)

def DosJugadores(Arena):
    Pista = Arena[0]
    Jugador1 = Jugador("JugadorUno.png", Pista.P1start_position[0], Pista.P1start_position[1])
    Jugador2 = Jugador("JugadorDos.png", Pista.P2start_position[0], Pista.P2start_position[1])
    game_loop([Jugador1, Jugador2], Pista)
    
# Funcion para el menu principal

def game_intro():
    """Menu principal, aqui se puede empezar una partida o ver las mejores puntuaciones"""
    intro = True
    Arena = False
    Players = False
    Jugador1 = None
    Jugador2 = None
    Pista = None
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
        pantalla.fill(Blanco)
        MenuIntro.title("Desert Mayhem")
        MenuIntro.button("Empezar",Largo_pantalla*0.5-350,Alto_pantalla/2,200,50,Verde_oscuro,Verde_claro, game_map)
        MenuIntro.button("Ver Puntuacion",Largo_pantalla*0.5-100,Alto_pantalla/2,200,50,Azul_oscuro,Azul_claro, gameQuit)
        MenuIntro.button("Salir",Largo_pantalla*0.5+150,Alto_pantalla/2,200,50,Rojo_oscuro,Rojo_claro, gameQuit)
        pygame.display.update()
        Clock.tick(15)

# Funcion para cantidad de jugadores

def game_map():
    """En este menu el usuario puede elegir el mapa en el que desea jugar"""
    intro = False
    Arena = True
    Players = False
    Jugador1 = None
    Jugador2 = None
    time.sleep(0.15)
    while Arena:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
        pantalla.fill(Blanco)
        MenuIntro.infoText("Escoja el mapa")
        MenuIntro.button("Mapa 1", Largo_pantalla*0.5-250, Alto_pantalla/2, 100, 50, Gris_oscuro, Gris_claro, Mapa1)
        MenuIntro.button("Mapa 2", Largo_pantalla*0.5-100, Alto_pantalla/2, 100, 50, Gris_oscuro, Gris_claro, Mapa2)
        MenuIntro.button("No elegir", Largo_pantalla*0.5+100, Alto_pantalla/2, 100, 50, Gris_oscuro, Gris_claro, gameQuit)
        MenuIntro.button("No elegir", Largo_pantalla*0.5+250, Alto_pantalla/2, 100, 50, Gris_oscuro, Gris_claro, gameQuit)
        MenuIntro.button("Atras", Largo_pantalla*0.5, Alto_pantalla*0.25, 100, 50, Rojo_oscuro, Rojo_claro, game_intro)
        pygame.display.update()
        Clock.tick(15)

def Player_count(Arena):
    """Este menu permite al usuario elegir la cantidad de jugadores"""
    Players = True
    intro = False
    time.sleep(0.15)
    while Players:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
        pantalla.fill(Blanco)
        MenuIntro.infoText("Escoja cantidad de jugadores")
        MenuIntro.button("Un jugador", Largo_pantalla*0.5+100, Alto_pantalla*0.5, 150, 50, Verde_oscuro, Verde_claro, UnJugador, [Arena])
        MenuIntro.button("Dos jugadores", Largo_pantalla*0.5-100, Alto_pantalla*0.5, 150, 50, Verde_oscuro, Verde_claro, DosJugadores, [Arena])
        MenuIntro.button("Atras", Largo_pantalla*0.5-100, Alto_pantalla*0.25, 100, 50, Gris_oscuro, Gris_claro, game_map)
        MenuIntro.button("Menu", Largo_pantalla*0.5+100, Alto_pantalla*0.25, 100, 50, Rojo_oscuro, Rojo_claro, game_intro)
        pygame.display.update()
        Clock.tick(15)

def gameFinish(text):
    """Menu principal, aqui se puede empezar una partida o ver las mejores puntuaciones"""
    intro = True
    Arena = False
    Players = False
    Jugador1 = None
    Jugador2 = None
    Pista = None
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
        pantalla.fill(Blanco)
        MenuIntro.title(text)
        MenuIntro.button("Jugar Otra",Largo_pantalla*0.5-350,Alto_pantalla/2,200,50,Verde_oscuro,Verde_claro, game_map)
        MenuIntro.button("Ver Puntuacion",Largo_pantalla*0.5-100,Alto_pantalla/2,200,50,Azul_oscuro,Azul_claro, gameQuit)
        MenuIntro.button("Salir",Largo_pantalla*0.5+150,Alto_pantalla/2,200,50,Rojo_oscuro,Rojo_claro, gameQuit)
        pygame.display.update()
        Clock.tick(15)
        
        
        
# Funcion para el bucle principal

def game_loop(players, Pista):

    # Aqui se definen algunas variables que se utilizaran en el juego
    gameExit = False
    P2 = False
    P1vuelta = False
    P1Crashed = False
    PlayersCrashed = 0
    CrashMax = 1
    P1laps = 0
    MaxLaps = 3
    # Verifica si son dos jugadores y "activa" al segundo jugador
    if len(players) == 2:
        P2 = True
        CrashMax = 2
    # Variables especificas para el jugador 2, si esta activado
    if P2:
        P2laps = 0
        P2vuelta = False
        P2Crashed = False
    # Instancias de jugadores
    Jugador1 = players[0]
    if P2 == True:
        Jugador2 = players[1]
    # Se definen los drones para el mapa 1
    if Pista.mapnum == 1:
        Trafico1 = Dummy(0, 30, 240)
        Trafico2 = Dummy(180, 760,280)
        Trafico3 = Dummy(270,155, 500)
        Trafico4 = Dummy(90,400, 50)
    # Se definen los drones para el mapa 2
    if Pista.mapnum == 2:
        Trafico1 = Dummy(0,35, 300)
        Trafico2 = Dummy(90,500,30)
        Trafico3 = Dummy(180,735,300)
        Trafico4 = Dummy(270,500,550)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Logica del juego, aqui se controlan las vueltas que cada jugador ha completado, y lo que pasa cuando un jugador completa la carrera o si ambos jugadores se estrellan
        if PlayersCrashed == CrashMax:
            gameFinish('Perdiste')
        if P1laps == MaxLaps:
            gameFinish('Completado!')
        if P2 == True:
            if P2laps == MaxLaps:
                gameFinish('Completado!')
        if pantalla.get_at((int(Jugador1.x),int(Jugador1.y))) == Linea_Mitad:
            P1vuelta = True
        if (P1vuelta == True) and (pantalla.get_at((int(Jugador1.x),int(Jugador1.y))) == Linea_Meta):
            P1laps += 1
            P1vuelta = False
        if P2 == True:
            if pantalla.get_at((int(Jugador2.x),int(Jugador2.y))) == Linea_Mitad:
                P2vuelta = True
            if (P2vuelta == True) and (pantalla.get_at((int(Jugador2.x),int(Jugador2.y))) == Linea_Meta):
                P2laps += 1
                P2vuelta = False

        ## Control para los drones, cuando encuentran una linea, giran hacia la direccion indicada
        if Trafico1.direction == 0 or Trafico1.direction == 360 or Trafico1.direction == 180:
            if pantalla.get_at((Trafico1.x,Trafico1.y)) == Derecha_Horizontal:
                Trafico1.steerleft()
            if pantalla.get_at((Trafico1.x,Trafico1.y)) == Izquierda_Horizontal:
                Trafico1.steerright()
        if Trafico1.direction == 270 or Trafico1.direction == 90:
            if pantalla.get_at((Trafico1.x,Trafico1.y)) == Derecha_Vertical:
                Trafico1.steerleft()
            if pantalla.get_at((Trafico1.x,Trafico1.y)) == Izquierda_Vertical:
                Trafico1.steerright()
        if Trafico2.direction == 0 or Trafico2.direction == 360 or Trafico2.direction == 180:
            if pantalla.get_at((Trafico2.x,Trafico2.y)) == Derecha_Horizontal:
                Trafico2.steerleft()
            if pantalla.get_at((Trafico2.x,Trafico2.y)) == Izquierda_Horizontal:
                Trafico2.steerright()
        if Trafico2.direction == 270 or Trafico2.direction == 90:
            if pantalla.get_at((Trafico2.x,Trafico2.y)) == Derecha_Vertical:
                Trafico2.steerleft()
            if pantalla.get_at((Trafico2.x,Trafico2.y)) == Izquierda_Vertical:
                Trafico2.steerright()
        if Trafico3.direction == 0 or Trafico3.direction == 360 or Trafico3.direction == 180:
            if pantalla.get_at((Trafico3.x,Trafico3.y)) == Derecha_Horizontal:
                Trafico3.steerleft()
            if pantalla.get_at((Trafico3.x,Trafico3.y)) == Izquierda_Horizontal:
                Trafico3.steerright()
        if Trafico3.direction == 270 or Trafico3.direction == 90:
            if pantalla.get_at((Trafico3.x,Trafico3.y)) == Derecha_Vertical:
                Trafico3.steerleft()
            if pantalla.get_at((Trafico3.x,Trafico3.y)) == Izquierda_Vertical:
                Trafico3.steerright()
        if Trafico4.direction == 0 or Trafico4.direction == 360 or Trafico4.direction == 180:
            if pantalla.get_at((Trafico4.x,Trafico4.y)) == Derecha_Horizontal:
                Trafico4.steerleft()
            if pantalla.get_at((Trafico4.x,Trafico4.y)) == Izquierda_Horizontal:
                Trafico4.steerright()
        if Trafico4.direction == 270 or Trafico4.direction == 90:
            if pantalla.get_at((Trafico4.x,Trafico4.y)) == Derecha_Vertical:
                Trafico4.steerleft()
            if pantalla.get_at((Trafico4.x,Trafico4.y)) == Izquierda_Vertical:
                Trafico4.steerright()

        ## Controles de los jugadores, se definen las teclas que realizan cada accion; si se estrellan, se deshabilitan los controles.
        keys = pygame.key.get_pressed()

        # Jugador 1
        if P1Crashed != True:
            if keys[K_a]:
                Jugador1.steerleft()
            if keys[K_d]:
                Jugador1.steerright()
            if keys[K_w]:
                Jugador1.accelerate()
            else:
                Jugador1.soften()
            if keys[K_a]:
                Jugador1.deaccelerate()
            if pantalla.get_at((int(Jugador1.x),int(Jugador1.y))) == Amarillo_arena:
                    PlayersCrashed += 1
                    P1Crashed = True
        if P2 == True:
            # Jugador 2
            if P2Crashed != True:
                if keys[K_j]:
                    Jugador2.steerleft()
                if keys[K_l]:
                    Jugador2.steerright()
                if keys[K_i]:
                    Jugador2.accelerate()
                else:
                    Jugador2.soften()
                if keys[K_k]:
                    Jugador2.deaccelerate()
                if pantalla.get_at((int(Jugador2.x),int(Jugador2.y))) == Amarillo_arena:
                    PlayersCrashed += 1
                    P2Crashed = True
        # Aqui se maneja el movimiento de los sprites
        if P1Crashed != True:
            Jugador1.update()
        if P2 == True:
            if P2Crashed != True:
                Jugador2.update()
        Trafico1.update(Trafico1.x,Trafico1.y)
        Trafico2.update(Trafico2.x,Trafico2.y)
        Trafico3.update(Trafico3.x,Trafico3.y)
        Trafico4.update(Trafico4.x,Trafico4.y)

        
        # Aqui se realiza lo que es dibujo en la pantalla del juego y el reloj 
        pantalla.fill(Amarillo_arena)
        PistaSprite(Pista,Pista.x,Pista.y)
        Meta(Pista)
        Mitad(Pista)
        if Pista.mapnum == 1:
            pantalla.blit(HorizontalDerecha, (25,50))
            pantalla.blit(VerticalDerecha, (740,30))
            pantalla.blit(VerticalIzquierda, (600,350))
            pantalla.blit(HorizontalDerecha, (555,525))
            pantalla.blit(HorizontalDerecha, (670,400))
            pantalla.blit(VerticalDerecha, (325,450))
            pantalla.blit(HorizontalIzquierda,(275,340))
            pantalla.blit(VerticalIzquierda, (205,300))
            pantalla.blit(HorizontalDerecha, (155,525))
            pantalla.blit(VerticalDerecha, (45,450))
        if Pista.mapnum == 2:
            pantalla.blit(HorizontalDerecha, (25,50))
            pantalla.blit(VerticalDerecha, (740,30))
            pantalla.blit(HorizontalDerecha, (680,565))
            pantalla.blit(VerticalDerecha, (25,490))
        JugadorSprite(Jugador1,Jugador1.x,Jugador1.y)
        Dummyblit(Trafico1, Trafico1.x, Trafico1.y)
        Dummyblit(Trafico2, Trafico2.x, Trafico2.y)
        Dummyblit(Trafico3, Trafico3.x, Trafico3.y)
        Dummyblit(Trafico4, Trafico4.x, Trafico4.y)
        if P2 == True:
            JugadorSprite(Jugador2,Jugador2.x,Jugador2.y)
        pygame.display.flip()
        Clock.tick(60)

game_intro()
game_loop()
pygame.quit()
