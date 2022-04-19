class Tavara:
    def __init__(self, tavaran_nimi: str, tavaran_paino: int):
        self.__tavaran_nimi = tavaran_nimi
        self.__tavaran_paino = tavaran_paino
    
    def paino(self):
        return self.__tavaran_paino
        
    def nimi(self):
        return self.__tavaran_nimi

    def __str__(self):
        return f"{self.__tavaran_nimi} ({self.__tavaran_paino} kg)"

class Matkalaukku:
    def __init__(self, maksimipaino: int):
        self.maksimipaino = maksimipaino
        self.tavara_maara = 0
        self.tavaroiden_paino = 0
        self.tavarat = []

    def lisaa_tavara(self, tavara: Tavara):
        if tavara.paino() + self.tavaroiden_paino <= self.maksimipaino:
            self.tavaroiden_paino += tavara.paino()
            self.tavara_maara += 1
            self.tavarat.append(tavara)
    
    def __str__(self):
        if self.tavara_maara == 1:
            return f"{self.tavara_maara} tavara ({self.tavaroiden_paino} kg)"
        return f"{self.tavara_maara} tavaraa ({self.tavaroiden_paino} kg)"
    
    def tulosta_tavarat(self):
        for tavara in self.tavarat:
            print(tavara)
    
    def paino(self):
        return self.tavaroiden_paino

    def raskain_tavara(self):
        if len(self.tavarat) == 0:
            return None
        
        painavin = []
        for tavara in self.tavarat:
            painavin.append(tavara.paino())
        for tavara in self.tavarat:
            if tavara.paino() == max(painavin):
                return tavara
            
class Lastiruuma:
    def __init__(self, maksimipaino: int):
        self.maksimipaino = maksimipaino
        self.maara = 0
        self.tavarat = []

    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if self.maksimipaino - matkalaukku.paino() >= 0:
            self.maara += 1
            self.maksimipaino -= matkalaukku.paino()

            for tavara in matkalaukku.tavarat:
                self.tavarat.append(tavara)

    def __str__(self):
        if self.maara == 1:
            return f"{self.maara} matkalaukku, tilaa {self.maksimipaino} kg"
        return f"{self.maara} matkalaukkua, tilaa {self.maksimipaino} kg"

    def tulosta_tavarat(self):
        for tavara in self.tavarat:
            print(tavara)

if __name__ == '__main__':
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()