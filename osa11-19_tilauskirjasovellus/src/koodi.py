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


class Sovellus:
    def __init__(self):
        self.__tilauskirja = Tilauskirja()


    def ohje(self):
        print('komennot:')
        print('0 lopetus')
        print('1 lisää tilaus')
        print('2 listaa valmiit')
        print('3 listaa ei valmiit')
        print('4 merkitse tehtävä valmiiksi')
        print('5 koodarit')
        print('6 koodarin status')

    def lisaa_tilaus(self):
        kuvaus = input("kuvaus: ")
        nimi_ja_tyomaara = input("koodari ja työmääräarvio: ")
        try:
            nimi_ja_tyomaara = nimi_ja_tyomaara.split(" ")
            self.__tilauskirja.lisaa_tilaus(kuvaus, nimi_ja_tyomaara[0], int(nimi_ja_tyomaara[1]))
            print("lisätty!")
        except:
            print("virheellinen syöte")
        

    def listaa_valmiita(self):
        if len(self.__tilauskirja.valmiit_tilaukset()) > 0:
            for tilaus in self.__tilauskirja.valmiit_tilaukset():
                print(tilaus)
        else:
            print("ei valmiita")

    def listaa_ei_valmiita(self):
        if len(self.__tilauskirja.ei_valmiit_tilaukset()) > 0:
            for tilaus in self.__tilauskirja.ei_valmiit_tilaukset():
                print(tilaus)
        else:
            print("kaikki valmis!")

    def merkitse_valmiiksi(self):
        
        try:
            tunniste = int(input("tunniste: "))
            self.__tilauskirja.merkkaa_valmiiksi(tunniste)
            print("merkitty valmiiksi")
        except:
            print("virheellinen syöte")


    def koodarit(self):
        for koodari in self.__tilauskirja.koodajat:
            print(koodari)

    def status(self):
        try:
            koodari = input("koodari: ")
            tiedot = self.__tilauskirja.koodarin_status(koodari)
            print(f"työt: valmiina {tiedot[0]} ei valmiina {tiedot[1]}, tunteja: tehty {tiedot[2]} tekemättä {tiedot[3]}")
        except:
            print("virheellinen syöte")

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_tilaus()
            elif komento == "2":
                self.listaa_valmiita()
            elif komento == "3":
                self.listaa_ei_valmiita()
            elif komento == "4":
                self.merkitse_valmiiksi()
            elif komento == "5":
                self.koodarit()
            elif komento == "6":
                self.status()



    
sovellus = Sovellus()
sovellus.suorita()



