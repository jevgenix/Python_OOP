# Tee ratkaisusi tähän:
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa
        self.alussa = self.arvo
    def tulosta_arvo(self):
        print("arvo:", self.arvo)
        
    def vahenna(self):
        if self.arvo > 0:
            self.arvo -= 1
            
    def nollaa(self):
        self.arvo -= self.arvo

    def palauta_alkuperainen_arvo(self):
        self.arvo = self.alussa
    
    # ja tänne muut metodit

if __name__ == "__main__":
    laskuri = VahenevaLaskuri(100)
    laskuri.tulosta_arvo()
    laskuri.nollaa()
    laskuri.tulosta_arvo()
    laskuri.palauta_alkuperainen_arvo()
    laskuri.tulosta_arvo()
    