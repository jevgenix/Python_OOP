class Kurssi:
    def __init__(self, kurssi: str):
        self._kurssi = kurssi
        self._arvosana = None
        self._opintopisteet = None
        self._suoritukset = []

    def lisaa_arvosana(self, arvosana: int):
        if self._arvosana == None: 
            self._arvosana = arvosana
            self._suoritukset.append(arvosana)

        elif arvosana > self._suoritukset[0]:
            self._arvosana = arvosana
            self._suoritukset[0] = arvosana

    def lisaa_opintopisteet(self, opintopisteet: int):
        self._opintopisteet = opintopisteet
        self._suoritukset.append(opintopisteet)

    def kurssi(self):
        return self._kurssi
    
    def arvosana(self):
        return self._arvosana

    def opintopisteet(self):
        return self._opintopisteet
    
class Kurssisuoritusote:
    def __init__(self):
        self.__suoritus = {}

    def lisaa_kurssi(self, kurssi: str, opintopisteet: int, arvosana: int):
        if kurssi not in self.__suoritus:
            self.__suoritus[kurssi] = Kurssi(kurssi)
        self.__suoritus[kurssi].lisaa_arvosana(arvosana)
        self.__suoritus[kurssi].lisaa_opintopisteet(opintopisteet)

    def hae_tiedot(self, kurssi: str):
        if kurssi not in self.__suoritus:
            return None
        return self.__suoritus[kurssi]

    def kaikki_tiedot(self):
        return self.__suoritus

    def tiedot(self, kurssi: str):
        for nimi, tieto in self.__suoritus.items():
            if kurssi == nimi:
                print(f"{nimi} ({tieto.opintopisteet()} op) arvosana {tieto.arvosana()}")

    def tilasto(self):
        laskuri = 0
        keskiarvo = 0
        opintopisteet = 0
        arvot = [0, 0, 0, 0, 0]
        jakauma = [5, 4, 3, 2, 1]

        for value in self.__suoritus.values():  
            laskuri += 1
            keskiarvo += int(value.arvosana())
            opintopisteet += int(value.opintopisteet())

            if value.arvosana() == "1":
                arvot[4] += 1

            elif value.arvosana() == "2":
                arvot[3] += 1
            
            elif value.arvosana() == "3":
                arvot[2] += 1
            
            elif value.arvosana() == "4":
                arvot[1] += 1
            
            elif value.arvosana() == "5":
                arvot[0] += 1
        
        keskiarvo = keskiarvo / laskuri

        print(f"suorituksia {laskuri} kurssilta, yhteensä {opintopisteet} opintopistettä")
        print(f"keskiarvo {keskiarvo:.1f}\narvosanajakauma")
        
        for i in range(len(arvot)):
            print(f"{jakauma[i]}: {arvot[i] * 'x'}")

class KurssiSovellus:
    def __init__(self):
        self.__tilasto = Kurssisuoritusote()

    def ohje(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")

    def lisaa_suoritus(self):
        kurssi = input("kurssi: ")
        arvosana = input("arvosana: ")
        opintopisteet = input("opintopisteet: ")
        self.__tilasto.lisaa_kurssi(kurssi, opintopisteet, arvosana)


    def hae_suoritus(self):
        kurssi = input("kurssi: ")
        kurssit = self.__tilasto.hae_tiedot(kurssi)
        if kurssit == None:
            print("ei suoritusta")
        else:
            return self.__tilasto.tiedot(kurssi)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_suoritus()
            elif komento == "2":
                self.hae_suoritus()
            elif komento == "3":
                self.__tilasto.tilasto()
            else:
                self.ohje()


kurssi = KurssiSovellus()
kurssi.suorita()