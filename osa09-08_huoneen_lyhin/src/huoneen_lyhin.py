# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:
    def __init__(self):
        self.henkilot_huonessa = []

    def lisaa(self, henkilo: Henkilo):
        self.henkilot_huonessa.append(henkilo)

    def on_tyhja(self):
        return len(self.henkilot_huonessa) == 0
    
    def tulosta_tiedot(self):
        yhteinenpituus = 0
        for henkilo in self.henkilot_huonessa:
            yhteinenpituus += henkilo.pituus
        print(f"Huoneessa on {len(self.henkilot_huonessa)} henkilöä, yhteispituus {yhteinenpituus} cm")
        for henkilo in self.henkilot_huonessa:
            print(f"{henkilo.nimi} ({henkilo.pituus})")
    
    def lyhin(self):
        if self.on_tyhja():
            return None
            
        lyhin = []
        for henkilo in self.henkilot_huonessa:
            lyhin.append(henkilo.pituus)
        for henkilo in self.henkilot_huonessa:
            if henkilo.pituus == min(lyhin):
                return henkilo
    
    def poista_lyhin(self):
        lyhin = self.lyhin()
        if lyhin:
            self.henkilot_huonessa.remove(lyhin)
        return lyhin

if __name__ == '__main__':
    huone = Huone()
    print("Huone tyhjä?", huone.on_tyhja())
    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Auli", 186))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Terhi", 185))
    print("Huone tyhjä?", huone.on_tyhja())
    huone.tulosta_tiedot()