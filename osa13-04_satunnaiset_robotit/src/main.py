# TEE RATKAISUSI TÄHÄN:

import pygame
from random import randint

pygame.init()
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))


for y in range(1000):
    x = randint(0, leveys-robo.get_width())
    y = randint(0, korkeus-robo.get_height())
    naytto.blit(robo, (x, y))


pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
