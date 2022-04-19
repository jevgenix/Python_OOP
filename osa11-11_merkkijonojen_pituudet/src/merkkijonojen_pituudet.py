# TEE RATKAISUSI TÄHÄN:


def pituudet(merkkijonot: list):
    return {sana : len(sana) for sana in merkkijonot}


if __name__ == '__main__':
    
    sanalista = ["suo", "kuokka" , "python", "ja", "koodari"]

    sanojen_pituudet = pituudet(sanalista)
    print(sanojen_pituudet)