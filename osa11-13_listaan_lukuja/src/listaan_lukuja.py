# TEE RATKAISUSI TÄHÄN:
def listaan_lukuja(luvut: list):
    if len(luvut) % 5 != 0:
        luvut.append(luvut[-1] + 1)

        listaan_lukuja(luvut)

        
if __name__ == "__main__":
    luvut = [1,3,4,5,10,11]
    listaan_lukuja(luvut)
    print(luvut)