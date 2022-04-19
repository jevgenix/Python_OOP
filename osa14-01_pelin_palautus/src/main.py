import pygame
from random import randrange


class Roboman:
    def __init__(self):
        pygame.init()

        # värit
        self.LIGHTGREY = (192, 192, 192)
        self.DARKGREY = (128, 128, 128)
        self.YELLOW = (255, 255, 0)
        self.RED = (255, 0, 0)

        self.lataa_kuvat()
        self.nayton_korkeus = 900
        self.nayton_leveys = 500
        self.naytto = pygame.display.set_mode(
            (self.nayton_leveys, self.nayton_korkeus))
        pygame.display.set_caption("Roboman")

        """ robon sijainti """
        self.robo_x = 250 - self.kuvat[0].get_width()/4
        self.robo_y = 450 - self.kuvat[0].get_height()/2

        # kolikon sijainti
        self.kolikko_x = randrange(50, self.nayton_leveys-50)
        self.kolikko_y = randrange(-3 * self.nayton_korkeus, -800)

        # liikkuminen
        self.oikealle = False
        self.vasemmalle = False

        # laskuri
        self.laskuri = 0

        # hirvion y sijainti
        self.hirvio_y = 880

        # hirvioiden pseudo laatikko
        self.raja = 700
        self.peli_paalla = False

        # päävalikko
        self.paa_valikko = True

        # fontti
        self.fontti = pygame.font.SysFont("8-Bit-Madness", 38)

        # pisteet
        self.pisteet = 0

        """ tähdet """
        self.tahti_lista()

        """ Robon esteet """
        # laserit
        self.laseri_keskella_y = -3000
        self.laseri_vasemmalla_y = -2000
        self.laseri_oikealla_y = -1000

        # FPS
        self.kello = pygame.time.Clock()
        self.peli_kayntiin()

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()

            # liikkuminen
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()

                if not self.peli_paalla:
                    if tapahtuma.key == pygame.K_RETURN:
                        self.peli_paalla = True
                    if tapahtuma.key == pygame.K_F1:
                        self.paa_valikko = False
                    if tapahtuma.key == pygame.K_F2:
                        self.paa_valikko = True

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False

    def peli_kayntiin(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()
            self.kello.tick(60)

    def lataa_kuvat(self):
        self.kuvat = []
        for kuva in ["robo", "hirvio", "kolikko"]:
            self.kuvat.append(pygame.image.load(kuva + ".png"))

    def tahti_lista(self):
        self.nopeat_tahdet = []
        self.medium_tahdet = []
        self.hitaat_tahdet = []

        for nopea_tahti in range(50):
            self.tahti_x = randrange(0, self.nayton_leveys)
            self.tahti_y = randrange(0, self.nayton_korkeus)
            self.hitaat_tahdet.append(
                [self.tahti_x, self.tahti_y])

        for medium_tahti in range(35):
            self.tahti_x = randrange(0, self.nayton_leveys)
            self.tahti_y = randrange(0, self.nayton_korkeus)
            self.medium_tahdet.append([self.tahti_x, self.tahti_y])

        for nopea_tahti in range(15):
            self.tahti_x = randrange(0, self.nayton_leveys)
            self.tahti_y = randrange(0, self.nayton_korkeus)
            self.nopeat_tahdet.append([self.tahti_x, self.tahti_y])

    def tahdet(self):
        for tahti in self.hitaat_tahdet:
            tahti[1] += 1
            if tahti[1] > self.nayton_korkeus:
                tahti[0] = randrange(0, self.nayton_leveys)
                tahti[1] = randrange(-20, -5)
            pygame.draw.circle(self.naytto, self.DARKGREY, tahti, 3)

        for tahti in self.medium_tahdet:
            tahti[1] += 4
            if tahti[1] > self.nayton_korkeus:
                tahti[0] = randrange(0, self.nayton_leveys)
                tahti[1] = randrange(-20, -5)
            pygame.draw.circle(self.naytto, self.LIGHTGREY, tahti, 2)

        for tahti in self.nopeat_tahdet:
            tahti[1] += 8
            if tahti[1] > self.nayton_korkeus:
                tahti[0] = randrange(0, self.nayton_leveys)
                tahti[1] = randrange(-20, -5)
            pygame.draw.circle(self.naytto, self.YELLOW, tahti, 1)

    def valikko(self):
        self.naytto.fill((0, 0, 0))

        # fontti
        fontti = pygame.font.SysFont("8-Bit-Madness", 64)

        # lopullinen pistemäärä
        if self.pisteet > 0:
            pistemaara = self.fontti.render(
                f"Final score {self.pisteet}", True, (0, 255, 0))
            pistemaara_rect = pistemaara.get_rect(
                midtop=(self.nayton_leveys/2, self.nayton_korkeus/2 - 200))

        # aloita nappi
        aloita_nappi = self.fontti.render(
            "Press 'Enter' to start", True, (255, 0, 0))
        aloita_nappi_rect = aloita_nappi.get_rect(
            center=(self.nayton_leveys/2, self.nayton_korkeus/2))

        # ohjeet nappi
        ohjeet = self.fontti.render("F1 instructions", True, (255, 255, 255))
        ohjeet_rect = ohjeet.get_rect(
            topleft=(5, self.nayton_korkeus-30))

        if self.paa_valikko:
            # teksti naytölle
            self.naytto.blit(ohjeet, ohjeet_rect)
            self.naytto.blit(aloita_nappi, aloita_nappi_rect)
            if self.pisteet > 0:
                self.naytto.blit(pistemaara, pistemaara_rect)
        else:
            teksti_lista = [
                "Robo is trying to escape from monsters",
                "Coins are falling from the sky",
                "If Robo catches a coin:",
                "Robo gets a point",
                "If monsters catches a coin:",
                "They will approach closer to robo",
                "Robo should avoid obstacles",
                "Robo should collect coins",
                "If Robo encounters obstacles:",
                "Robo will die and game will end",
                "If monsters catches Robo:",
                "Robo will die and game will end",
                "Good luck and have fun!"
            ]

            x = self.nayton_leveys
            y = 150
            for teksti in teksti_lista:
                ohjeet_fontti = pygame.font.SysFont("8-Bit-Madness", 28)
                ohjeet_teksti = ohjeet_fontti.render(teksti, True, (255, 0, 0))
                ohjeet_teksti_rect = ohjeet_teksti.get_rect(center=(x/2, y))

                self.naytto.blit(ohjeet_teksti, ohjeet_teksti_rect)
                y += 50

            back_nappi = self.fontti.render(
                "F2 to return", True, (255, 255, 255))
            back_nappi_rect = back_nappi.get_rect(
                topleft=(5, self.nayton_korkeus-30))
            self.naytto.blit(back_nappi, back_nappi_rect)

    def piirra_naytto(self):
        if self.peli_paalla:
            # pelin tausta
            self.naytto.fill((4, 4, 4))
            self.tahdet()

            # pisteet ruudulle
            teksti = self.fontti.render(
                f"Pisteet: {self.laskuri}", True, (0, 255, 0))
            self.naytto.blit(teksti, (370, 50))

            # kuva-muuttujat
            # dokumentaation mukaan convert_alpha() nopeuttaa pelin
            robo = self.kuvat[0].convert_alpha()
            hirvio = self.kuvat[1].convert_alpha()
            kolikko = self.kuvat[2].convert_alpha()

            # kolikko ruudulle
            self.naytto.blit(kolikko, (self.kolikko_x, self.kolikko_y))

            # robon laatikko
            self.robo_rect = robo.get_rect(topleft=(self.robo_x, self.robo_y))
            self.kolikko_y += 10

            # kolikon laatikko
            self.kolikko_rect = kolikko.get_rect(
                topleft=(self.kolikko_x, self.kolikko_y))

            # jos kolikko osuu roboon
            if self.robo_rect.colliderect(self.kolikko_rect):
                self.laskuri += 1
                # kolikko siirtyy muualle
                self.kolikko_x = randrange(50, self.nayton_leveys-50)
                self.kolikko_y = randrange(-3 * self.nayton_korkeus, -800)

            # mikäli kolikko osuu hirviöön
            if self.kolikko_y > self.raja:
                # hirviö lähestyy
                self.hirvio_y -= 100
                self.raja -= 100
                # kolikko siirtyy muualle
                self.kolikko_x = randrange(50, self.nayton_leveys-50)
                self.kolikko_y = randrange(-3 * self.nayton_korkeus, -800)

            # robo liikkuu oikealle
            if self.oikealle:
                # reunat
                if self.robo_x + robo.get_width() < self.nayton_leveys:
                    self.robo_x += 10

            # robo liikkuu vasemmalle
            if self.vasemmalle:
                # reunat
                if self.robo_x - robo.get_width() > -robo.get_width():
                    self.robo_x -= 10

            # monsterit ruudulle
            hirvio_y = self.hirvio_y
            for i in range(3):
                hirvio_x = 5
                hirvio_y -= 50

                for j in range(12):
                    self.hirvio_rect = hirvio.get_rect()
                    self.naytto.blit(hirvio, (hirvio_x, hirvio_y))
                    hirvio_x += 40
            self.naytto.blit(robo, self.robo_rect)

            # jos hirviot osuu roboon, peli päättyy
            if self.hirvio_y == 580:
                self.peli_paalla = False
                self.hirvio_y = 880
                self.raja = 700
                self.pisteet = self.laskuri
                self.laskuri = 0
                self.laseri_keskella_y = -3000
                self.laseri_vasemmalla_y = -2000
                self.laseri_oikealla_y = -1000

            # lisätään esteet
            self.esteet()

        else:
            self.valikko()
            self.tahdet()

        # update naytto
        pygame.display.flip()

    def esteet(self):
        # laseri keskella
        laseri_keskella = pygame.Rect(125, self.laseri_keskella_y, 250, 5)
        pygame.draw.rect(self.naytto, self.RED, laseri_keskella)
        self.laseri_keskella_y += 10

        # laseri vasemmalla
        laseri_vasemmalla = pygame.Rect(
            0, self.laseri_vasemmalla_y, 130, 5)
        pygame.draw.rect(self.naytto, self.RED, laseri_vasemmalla)
        self.laseri_vasemmalla_y += 10

        # laseri oikealla
        laseri_oikealla = pygame.Rect(370, self.laseri_oikealla_y, 500, 5)
        pygame.draw.rect(self.naytto, self.RED, laseri_oikealla)
        self.laseri_oikealla_y += 10

        if self.laseri_keskella_y > 900:
            self.laseri_keskella_y = -3000

        elif self.laseri_vasemmalla_y > 900:
            self.laseri_vasemmalla_y = -2000

        elif self.laseri_oikealla_y > 900:
            self.laseri_oikealla_y = -1000

        # mikäli laseri osuu toiseen laseriin:
        if laseri_keskella.colliderect(laseri_vasemmalla) or laseri_keskella.colliderect(laseri_oikealla):
            self.laseri_keskella_y = -3000

        # mikäli kolikko osuu laseriin
        if self.kolikko_rect.colliderect(laseri_keskella) or self.kolikko_rect.colliderect(laseri_vasemmalla) or self.kolikko_rect.colliderect(laseri_oikealla):
            self.kolikko_y = randrange(-2 * self.nayton_korkeus, -800)

        # mikäli robo osuu laseriin
        if self.robo_rect.colliderect(laseri_keskella) or self.robo_rect.colliderect(laseri_vasemmalla) or self.robo_rect.colliderect(laseri_oikealla):
            self.peli_paalla = False
            self.hirvio_y = 880
            self.raja = 700
            self.pisteet = self.laskuri
            self.laskuri = 0
            self.kolikko_y = randrange(-3 * self.nayton_korkeus, -800)
            self.laseri_keskella_y = -3000
            self.laseri_vasemmalla_y = -2000
            self.laseri_oikealla_y = -1000


if __name__ == '__main__':
    Roboman()
