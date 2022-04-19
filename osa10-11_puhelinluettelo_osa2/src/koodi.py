class Henkilo:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._osoite = None
        self._numerot = []

    def nimi(self):
        return self._nimi

    def numerot(self):
        return self._numerot

    def osoite(self):
        return self._osoite

    def lisaa_numero(self, numero: str):
        self._numerot.append(numero)

    def lisaa_osoite(self, osoite: str):
        self._osoite = osoite


class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if nimi not in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, osoite: str):
        if nimi not in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)

    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    def kaikki_tiedot(self):
        return self.__henkilot

    def tiedot(self, nimi: str):
        for name, data in self.__henkilot.items():
            numerot = ", ".join(data.numerot())
            if nimi == name:
                print(("osoite ei tiedossa\n" if data.osoite() == None else data.osoite() + "\n")
                      + ("numero ei tiedossa" if len(numerot) < 1 else numerot))


class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_tiedot(nimi)
        osoite = self.__luettelo.hae_tiedot(nimi)
        if numerot == None:
            print("numero ei tiedossa")
        if osoite == None:
            print("osoite ei tiedossa")
        else:
            return self.__luettelo.tiedot(nimi)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()


# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()


#testi = {}
#testi["nimi"] = ["Pekka", "Python"]
#
# for key, value in testi.items():
#    for i in range(len(value)):
#        etu = value[0]
#        suku = value[1]
#    print(key, etu, suku)
