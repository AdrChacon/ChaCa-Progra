import pygame, math, json, random, time
from pygame.locals import *
from jugador import *
from menu import *
from proyectiles import *
from trafico import *
from mapa import *
from obstaculos import *

pygame.init()

pygame.display.set_caption("Desert Mayhem")

# Definicion de sonidos y canales

Idle = pygame.mixer.Sound('Sound/TruckIdle2.wav')
Drive = pygame.mixer.Sound('Sound/TankAccelerate2.wav')
Explode = pygame.mixer.Sound('Sound/BOOM.wav')
revChannel1 = pygame.mixer.Channel(1)
revChannel2 = pygame.mixer.Channel(2)
revChannel3 = pygame.mixer.Channel(3)

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

# Definicion de grupos de sprites

ListaDrones = pygame.sprite.Group()
ListaMinas = pygame.sprite.Group()
ListaSprites = pygame.sprite.Group()

# Definicion de reloj

Clock = pygame.time.Clock()

# Creacion de instancias

MenuIntro = Menu(Largo_pantalla, Alto_pantalla, pantalla)

# Lineas

HorizontalDerecha = pygame.image.load('Image/LineaHRight.png')
HorizontalIzquierda = pygame.image.load('Image/LineaHLeft.png')
VerticalDerecha = pygame.image.load('Image/LineaVRight.png')
VerticalIzquierda = pygame.image.load('Image/LineaVLeft.png')

# Definicion de los mapas

Mapa1 = ("Image/PistaUno.png", 20,20, (30,280),(20,250), 1)
Mapa2 = ("Image/PistaDos.png", 2,2, (16,366),(6,326), 2)
Mapa3 = ("Image/PistaTres.png", 2,2, (16,366),(6,326), 3)


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
    """Funcion para dibujar a los drones"""
    pantalla.blit(Dummy.image, (x,y))

def Meta(mapa):
    """Funcion para dibujar la linea de meta"""
    pantalla.blit(mapa.start, (mapa.startline[0],mapa.startline[1]))

def Mitad(mapa):
    """Funcion para dibujar la linea en la mitad de la pista"""
    pantalla.blit(mapa.halfline, (mapa.half[0]+35,mapa.half[1]))
    
def Mapa1():
    """Esta funcion elige una pista al azar"""
    Pista = random.choice([Mapa("Image/PistaTres.png", 2,2, (16,366),(6,326), 3),Mapa("Image/PistaDos.png", 2,2, (16,366),(6,326), 2),Mapa("Image/PistaUno.png", 20,20, (30,280),(20,250), 1)])
    Player_count(Pista)
    

def UnJugador(Arena):
    """Funcion para generar 1 jugador"""
    Pista = Arena[0]
    Jugador1 = Jugador("Image/JugadorUno.png", Pista.P1start_position[0], Pista.P1start_position[1])
    P2 = False
    game_loop([Jugador1], Pista, 0, 0)

def DosJugadores(Arena):
    """Funcion para generar 2 jugadores"""
    Pista = Arena[0]
    Jugador1 = Jugador("Image/JugadorUno.png", Pista.P1start_position[0], Pista.P1start_position[1])
    Jugador2 = Jugador("Image/JugadorDos.png", Pista.P2start_position[0], Pista.P2start_position[1])
    game_loop([Jugador1, Jugador2], Pista,0 , 0)
    
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
        MenuIntro.button("Empezar",Largo_pantalla*0.5-350,Alto_pantalla/2,200,50,Verde_oscuro,Verde_claro, Mapa1)
        MenuIntro.button("Ver Puntuacion",Largo_pantalla*0.5-100,Alto_pantalla/2,200,50,Azul_oscuro,Azul_claro, gameQuit)
        MenuIntro.button("Salir",Largo_pantalla*0.5+150,Alto_pantalla/2,200,50,Rojo_oscuro,Rojo_claro, gameQuit)
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
        MenuIntro.button("Atras", Largo_pantalla*0.5-100, Alto_pantalla*0.25, 100, 50, Gris_oscuro, Gris_claro, game_intro)
        pygame.display.update()
        Clock.tick(15)

