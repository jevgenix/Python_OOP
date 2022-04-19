class Tehtava:
    uniqueID = 1
    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.__kuvaus = kuvaus
        self.__koodari = koodari
        self.__tyomaara = tyomaara
        
        self.__id = Tehtava.uniqueID
        Tehtava.uniqueID += 1

        self.bool = False

    @property
    def kuvaus(self):
        return self.__kuvaus
    @property
    def koodari(self):
        return self.__koodari
    @property
    def tyomaara(self):
        return self.__tyomaara
    @property
    def id(self):
        return self.__id


    def on_valmis(self):
        return self.bool

    def merkkaa_valmiiksi(self):
        self.bool = True

    def __str__(self):
        return f"{self.__id}: {self.__kuvaus} ({self.__tyomaara} tuntia), koodari {self.__koodari} {'VALMIS' if self.bool == True else 'EI VALMIS'}"
    

class Tilauskirja:
    def __init__(self):
        self.tilaukset = []
        self.koodajat = []

    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        self.tilaukset.append(Tehtava(kuvaus, koodari, tyomaara))
        self.koodajat.append(koodari)
    
    def kaikki_tilaukset(self):
        return self.tilaukset

    def koodarit(self):
        return list(set(self.koodajat))

    def merkkaa_valmiiksi(self, id: int):
        for tilaus in self.tilaukset:
            if id == tilaus.id:
                tilaus.merkkaa_valmiiksi()
                return
        raise ValueError    
        

    def valmiit_tilaukset(self):
        valmiit = []
        for tilaus in self.tilaukset:
            if tilaus.on_valmis():
                valmiit.append(tilaus)
        return valmiit

    def ei_valmiit_tilaukset(self):
        ei_valmiit = []
        for tilaus in self.tilaukset:
            if not tilaus.on_valmis():
                ei_valmiit.append(tilaus)
        return ei_valmiit

    def koodarin_status(self, koodari: str):
        valmiit = 0
        ei_valmiit = 0
        tehdyt = 0
        ei_tehdyt = 0

        if koodari not in self.koodajat:
            raise ValueError

        for tilaus in self.tilaukset:
            if tilaus.koodari == koodari:
                if tilaus.on_valmis():
                    tehdyt += 1
                    valmiit += tilaus.tyomaara
                else:
                    ei_tehdyt += 1
                    ei_valmiit += tilaus.tyomaara
            
        return (tehdyt, ei_tehdyt, valmiit, ei_valmiit)
        
        
 
if __name__ == '__main__':
    
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    for tilaus in tilaukset.kaikki_tilaukset():
        print(tilaus)



