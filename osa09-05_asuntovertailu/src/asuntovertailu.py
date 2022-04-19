class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    def suurempi(self, verrattava):
        return self.nelioita > verrattava.nelioita

    def hintaero(self, verrattava):
        return abs((self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita))
    
    def kalliimpi(self, verrattava):
        if (self.neliohinta * self.nelioita) > (verrattava.neliohinta * verrattava.nelioita):
            return True
        return False
        
if __name__ == "__main__":
    asunto1 = Asunto(1,24,2500)
    asunto2 = Asunto(2,48,3200)
    print(asunto1.hintaero(asunto2))