def gameFinish(text):
    """Menu principal pero con diferente texto, se muestra despues de cada partida, aqui se puede empezar una partida o ver las mejores puntuaciones"""
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
        MenuIntro.button("Jugar Otra",Largo_pantalla*0.5-350,Alto_pantalla/2,200,50,Verde_oscuro,Verde_claro, Mapa1)
        MenuIntro.button("Ver Puntuacion",Largo_pantalla*0.5-100,Alto_pantalla/2,200,50,Azul_oscuro,Azul_claro, gameQuit)
        MenuIntro.button("Salir",Largo_pantalla*0.5+150,Alto_pantalla/2,200,50,Rojo_oscuro,Rojo_claro, gameQuit)
        pygame.display.update()
        Clock.tick(15)
        
# Funcion para el bucle principal

def game_loop(players, Pista, score1, score2):

    # Aqui se definen algunas variables que se utilizaran en el juego
    gameExit = False
    P2 = False
    P1vuelta = False
    P1Crashed = False
    P1Laps = 0
    PlayersCrashed = 0
    CrashMax = 1
    PuntuacionP1 = score1
    MaxLaps = 2

    # Aqui se generan los obstaculos
    for i in range(random.randint(2,32)):
        Mina = Mine(20, 20)
        Mina.rect.x = random.randrange(Largo_pantalla)
        Mina.rect.y = random.randrange(Alto_pantalla)
        ListaMinas.add(Mina)
        ListaSprites.add(Mina)
        
    # Verifica si son dos jugadores y "activa" al segundo jugador
    if len(players) == 2:
        P2 = True
        PuntuacionP2 = 0
        CrashMax = 2
        
    # Variables especificas para el jugador 2, si esta activado
    if P2:
        P2vuelta = False
        P2Crashed = False
        P2Laps = 0
    # Instancias de jugadores
    Jugador1 = players[0]
    ListaSprites.add(Jugador1)
    if P2 == True:
        Jugador2 = players[1]
        ListaSprites.add(Jugador2)

