# TEE RATKAISUSI TÄHÄN:
class Tyontekija:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)

def laske_alaiset(tyontekija: Tyontekija):
    alaiset = len(tyontekija.alaiset)

    if len(tyontekija.alaiset) >= 1:
        for alainen in tyontekija.alaiset:
            alaiset += laske_alaiset(alainen)
            
    return alaiset
    


if __name__ == "__main__":
    t1 = Tyontekija("Sasu")
    t2 = Tyontekija("Erkki")
    t3 = Tyontekija("Matti")
    t4 = Tyontekija("Emilia")
    t5 = Tyontekija("Antti")
    t6 = Tyontekija("Kjell")
    t1.lisaa_alainen(t4)
    t1.lisaa_alainen(t6)
    t4.lisaa_alainen(t2)
    t4.lisaa_alainen(t3)
    t4.lisaa_alainen(t5)
    print(laske_alaiset(t1))
    print(laske_alaiset(t4))
    print(laske_alaiset(t5))
