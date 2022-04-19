# TEE RATKAISUSI TÄHÄN:
class Paivays:
    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.paiva = paiva
        self.kuukausi = kuukausi
        self.vuosi = vuosi

    def __str__(self):
        return f"{self.paiva}.{self.kuukausi}.{self.vuosi}"

    def __arvo(self):
        return self.paiva + self.kuukausi * 30 + self.vuosi * 12 * 30

    def __muuta_paivamaaraksi(self, paivat):
        self.vuosi = (paivat // 360)
        self.kuukausi = int((paivat / 360 - self.vuosi) * 12)
        self.paiva = round(((paivat / 360 - self.vuosi) * 12 - int((paivat / 360 - self.vuosi) * 12)) * 30)

    def __eq__(self, toinen: "Paivays"):
        return self.__arvo() == toinen.__arvo()

    def __gt__(self, toinen: "Paivays"):
        return self.__arvo() > toinen.__arvo()

    def __ge__(self, toinen: "Paivays"):
        return self.__arvo() >= toinen.__arvo()

    def __add__(self, toinen):
        paivamaara = Paivays(0, 0, 0)
        paivamaara.__muuta_paivamaaraksi(self.__arvo() + toinen)
        return paivamaara

    def __sub__(self, toinen):
        return abs(self.__arvo() - toinen.__arvo())

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)

    