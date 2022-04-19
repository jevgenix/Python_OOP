class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        return max(set(lista), key = lista.count)

    @classmethod
    def tuplia(cls, lista: list):
        lkm = 0
        tarkistus = {i:lista.count(i) for i in lista}
        for key in tarkistus.values():
            if key > 1:
                lkm += 1
        return lkm

if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))