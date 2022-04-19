# TEE RATKAISUSI TÄHÄN:
class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{kirja.nimi} ({kirja.paino} kg)"

class Pakkaus:
    def __init__(self):
        self.lahjat = []
    
    def lisaa_lahja(self, lahja: Lahja):
        self.lahjat.append(lahja)
        
    def yhteispaino(self):
        yht_paino = 0
        for lahja in self.lahjat:
            yht_paino += lahja.paino

        return yht_paino

if __name__ == '__main__':
    kirja = Lahja("Aapiskukko", 2)

    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    
    print(pakkaus.yhteispaino())
    
    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())
