from functools import reduce


class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"


# Tee ratkaisusi tähän:
def kaikkien_opintopisteiden_summa(s: list):
    return reduce(lambda summa, op: op.opintopisteet + summa, s, 0)


def hyvaksyttyjen_opintopisteiden_summa(s: list):
    hyvaksytyt = list(filter(lambda x: x.arvosana > 0, s))
    return reduce(lambda summa, op: op.opintopisteet + summa, hyvaksytyt, 0)


def keskiarvo(s: list):
    hyvaksytyt = list(filter(lambda x: x.arvosana > 0, s))
    arvosanojen_summa = reduce(
        lambda summa, op: op.arvosana + summa, hyvaksytyt, 0)
    return arvosanojen_summa / len(hyvaksytyt)


if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print(summa)
