# Tee ratkaisusi tähän:
class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

if __name__ == '__main__':
    
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)

    print(f"{python.kirjoittaja}: {python.nimi} ({python.kirjoitusvuosi})")
    print(f"Kirjan {everest.nimi} genre on {everest.genre}")
    
