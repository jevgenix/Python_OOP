# TEE RATKAISUSI TÄHÄN:
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.tuotteet):
            tuote = self.tuotteet[self.n]
            self.n += 1
            return tuote
        else:
            raise StopIteration

def kauppalistan_tuotteet(kauppalista, maara: int):
    return [tavara[0] for tavara in kauppalista if tavara[1] >= maara]

if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("alkoholiton olut", 24)
    lista.lisaa("ananas", 1)

    print("kauppalistalla vähintään 8 seuraavia tuotteita:")
    for tuote in kauppalistan_tuotteet(lista, 8):
        print(tuote)

    
