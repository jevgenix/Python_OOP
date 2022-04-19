# TEE RATKAISUSI TÄHÄN:
def vokaalilla_alkavat(sanat: list):
    return [sana for sana in sanat if sana[0].lower() in "aeiouyäö"]
 
if __name__ == "__main__":

    klista = ["auto","mopo","Etana","kissa","Koira","OMENA","appelsiini"]
    for vok in vokaalilla_alkavat(klista):
        print(vok)