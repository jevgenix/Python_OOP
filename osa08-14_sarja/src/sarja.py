class Sarja:
    def __init__(self, nimi: str, kausien_maara: int, genre: list):
        self.nimi = nimi
        self.kausien_maara = kausien_maara
        self.genre = genre
        self.arvostelut = []

    def arvostele(self, arvosana: int):
        if arvosana >= 0 or arvosana <= 5:
            self.arvostelut.append(arvosana)

    def keskiarvo(self):
        return sum(self.arvostelut) / len(self.arvostelut)
        
    def __str__(self):
        genret = ", ".join(self.genre)
        if self.arvostelut:
            maara = len(self.arvostelut)
            grade = self.keskiarvo()
            return f"{self.nimi} ({self.kausien_maara} esityskautta)\ngenret: {genret}\narvosteluja {maara}, keskiarvo {grade:.1f} pistettä"
        
        return f"{self.nimi} ({self.kausien_maara} esityskautta)\ngenret: {genret}\nei arvosteluja"

def arvosana_vahintaan(arvosana: float, sarjat:list):
        lista = []
        for i in sarjat:
            if i.keskiarvo() >= arvosana:
                lista.append(i)
        
        return lista

def sisaltaa_genren(genre: str, sarjat:list):
    lista = []
    for i in sarjat:
        if genre in i.genre:
            lista.append(i)

    return lista

if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)
    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)
    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)
    
    sarjat = [s1, s2, s3]
    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)
    
    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)