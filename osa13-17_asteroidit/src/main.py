import pygame
from random import randrange

pygame.init()

leveys = 640
korkeus = 480
naytto = pygame.display.set_mode((leveys, korkeus))

robo = pygame.image.load("robo.png")

# creating multiple asteroids
asteroidit = []
asteroiditX = []
asteroiditY = []
asteroidi_leveys = []
asteroidi_korkeus = []
maara = 5

asteroidi = pygame.image.load("kivi.png")
asteroidiLeveys = asteroidi.get_width()
asteroidiKorkeus = asteroidi.get_height()

for i in range(maara):
    kiviX = randrange(leveys)
    kiviY = randrange(-korkeus*2, 0)

    asteroidit.append(asteroidi)
    asteroiditX.append(kiviX)
    asteroiditY.append(kiviY)
    asteroidi_leveys.append(asteroidiLeveys)
    asteroidi_korkeus.append(asteroidiKorkeus)

# robo koordinaatit
roboXkoordinaatti = 320
roboYkoordinaatti = korkeus-robo.get_height()

robo_korkeus = robo.get_height()
robo_leveys = robo.get_width()

keyLeft = False
keyRight = False

laskuri = 0

kello = pygame.time.Clock()
while True:
    naytto.fill(0)
    naytto.blit(robo, (roboXkoordinaatti, roboYkoordinaatti))

    fontti = pygame.font.SysFont("Arial", 28)
    teksti = fontti.render(f"Pisteet: {laskuri}", True, (255, 0, 0))
    naytto.blit(teksti, (500, 50))

    for i in range(maara):
        naytto.blit(asteroidit[i], (asteroiditX[i], asteroiditY[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Event for Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # Event to check if key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    if keyLeft:
        if roboXkoordinaatti > 0:
            roboXkoordinaatti -= 10

    if keyRight:
        if roboXkoordinaatti < leveys - robo_leveys:
            roboXkoordinaatti += 10

    # robo box
    roboBox = pygame.Rect(robo.get_rect())
    roboBox.top = roboYkoordinaatti
    roboBox.left = roboXkoordinaatti

    # asteroidit putoa
    for i in range(maara):
        asteroiditY[i] += 2

        # asteroidi box
        asteroidiBox = pygame.Rect(asteroidit[i].get_rect())
        asteroidiBox.top = asteroiditY[i]
        asteroidiBox.left = asteroiditX[i]

        if roboBox.colliderect(asteroidiBox):
            laskuri += 1
            asteroiditY[i] = randrange(-korkeus*2, 0)
            asteroiditX[i] = randrange(leveys)

        if asteroiditY[i] > korkeus:
            raise ValueError("Game Over")

    pygame.display.flip()
    kello.tick(60)
