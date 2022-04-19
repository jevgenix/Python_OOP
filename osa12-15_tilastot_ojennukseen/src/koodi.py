# tee ratkaisusi tänne
import json


class Pelaajat:
    def __init__(self):
        t = input("tiedosto: ")
        #t = "kaikki.json"
        self.pelaajat = self.lueTiedot(t)

    def lueTiedot(self, t):
        with open(t) as tiedosto:
            tiedot = tiedosto.read()

        data = json.loads(tiedot)
        print(f"luettiin {len(data)} pelaajan tiedot")

        pelaajat = []
        for d in data:
            nimi = d["name"]
            nationality = d["nationality"]
            assists = d["assists"]
            goals = d["goals"]
            penalties = d["penalties"]
            team = d["team"]
            games = d["games"]

            pelaajat.append((nimi, nationality, assists,
                             goals, penalties, team, games))
        return pelaajat


class Sovellus:
    def __init__(self):
        self.nhl = Pelaajat()

    def ohje(self):
        print("")
        print("komennot:")
        print("0 lopeta")
        print("1 hae pelaaja")
        print("2 joukkueet")
        print("3 maat")
        print("4 joukkueen pelaajat")
        print("5 maan pelaajat")
        print("6 eniten pisteitä")
        print("7 eniten maaleja")

    def tulostuksenMuotoilu(self, merkki: str, arvo: int):
        if merkki == '+':
            if arvo < 10:
                return f"{'+':<2}"
            return f"{'+':<1}"
        elif merkki == '=':
            if arvo < 10:
                return f"{'=':<3}"
            elif arvo >= 10 and arvo < 100:
                return f"{'=':<2}"
            else:
                return f"{'=':<1}"
        else:
            return f"{arvo:>3}"

    def haePelaaja(self, nimi: str):

        for x in self.nhl.pelaajat:
            if nimi == x[0]:
                print(
                    f"{x[0]:<20} {x[5]} {x[3]:>3} {self.tulostuksenMuotoilu('+', x[2])} {x[2]} {self.tulostuksenMuotoilu('=', (x[2] + x[3]))} {x[2] + x[3]}")

    def joukkueenPelaajat(self, joukkue: str):
        lista = []
        for x in self.nhl.pelaajat:
            if joukkue == x[5]:
                lista.append((x[0], x[5], x[2], x[3], (x[3] + x[2])))
        for x in self.suurempiNumero(lista):
            print(f"{x[0]:<20} {x[1]} {x[3]:>3} {self.tulostuksenMuotoilu('+', x[2])} {x[2]} {self.tulostuksenMuotoilu('=', x[4])} {x[4]}")

    def maanPelaajat(self, maa: str):
        lista = []
        for x in self.nhl.pelaajat:
            if maa == x[1]:
                lista.append((x[0], x[5], x[2], x[3], (x[3] + x[2])))
        for x in self.suurempiNumero(lista):
            print(f"{x[0]:<20} {x[1]} {x[3]:>3} {self.tulostuksenMuotoilu('+', x[2])} {x[2]} {self.tulostuksenMuotoilu('=', x[4])} {x[4]}")

    def aakkosjarjestys(self, alkiot: list):
        def jarjestys(alkio: tuple):
            return alkio
        return sorted(alkiot, key=jarjestys)

    def suurempiNumero(self, alkiot: list):
        def numeroJarjestys(alkio):
            return alkio[4]
        return sorted(alkiot, key=numeroJarjestys, reverse=True)

    def enitenPisteita(self, monta: int):
        lista = []
        for x in self.nhl.pelaajat:
            lista.append((x[0], x[5], x[2], x[3], (x[3] + x[2])))
        jarjestetty = self.suurempiNumero(lista)
        index = 0
        for x in jarjestetty:
            if index == monta:
                break
            print(f"{x[0]:<20} {x[1]} {x[3]:>3} {self.tulostuksenMuotoilu('+', x[2])} {x[2]} {self.tulostuksenMuotoilu('=', x[4])} {x[4]}")
            index += 1

    def maaleja(self, alkiot: list):
        def maaliJarjestys(alkio):
            return alkio[3]

        return sorted(alkiot, key=maaliJarjestys, reverse=True)

    def enitenMaaleja(self, monta):
        lista = []
        for x in self.nhl.pelaajat:
            lista.append((x[0], x[5], x[2], x[3], (x[3] + x[2]), x[6]))

        jarjestetty = self.maaleja(lista)

        temp = [jarjestetty[alkio] for alkio in range(monta)]

        for a in range(len(temp) - 1):
            if temp[a][3] == temp[a + 1][3]:
                if temp[a][5] > temp[a + 1][5]:
                    temp[a], temp[a + 1] = temp[a + 1], temp[a]

        index = 0
        for x in temp:
            if index == monta:
                break
            print(f"{x[0]:<20} {x[1]} {x[3]:>3} {self.tulostuksenMuotoilu('+', x[2])} {x[2]} {self.tulostuksenMuotoilu('=', x[4])} {x[4]}")
            index += 1

    def suorita(self):
        self.ohje()
        data = self.nhl.pelaajat
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break

            elif komento == "1":
                nimi = input("nimi: ")
                print("")
                self.haePelaaja(nimi)

            elif komento == "2":
                teams = []
                for t in data:
                    if t[5] not in teams:
                        teams.append(t[5])

                for t in self.aakkosjarjestys(teams):
                    print(t)

            elif komento == "3":
                maat = []
                for t in data:
                    if t[1] not in maat:
                        maat.append(t[1])

                for maa in self.aakkosjarjestys(maat):
                    print(maa)

            elif komento == "4":
                print("")
                joukkue = input("joukkue: ")
                self.joukkueenPelaajat(joukkue)

            elif komento == "5":
                print("")
                maa = input("maa: ")
                self.maanPelaajat(maa)

            elif komento == "6":
                monta = int(input("kuinka monta: "))
                print("")
                self.enitenPisteita(monta)

            elif komento == "7":
                monta = int(input("kuinka monta: "))
                print("")
                self.enitenMaaleja(monta)

            else:
                self.ohje()