##    lista_impacto_minas = pygame.sprite.spritecollide(Jugador1, ListaMinas, True)
    # Se definen los drones para el mapa 1

    if Pista.mapnum == 1:
        Trafico1 = Dummy(0, 30, 240)
        Trafico2 = Dummy(180, 760,280)
        Trafico3 = Dummy(270,155, 500)
        Trafico4 = Dummy(90,400, 50)
        ListaDrones.add(Trafico1)
        ListaDrones.add(Trafico2)
        ListaDrones.add(Trafico3)
        ListaDrones.add(Trafico4)
        ListaSprites.add(Trafico1)
        ListaSprites.add(Trafico2)
        ListaSprites.add(Trafico3)
        ListaSprites.add(Trafico4)
    # Se definen los drones para el mapa 2
    if Pista.mapnum == 2:
        Trafico1 = Dummy(0,35, 300)
        Trafico2 = Dummy(90,500,30)
        Trafico3 = Dummy(180,735,300)
        Trafico4 = Dummy(270,500,550)
        ListaDrones.add(Trafico1)
        ListaDrones.add(Trafico2)
        ListaDrones.add(Trafico3)
        ListaDrones.add(Trafico4)
        ListaSprites.add(Trafico1)
        ListaSprites.add(Trafico2)
        ListaSprites.add(Trafico3)
        ListaSprites.add(Trafico4)
    if Pista.mapnum == 3:
        Trafico1 = Dummy(0,35,300)
        Trafico2 = Dummy(90,400,30)
        Trafico3 = Dummy(180,735,300)
        Trafico4 = Dummy(270,500,550)
        ListaDrones.add(Trafico1)
        ListaDrones.add(Trafico2)
        ListaDrones.add(Trafico3)
        ListaDrones.add(Trafico4)
        ListaSprites.add(Trafico1)
        ListaSprites.add(Trafico2)
        ListaSprites.add(Trafico3)
        ListaSprites.add(Trafico4)
        
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Logica del juego, aqui se controlan las vueltas que cada jugador ha completado, y lo que pasa cuando un jugador completa la carrera o si ambos jugadores se estrellan
        if PlayersCrashed == CrashMax:
            revChannel1.stop()
            ListaDrones.empty()
            ListaSprites.empty
            ListaMinas.empty()
            if P2 == True:
                gameFinish('Nadie Gana :(')
            else:
                gameFinish('Perdiste')
        if P2 == True:
            if P1Laps > MaxLaps:
                PuntuacionP1 += 400
                if PuntuacionP1 > PuntuacionP2:
                    gameFinish('Rojo Gana!')
                elif PuntuacionP2 > PuntuacionP1:
                    gameFinish('Azul Gana!')
            if P2Laps > MaxLaps:
                PuntuacionP2 += 400
                if PuntuacionP1 > PuntuacionP2:
                    gameFinish('Rojo Gana!')
                elif PuntuacionP2 > PuntuacionP1:
                    gameFinish('Azul Gana!')
        elif P1Laps == MaxLaps:
            gameFinish('Completado!')
        if pantalla.get_at((int(Jugador1.x),int(Jugador1.y))) == Linea_Mitad:
            P1vuelta = True
        if (P1vuelta == True) and (pantalla.get_at((int(Jugador1.x),int(Jugador1.y))) == Linea_Meta):
            PuntuacionP1 += 200
            P1Laps += 1
            P1vuelta = False
        if P2 == True:
            if pantalla.get_at((int(Jugador2.x),int(Jugador2.y))) == Linea_Mitad:
                P2vuelta = True
            if (P2vuelta == True) and (pantalla.get_at((int(Jugador2.x),int(Jugador2.y))) == Linea_Meta):
                PuntuacionP2 += 200
                P2Laps += 1
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

        lista_impacto_minas_P1 = pygame.sprite.spritecollide(Jugador1, ListaMinas, True)
        if P2 == True:
            lista_impacto_minas_P2 = pygame.sprite.spritecollide(Jugador2, ListaMinas, True)

        # Jugador 1
        if P1Crashed != True:
            # Girar a la izquierda
            if keys[K_a]:
                Jugador1.steerleft()
            # Girar a la derecha
            if keys[K_d]:
                Jugador1.steerright()
            # Acelerar
            if keys[K_w]:
                PuntuacionP1 += 2
                revChannel1.play(Drive)
                Jugador1.accelerate()
            else:
                if Jugador1.speed == 0:
                    revChannel1.play(Idle)
                Jugador1.soften() # Neutro
            # Reversa
            if keys[K_s]:
                Jugador1.deaccelerate()
            if pantalla.get_at((int(Jugador1.x),int(Jugador1.y))) == Amarillo_arena:
                    PuntuacionP1 -= 8
            if PuntuacionP1 < 0:
                PuntuacionP1 = 0
                PlayersCrashed += 1
                P1Crashed = True
            for mina in lista_impacto_minas_P1:
                revChannel2.play(Explode)
                PuntuacionP1 -= 400
                Jugador1.speed = 0
        if P2 == True:
            # Jugador 2
            if P2Crashed != True:
                # Girar a la izquierda
                if keys[K_j]:
                    Jugador2.steerleft()
                # Girar a la derecha
                if keys[K_l]:
                    Jugador2.steerright()
                # Acelerar
                if keys[K_i]:
                    PuntuacionP2 += 2
                    revChannel3.play(Drive)
                    Jugador2.accelerate()
                else:
                    if Jugador2.speed == 0:
                        revChannel3.play(Idle)
                    Jugador2.soften() # Neutro
                # Reversa
                if keys[K_k]:
                    Jugador2.deaccelerate()
                if pantalla.get_at((int(Jugador2.x),int(Jugador2.y))) == Amarillo_arena:
                    PuntuacionP2 -= 8
                if PuntuacionP2 < 0:
                    PuntuacionP2 = 0
                    PlayersCrashed += 1
                    P2Crashed = True
                for mina in lista_impacto_minas_P2:
                    revChannel2.play(Explode)
                    PuntuacionP2 -= 400
                    Jugador2.speed = 0
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

