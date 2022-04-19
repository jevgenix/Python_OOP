# TEE RATKAISUSI TÄHÄN:
def parilliset(alku: int, maksimi: int):
    luku = alku
    while luku <= maksimi:
        if luku % 2 == 0:
            yield luku
        luku += 1

if __name__ == "__main__":
    luvut = parilliset(11, 21)
    for luku in luvut:
        print(luku)