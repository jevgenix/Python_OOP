# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")


kulma = 0
leveys = 320
korkeus = 240

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))

    for i in range(1, 11):
        kulman_koko = 2 * math.pi/10
        x = 320+math.cos(kulma+kulman_koko*i)*150-robo.get_width()/2
        y = 240+math.sin(kulma+kulman_koko*i)*150-robo.get_height()/2

        naytto.blit(robo, (x, y))

    pygame.display.flip()
    kulma += 0.01
    kello.tick(60)
