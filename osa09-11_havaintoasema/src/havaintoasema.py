# TEE RATKAISUSI TÄHÄN:
class Havaintoasema:
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__havainnot = []
    
    def lisaa_havainto(self, havainto: str):
        self.__havainnot.append(havainto)
    
    def havaintojen_maara(self):
        return len(self.__havainnot)

    def viimeisin_havainto(self):
        if len(self.__havainnot) == 0:
            return ""
        return self.__havainnot[-1]

    def __str__(self):
        return f"{self.__nimi}, {len(self.__havainnot)} havaintoa"

if __name__ == '__main__':
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)
    