import pygame
import sys
import random

pygame.init()

ANCHO = 600
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de pygame")

background = pygame.image.load('bg_space2.png')

pygame.mixer.music.load("INZO - L.E.O.mp3")
pygame.mixer.music.play(loops=-1)

bolita_imagen = pygame.image.load("Daco_4483923.png")
bolita_imagen = pygame.transform.scale(bolita_imagen, (30, 30))
bolita_radio = 15
bolita_posicion = [ANCHO // 2, ALTO - 2 * bolita_radio]
bolita_velocidad = 12

objetos_caida = []
objeto_imagen = pygame.image.load("8bit-Cartoon-PNG-Clipart.png")
objeto_imagen = pygame.transform.scale(objeto_imagen, (30, 30))
objeto_ancho = 30
objeto_alto = 30

tiempo_transcurrido = 0
velocidad_inicial_objetos = 5
aceleracion_objetos = 0.4

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and bolita_posicion[0] > bolita_radio:
        bolita_posicion[0] -= bolita_velocidad
    if teclas[pygame.K_RIGHT] and bolita_posicion[0] < ANCHO - bolita_radio:
        bolita_posicion[0] += bolita_velocidad

    if random.randint(0, 100) < 5:
        objeto_posicion = [random.randint(0, ANCHO - objeto_ancho), 0]
        objetos_caida.append(objeto_posicion)

    for objeto in objetos_caida:
        objeto[1] += velocidad_inicial_objetos + tiempo_transcurrido * aceleracion_objetos

    objetos_caida = [objeto for objeto in objetos_caida if objeto[1] < ALTO]

    for objeto in objetos_caida:
        objeto_rect = pygame.Rect(objeto[0], objeto[1], objeto_ancho, objeto_alto)
        if objeto_rect.colliderect((bolita_posicion[0] - bolita_radio, bolita_posicion[1] - bolita_radio, 2 * bolita_radio, 2 * bolita_radio)):
            print("¡Game Over!")
            pygame.quit()
            sys.exit()

    ventana.blit(background, (0, 0))

    ventana.blit(bolita_imagen, (bolita_posicion[0] - bolita_radio, bolita_posicion[1] - bolita_radio))

    for objeto in objetos_caida:
        ventana.blit(objeto_imagen, (objeto[0], objeto[1]))

    pygame.display.flip()

    reloj.tick(30)
    tiempo_transcurrido += 1 / 30
