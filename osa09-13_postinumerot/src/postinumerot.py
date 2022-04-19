# Lisää allaolevaan luokkaan pyydetyt ominaisuudet:
class Kaupunki:
    postinumerot = {"Helsinki": "00100", 
                    "Turku": "20100", 
                    "Tampere": "33100", 
                    "Jyväskylä": "40100", 
                    "Oulu": "90100"}

    def __init__(self, nimi: str, asukasluku: int):
        self.__nimi = nimi
        self.__asukasluku = asukasluku

    @property
    def nimi(self):
        return self.__nimi

    @property
    def asukasluku(self):
        return self.__asukasluku

    def __str__(self):
        return f"{self.__nimi} ({self.__asukasluku} as.)"
