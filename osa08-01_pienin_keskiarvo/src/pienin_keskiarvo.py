# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    h1 = 0 
    h2 = 0 
    h3 = 0
    luvut = []
    while True:
        for (v1), (v2), (v3) in zip(henkilo1.values(),henkilo2.values(),henkilo3.values()):
            if isinstance(v1, int):
                h1 += v1
            if isinstance(v2, int):
                h2 += v2
            if isinstance(v3, int):
                h3 += v3
        luvut.append(h1/3)
        luvut.append(h2/3)
        luvut.append(h3/3)
        if min(luvut) == luvut[0]:
            return henkilo1
        elif min(luvut) == luvut[1]:
            return henkilo2
        else:
            return henkilo3


if __name__ == '__main__':
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}
    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))

