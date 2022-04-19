# Tee ratkaisusi tähän:
class Muistilista:
    def __init__(self, otsikko: str, merkinnat: list):
        self.otsikko = otsikko
        self.merkinnat = merkinnat

class Asiakas:
    def __init__(self, tunniste: str, saldo: float, alennusprosentti: int):
        self.tunniste = tunniste
        self.saldo = saldo
        self.alennusprosentti = alennusprosentti

class Kaapeli:
    def __init__(self, malli: str, pituus: float, maksiminopeus: int, kaksisuuntainen: bool):
        self.malli = malli
        self.pituus = pituus
        self.maksiminopeus = maksiminopeus
        self.kaksisuuntainen = kaksisuuntainen