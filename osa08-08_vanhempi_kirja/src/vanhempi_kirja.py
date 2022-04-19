# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen

class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
    if kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi:
        print(f"{kirja1.nimi} on vanhempi, se kirjoitettiin {kirja1.kirjoitusvuosi}")
    elif kirja1.kirjoitusvuosi > kirja2.kirjoitusvuosi:
        print(f"{kirja2.nimi} on vanhempi, se kirjoitettiin {kirja2.kirjoitusvuosi}")
    else:
        print(f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.kirjoitusvuosi}")
    
if __name__ == '__main__':
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    vanhempi_kirja(python, everest)
    vanhempi_kirja(python, norma)
