# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
leveys, korkeus = 640, 480
robo = pygame.image.load("robo.png")
x = 640-robo.get_width()
y = 480-robo.get_height()

oikealle = False
vasemmalle = False
ylos = False
alas = False

kello = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            if tapahtuma.key == pygame.K_UP:
                ylos = True
            if tapahtuma.key == pygame.K_DOWN:
                alas = True

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            if tapahtuma.key == pygame.K_UP:
                ylos = False
            if tapahtuma.key == pygame.K_DOWN:
                alas = False

        if tapahtuma.type == pygame.QUIT:
            exit()

    if oikealle:
        if x+robo.get_width() != leveys:
            x += 5
    if vasemmalle:
        if x-robo.get_width() > -robo.get_width():
            x -= 5
    if alas:
        if y+robo.get_height() != korkeus:
            y += 5
    if ylos:
        if y-robo.get_height() > -robo.get_height():
            y -= 5

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    kello.tick(60)
