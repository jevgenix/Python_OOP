# TEE RATKAISUSI TÄHÄN:
class Lottorivi:
    def __init__(self, kierroksen_numero: int, lista: list):
        self.kierroksen_numero = kierroksen_numero
        self.lista = lista

    def osumien_maara(self, pelattu_rivi: list):
        return len([ i for i in self.lista if i in pelattu_rivi])

    def osumat_paikoillaan(self, pelattu_rivi):
        return [i if i in self.lista else -1 for i in pelattu_rivi]

if __name__ == '__main__':
    
    oikea = Lottorivi(5, [1,2,3,4,5,6,7])
    oma_rivi = [1,4,7,11,13,19,24]

    print(oikea.osumien_maara(oma_rivi))

    print(oikea.osumat_paikoillaan(oma_rivi))
    

   