# TEE RATKAISUSI TÄHÄN:
class Tietokone:
    def __init__(self, malli: str, nopeus: int):
        self.__malli = malli
        self.__nopeus = nopeus

    @property
    def malli(self):
        return self.__malli

    @property
    def nopeus(self):
        return self.__nopeus

class KannettavaTietokone(Tietokone):
    def __init__(self, malli: str, nopeus: int, paino: int):
        super().__init__(malli, nopeus)
        self.paino = paino

    def __str__(self):
        return f"{self.malli}, {self.nopeus} MHz, {self.paino} kg"

if __name__ == '__main__':
    ipm = KannettavaTietokone("IPM MikroMauri", 1500, 2)
    print(ipm)