# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.lista = []

    def lisaa_luku(self, luku:int):
        self.lista.append(luku)

    def lukujen_maara(self):
        return len(self.lista)

    def summa(self):
        return sum(self.lista)
    
    def keskiarvo(self):
        if len(self.lista) > 0:
            return(sum(self.lista) / len(self.lista))



tilasto = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()

print('Anna lukuja:')
while True:
    luku = int(input())
    if luku == -1:
        break
    if luku % 2 == 0:
        parilliset.lisaa_luku(luku)
    else:
        parittomat.lisaa_luku(luku)
    tilasto.lisaa_luku(luku)
        
print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print('Parillisten summa:', parilliset.summa())
print('Parittomien summa:', parittomat.summa())
    
        


