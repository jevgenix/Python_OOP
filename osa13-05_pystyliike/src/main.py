import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
x = 0
y = 0
nopeus = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    y += nopeus
    if nopeus > 0 and y+robo.get_height() >= 480:
        nopeus = -nopeus
    if nopeus < 0 and y <= 0:
        nopeus = -nopeus

    kello.tick(60)
