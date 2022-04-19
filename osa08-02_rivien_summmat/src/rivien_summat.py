# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    for rivi in matriisi:
        rivi.append(sum(rivi))

if __name__ == '__main__':

    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)