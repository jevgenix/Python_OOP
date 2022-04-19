# Tee ratkaisusi tähän:
class Henkilo:
    def __init__(self, nimi):
        self.nimi = nimi
    
    def anna_etunimi(self):
        etu_suku = self.nimi.split()
        return etu_suku[0]
    def anna_sukunimi(self):
        etu_suku = self.nimi.split()
        return etu_suku[1]

if __name__ == '__main__':
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())












