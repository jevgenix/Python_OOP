# TEE RATKAISUSI TÄHÄN:
class Lemmikki:
    def __init__(self, nimi: str, kuvaus: str):
        self.nimi = nimi
        self.kuvaus = kuvaus

    def __str__(self):
        return f"{self.nimi} ({self.kuvaus})"

class Henkilo:
    def __init__(self, nimi: str, lemmikki: Lemmikki):
        self.nimi = nimi
        self.lemmikki = lemmikki

    def __str__(self):
        return f"{self.nimi}, kaverina {self.lemmikki.nimi}, joka on {self.lemmikki.kuvaus}"

if __name__ == "__main__":
    hulda = Lemmikki("Hulda", "sekarotuinen koira")
    leevi = Henkilo("Leevi", hulda)

    print(leevi)