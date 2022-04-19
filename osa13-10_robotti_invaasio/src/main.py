# TEE RATKAISUSI TÄHÄN:
import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x_pos = random.sample(range(0, 600), 50)
y_pos = random.sample(range(-1080, 0), 50)


leveys, korkeus = 640, 480
nopeus = 5

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))

    for i in range(len(x_pos)):
        naytto.blit(robo, (x_pos[i], y_pos[i]))
        y_pos[i] += nopeus

        if y_pos[i]+robo.get_height() >= korkeus:
            y_pos[i] -= nopeus
            if x_pos[i] > 320:
                x_pos[i] += nopeus
            if x_pos[i] < 320:
                x_pos[i] -= nopeus

    pygame.display.flip()

    kello.tick(60)
