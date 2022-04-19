# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()

naytto = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))


korkeus = 50
leveys = 30

for y in range(10):
    for x in range(10):
        naytto.blit(robo, (leveys + 40*x, korkeus))
    leveys += 5
    korkeus += 30


pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
