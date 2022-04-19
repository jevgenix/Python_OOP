# Tee ratkaisusi tähän:
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            # henkilöön niittyy lista puhelinnumeroja
            self.__henkilot[nimi] = []
        self.__henkilot[nimi].append(numero)

    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    #Apumetodi joka hae nimet numeron perusteella
    def hae_nimet(self, numero: str):
        for key, value in self.__henkilot.items():
            for v in value:
                if numero not in v:
                    return None
                return key

    def kaikki_tiedot(self):
        return self.__henkilot

class Tiedostonkasittelija():
    def __init__(self, tiedosto):
        self.__tiedosto = tiedosto

    def lataa(self):
        nimet = {}
        with open(self.__tiedosto) as f:
            for rivi in f:
                osat = rivi.strip().split(';')
                nimi, *numerot = osat
                nimet[nimi] = numerot
        return nimet

    def talleta(self, luettelo: dict):
        with open(self.__tiedosto, "w") as f:
            for nimi, numerot in luettelo.items():
                rivi = [nimi] + numerot
                f.write(";".join(rivi) + "\n")

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()
        self.__tiedosto = Tiedostonkasittelija("luettelo.txt")

        # listään tiedostossa olevat nimet luetteloon
        for nimi, numerot in self.__tiedosto.lataa().items():
            for numero in numerot:
                self.__luettelo.lisaa_numero(nimi, numero)

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 lisäys")
        print("2 haku")
        print("3 haku numeron perusteella")

    def lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot == None:
            print("numero ei tiedossa") 
            return 
        for numero in numerot:
            print(numero)      
        
    #Apumetodi joka kysy numero ja lähettää sekä vastaanottaa tiedot
    #Toisesta apumetodista hae_nimet
    def hae_nimi_numerolla(self):
        numero = input("numero: ")
        nimet = self.__luettelo.hae_nimet(numero)
        if nimet == None:
            print("tuntematon numero")
        print(nimet)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                self.lopetus()
                break
            elif komento == "1":
                self.lisays()
            elif komento == "2":
                self.haku()

            elif komento == "3":
                self.hae_nimi_numerolla()

            else:
                self.ohje()
    
    def lopetus(self):
        self.__tiedosto.talleta(self.__luettelo.kaikki_tiedot())

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