##        print(Clock.get_time)
##        print("score1:", PuntuacionP1)
##        print(ListaMinas.sprites())
##        print(Jugador1.rect.x, Jugador1.rect.y)
##        print(ListaSprites.sprites())
##        print(pygame.mouse.get_pos())
##        print(lista_impacto_minas)
##        if P2 == True:
##            print("score2:", PuntuacionP2)

        
        # Aqui se realiza lo que es dibujo en la pantalla del juego y el reloj 
        pantalla.fill(Amarillo_arena)
        PistaSprite(Pista,Pista.x,Pista.y)

        # Impresion de puntaje y vueltas completadas en el espacio vacio de cada mapa
        # Para mapa 1
        if Pista.mapnum == 1:
            MenuIntro.ScoreDisplay(280, 155,"Jugador 1:",int(PuntuacionP1))
            MenuIntro.ScoreDisplay(520, 155, "Vueltas 3/", P1Laps)
            if P2 == True:
                MenuIntro.ScoreDisplay(280, 175,"Jugador 2:",PuntuacionP2)
                MenuIntro.ScoreDisplay(520, 175, "Vueltas 3/", P2Laps)
        # Para mapa 2
        if Pista.mapnum == 2:
            MenuIntro.ScoreDisplay(280, 155,"Jugador 1:",int(PuntuacionP1))
            MenuIntro.ScoreDisplay(520, 155, "Vueltas 3/", P1Laps)
            if P2 == True:
                MenuIntro.ScoreDisplay(280, 175,"Jugador 2:",PuntuacionP2)
                MenuIntro.ScoreDisplay(520, 175, "Vueltas 3/", P2Laps)
        # Para mapa 3
        if Pista.mapnum == 3:
            MenuIntro.ScoreDisplay(280, 355,"Jugador 1:",int(PuntuacionP1))
            MenuIntro.ScoreDisplay(520, 355, "Vueltas 3/", P1Laps)
            if P2 == True:
                MenuIntro.ScoreDisplay(280, 375,"Jugador 2:",PuntuacionP2)
                MenuIntro.ScoreDisplay(520, 375, "Vueltas 3/", P2Laps)
        Meta(Pista)
        Mitad(Pista)

        # Esto maneja las impresion de las lineas de las "curvas" de cada mapa para que los drones giren
        # Para mapa 1
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
        # Para mapa 2
        if Pista.mapnum == 2:
            pantalla.blit(HorizontalDerecha, (25,50))
            pantalla.blit(VerticalDerecha, (740,30))
            pantalla.blit(HorizontalDerecha, (680,565))
            pantalla.blit(VerticalDerecha, (25,490))
        # Para mapa 3
        if Pista.mapnum == 3:
            pantalla.blit(HorizontalDerecha, (25,50))
            pantalla.blit(VerticalDerecha, (740,30))
            pantalla.blit(HorizontalDerecha, (680,565))
            pantalla.blit(VerticalDerecha, (25,490))
            pantalla.blit(VerticalDerecha,(220,20))
            pantalla.blit(VerticalDerecha,(465,20))
            pantalla.blit(VerticalIzquierda,(620,208))
            pantalla.blit(VerticalIzquierda,(320,208))
            pantalla.blit(HorizontalDerecha,(270,40))
            pantalla.blit(HorizontalDerecha,(570,40))
            pantalla.blit(HorizontalIzquierda,(160,285))
            pantalla.blit(HorizontalIzquierda,(420,285))
        ListaMinas.draw(pantalla)
        ListaMinas.update()
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
