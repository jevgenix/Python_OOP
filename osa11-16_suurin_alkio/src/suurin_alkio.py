# TEE RATKAISUSI TÄHÄN:
class Alkio:
    """ Luokka mallintaa yhtä alkiota binääripuussa """
    def __init__(self, arvo, vasen_lapsi:'Alkio' = None, oikea_lapsi:'Alkio' = None):
        self.arvo = arvo
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi


def alkioiden_summa(juuri: Alkio):
    summa = juuri.arvo

    if juuri.vasen_lapsi is not None:
        summa += alkioiden_summa(juuri.vasen_lapsi)

    if juuri.oikea_lapsi is not None:
        summa += alkioiden_summa(juuri.oikea_lapsi)

    return summa


def suurin_alkio(juuri: Alkio):
    suurin = [juuri.arvo]

    if juuri.vasen_lapsi is not None:
        suurin.append(suurin_alkio(juuri.vasen_lapsi))

    if juuri.oikea_lapsi is not None:
        suurin.append(suurin_alkio(juuri.oikea_lapsi))

    return max(suurin)
        

if __name__ == "__main__":
    puu = Alkio(2)

    puu.vasen_lapsi = Alkio(3)
    puu.vasen_lapsi.vasen_lapsi = Alkio(5)
    puu.vasen_lapsi.oikea_lapsi = Alkio(8)

    puu.oikea_lapsi = Alkio(4)
    puu.oikea_lapsi.oikea_lapsi = Alkio(11)

    print(suurin_alkio(puu))