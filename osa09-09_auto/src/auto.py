# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self):
        self.__sailio = 0
        self.__kilsat = 0

    def __str__(self):
        return f"Auto: ajettu {self.__kilsat} km, bensaa {self.__sailio} litraa"
    
    def tankkaa(self):
        self.__sailio = 60

    def aja(self, km:int):
        if km > self.__sailio:
            km = self.__sailio
        self.__kilsat += km
        self.__sailio -= km
        



if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)