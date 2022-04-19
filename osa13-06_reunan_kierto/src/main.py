# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys, korkeus = 640, 480
x = 0
y = 0
suunta = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    if suunta == 1:
        x += 1
        if x+robo.get_width() == leveys:
            suunta = 2
    elif suunta == 2:
        y += 1
        if y+robo.get_height() == korkeus:
            suunta = 3
    elif suunta == 3:
        x -= 1
        if x == 0:
            suunta = 4
    elif suunta == 4:
        y -= 1
        if y == 0:
            suunta = 1

    kello.tick(60)
