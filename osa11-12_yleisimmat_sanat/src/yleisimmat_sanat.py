# TEE RATKAISUSI TÄHÄN:
from string import punctuation

def yleisimmat_sanat(tiedoston_nimi : str, raja: int):
    with open(tiedoston_nimi) as tiedosto:
        
        teksti = tiedosto.read()
        for merkki in punctuation:
            teksti = teksti.replace(merkki, "")

        teksti = teksti.split()        
        return {sana : teksti.count(sana) for sana in teksti if teksti.count(sana) >= raja}
        

if __name__ == '__main__':
    print(yleisimmat_sanat("comprehensions.txt", 3))
