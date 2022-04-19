# TEE RATKAISUSI TÄHÄN:
import pygame
from datetime import datetime
from math import pi, cos, sin

pygame.init()
leveys, korkeus = 640, 480
keskitaso = (leveys/2, korkeus/2)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 155)

naytto = pygame.display.set_mode((leveys, korkeus))
naytto.fill((0, 0, 0))
kello = pygame.time.Clock()


def viiva(r, theta):
    x = r * sin(pi * theta/180)
    y = r * cos(pi * theta/180)
    return x + 640 / 2, -(y - 480 / 2)


while True:
    pygame.draw.circle(naytto, (255, 0, 0), (320, 240), 220)
    pygame.draw.circle(naytto, (0, 0, 0), (320, 240), 215)
    pygame.draw.circle(naytto, (255, 0, 0), (320, 240), 10)

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    # titteli
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    pygame.display.set_caption(current_time)

    # aika muuttujat
    sekunnit = now.second
    minuutit = now.minute
    tunnit = now.hour

    # sekunnit viiva
    r = 200
    theta = sekunnit * (360 / 60)
    pygame.draw.line(naytto, DARK_BLUE, keskitaso, viiva(r, theta), 2)

    # minuutit viiva
    r = 200
    theta = (minuutit + sekunnit / 60) * (360 / 60)
    pygame.draw.line(naytto, BLUE, keskitaso, viiva(r, theta), 2)

    # tunnit viiva
    r = 150
    theta = (tunnit + minuutit / 60 + sekunnit / 3600) * (360 / 12)
    pygame.draw.line(naytto, BLUE, keskitaso, viiva(r, theta), 4)

    pygame.display.flip()
    kello.tick(60)
