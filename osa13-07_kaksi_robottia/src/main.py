# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x1 = 0
x2 = 0
nopeus1 = 1
nopeus2 = 2
leveys = 640
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    x1 += nopeus1
    if x1 == 0 or x1+robo.get_width() == leveys:
        nopeus1 = -nopeus1
    x2 += nopeus2
    if x2 == 0 or x2+robo.get_width() == leveys:
        nopeus2 = -nopeus2

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x1, 50))
    naytto.blit(robo, (x2, 200))
    pygame.display.flip()

    kello.tick(120)
