# TEE RATKAISUSI TÄHÄN:
# Huom! Älä muuta luokkaa Henkilo!

class Henkilo:
    def __init__(self, nimi: str, ika: int, pituus: int, paino: int):
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino

class Kasvatuslaitos:
    def __init__(self):
        self.punnitusten_lkm = 0

    def punnitse(self, henkilo: Henkilo):
        # palautetaan parametrina annetun henkilön paino
        self.punnitusten_lkm += 1
        return henkilo.paino

    def syota(self, henkilo: Henkilo):
        henkilo.paino += 1
        return henkilo.paino

    def punnitukset(self):
        return self.punnitusten_lkm

if __name__ == '__main__':
    haagan_neuvola = Kasvatuslaitos()

    eero = Henkilo("Eero", 1, 110, 7)
    pekka = Henkilo("Pekka", 33, 176, 85)

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")

    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")

    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)

    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")