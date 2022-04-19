import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("pallo.png")
x = 320
y = 240
nopeus_x = 5
nopeus_y = 5
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    y += nopeus_y
    x += nopeus_x
    if x == 0 or x+robo.get_width() == 640:
        nopeus_x = -nopeus_x

    if y == 0 or y+robo.get_height() == 480:
        nopeus_y = -nopeus_y

    kello.tick(60)
