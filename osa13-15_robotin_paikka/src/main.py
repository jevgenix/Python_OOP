import random
import pygame
from random import randint

pygame.init()
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

robo = pygame.image.load("robo.png")

x = randint(0, leveys-robo.get_width())
y = randint(0, korkeus-robo.get_height())

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            hiiri_x = tapahtuma.pos[0]
            hiiri_y = tapahtuma.pos[1]

            osuma_x = hiiri_x >= x and hiiri_x <= x+robo.get_width()
            osuma_y = hiiri_y >= y and hiiri_y <= y+robo.get_height()

            if osuma_x and osuma_y:
                x = randint(0, leveys-robo.get_width())
                y = randint(0, korkeus-robo.get_height())

        if tapahtuma.type == pygame.QUIT:
            exit()

        naytto.fill((0, 0, 0))
        naytto.blit(robo, (x, y))
        pygame.display.flip()


screen = pygame.display.set_mode([1024, 768])
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
pygame.display.set_caption('Window Caption')
clock = pygame.time.Clock()

# create the locations of the stars for when we animate the background
star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(50):  # birth those plasma balls, baby
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_slow.append([star_loc_x, star_loc_y])  # i love your balls

for medium_stars in range(35):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_fast.append([star_loc_x, star_loc_y])

# define some commonly used colours


# create the window
pygame.init()

app_is_alive = True

while app_is_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "Exiting... All hail the void!"
            app_is_alive = False  # murderer!
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print "Exiting... All hail the void!"
            app_is_alive = False  # murderer!

    # my soul knows only darkness
    screen.fill(BLACK)

    # animate some motherfucking stars
    for star in star_field_slow:
        star[1] += 1
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, DARKGREY, star, 3)

    for star in star_field_medium:
        star[1] += 4
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, LIGHTGREY, star, 2)

    for star in star_field_fast:
        star[1] += 8
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, YELLOW, star, 1)

    # redraw everything we've asked pygame to draw
    pygame.display.flip()

    # set frames per second
    clock.tick(30)

# quit gracefully
pygame.quit()
