class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._ainekset = []

    def lisaa_aines(self, ainesosa: str, maara: float):
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")


class SalainenTaikajuoma(Taikajuoma):
    def __init__(self, nimi: str, salasana: str):
        super().__init__(nimi)
        self.__salasana = salasana

    def lisaa_aines(self, ainesosa: str, maara: float, salasana: str):
        if salasana != self.__salasana:
            raise ValueError("Väärä salasana!")
        super().lisaa_aines(ainesosa, maara)

    def tulosta_resepti(self, salasana: str):
        if salasana != self.__salasana:
            raise ValueError("Väärä salasana!")
        super().tulosta_resepti()
        
if __name__ == "__main__":
    
    kutistus = SalainenTaikajuoma("Kutistus maksimus", "testi123")
    kutistus.lisaa_aines("Kärpässieni", 1.5, "testi123")
    kutistus.lisaa_aines("Taikahiekka", 3.0, "testi123")
    kutistus.lisaa_aines("Sammakonkutu", 4.0, "testi123")
    kutistus.tulosta_resepti("testi123")
    kutistus.tulosta_resepti("testi321") # VÄÄRÄ SALASANA!
    