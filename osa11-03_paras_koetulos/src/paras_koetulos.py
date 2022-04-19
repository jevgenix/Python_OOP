# TEE RATKAISUSI TÄHÄN:
class Koesuoritus:
    def __init__(self, nimi: str, arvosana1: int, arvosana2: int, arvosana3: int):
        self.nimi = nimi
        self.arvosana1 = arvosana1
        self.arvosana2 = arvosana2
        self.arvosana3 = arvosana3

    def __str__(self):
        return (f'Nimi:{self.nimi}, arvosana1: {self.arvosana1}' +
            f', arvosana2: {self.arvosana2}, arvosana3: {self.arvosana3}')




def parhaat_tulokset(suoritukset: list):
    return [max(s.arvosana1, s.arvosana2, s.arvosana3) for s in suoritukset]
    
    
    

if __name__ == '__main__':
    suoritus1 = Koesuoritus("Pekka",5,3,4)
    suoritus2 = Koesuoritus("Pirjo",3,4,1)
    suoritus3 = Koesuoritus("Paavo",2,1,3)
    suoritukset = [suoritus1, suoritus2, suoritus3]
    
    print(parhaat_tulokset(suoritukset))