s = Sovellus()
s.suorita()


#import json
#
# class Tilasto:
#    def __init__(self, pelaajat: list):
#        self.__pelaajat = pelaajat
#
#    def pisteiden_mukaan(self,  p):
#        return  p['goals'] + p['assists']
#
#    def maalien_mukaan(self,  p):
#        # jos maaleja yhtä monta, ratkaiseen pelien vähyys
#        return (p['goals'], -p['games'])
#
#    def pelaajan_tiedot(self, nimi: str):
#        for pelaaja in self.__pelaajat:
#            if pelaaja['name'] == nimi:
#                return pelaaja
#
#        return None
#
#    def maat(self):
#        return sorted(list(set(p['nationality'] for p in self.__pelaajat )))
#
#    def joukkueet(self):
#        return sorted(list(set(p['team'] for p in self.__pelaajat )))
#
#    def joukkueen_pelaajat(self, joukkue: str):
#        pelaajat = [ p for p in self.__pelaajat if p['team'] == joukkue]
#        return sorted(pelaajat, key=self.pisteiden_mukaan, reverse=True)
#
#    def maan_pelaajat(self, maa: str):
#        pelaajat = [ p for p in self.__pelaajat if p['nationality'] == maa]
#        return sorted(pelaajat, key=self.pisteiden_mukaan, reverse=True)
#
#    def eniten_pisteita(self, maara):
#        pelaajat = sorted(self.__pelaajat, key=self.pisteiden_mukaan, reverse=True)
#        return pelaajat[0: maara]
#
#    def eniten_maaleja(self, maara):
#        pelaajat = sorted(self.__pelaajat, key=self.maalien_mukaan, reverse=True)
#        return pelaajat[0: maara]
#
# class Sovellus:
#    def __init__(self):
#        self.__tilasto = None
#
#    def ohje(self):
#        ohje = """
# komennot:
# 0 lopeta
# 1 hae pelaaja
# 2 joukkueet
# 3 maat
# 4 joukkueen pelaajat
# 5 maan pelaajat
# 6 eniten pisteitä
# 7 eniten maaleja"""
#        print(ohje)
#
#    def f(self, p: dict):
#        """
#            apumetodi, joka muodostaa pelaajasta tulostukseen sopivan merkkijonon
#        """
#        pisteet = p['goals'] + p['assists']
#        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {pisteet:3}"
#
#    def lue_tiedosto(self):
#        tiedoston_nimi = input("tiedosto: ")
#        with open(tiedoston_nimi) as tiedosto:
#            data = tiedosto.read()
#
#        pelaajat = json.loads(data)
#        print(f"luettiin {len(pelaajat)} pelaajan tiedot")
#        self.__tilasto = Tilasto(pelaajat)
#
#    def hae_pelaaja(self):
#        nimi = input("nimi: ")
#        pelaaja = self.__tilasto.pelaajan_tiedot(nimi)
#        if pelaaja:
#            print(self.f(pelaaja))
#
#    def hae_joukkueet(self):
#        for joukkue in self.__tilasto.joukkueet():
#            print(joukkue)
#
#    def hae_maat(self):
#        for maa in self.__tilasto.maat():
#            print(maa)
#
#    def joukkueen_pelaajat(self):
#        joukkue = input("joukkue: ")
#        for pelaaja in self.__tilasto.joukkueen_pelaajat(joukkue):
#            print(self.f(pelaaja))
#
#    def maan_pelaajat(self):
#        maa = input("maa: ")
#        for pelaaja in self.__tilasto.maan_pelaajat(maa):
#            print(self.f(pelaaja))
#
#    def eniten_pisteita(self):
#        monta = int(input("kuinka monta: "))
#        for pelaaja in self.__tilasto.eniten_pisteita(monta):
#            print(self.f(pelaaja))
#
#    def eniten_maaleja(self):
#        monta = int(input("kuinka monta: "))
#        for pelaaja in self.__tilasto.eniten_maaleja(monta):
#            print(self.f(pelaaja))
#
#    def suorita(self):
#        self.lue_tiedosto()
#        self.ohje()
#        while True:
#            print()
#            komento = input("komento: ")
#            if komento == "0":
#                return
#            elif komento == "1":
#                self.hae_pelaaja()
#            elif komento == "2":
#                self.hae_joukkueet()
#            elif komento == "3":
#                self.hae_maat()
#            elif komento == "4":
#                self.joukkueen_pelaajat()
#            elif komento == "5":
#                self.maan_pelaajat()
#            elif komento == "6":
#                self.eniten_pisteita()
#            elif komento == "7":
#                self.eniten_maaleja()
#
# Sovellus().suorita()
#
