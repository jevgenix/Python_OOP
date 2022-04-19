class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"


def hyvaksytyt(suoritukset: list):
    return filter(lambda suoritus: suoritus.arvosana > 0, suoritukset)


def suoritus_arvosanalla(suoritukset: list, arvosana: int):
    return filter(lambda suoritus: suoritus.arvosana == arvosana, suoritukset)


def kurssin_suorittajat(suoritukset: list, kurssi: str):
    kurssin_opiskelijat = filter(
        lambda s: s.arvosana > 0 and s.kurssi == kurssi, suoritukset)

    kurssin_opiskelijat = map(
        lambda n: n.opiskelijan_nimi, kurssin_opiskelijat)
    return sorted(kurssin_opiskelijat)


def aakkosjarjestys(mjono):
    return sorted(mjono)


if __name__ == "__main__":
    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Tietoliikenteen perusteet", 5)
    s3 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 0)
    s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)

    # for suoritus in hyvaksytyt([s1, s2, s3]):
    #    print(suoritus)

    # for suoritus in suoritus_arvosanalla([s1, s2, s3, s4], 3):
    #     print(suoritus)

    for suoritus in kurssin_suorittajat([s1, s2, s3, s4], "Tietoliikenteen perusteet"):
        print(suoritus)
