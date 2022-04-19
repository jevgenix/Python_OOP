# TEE RATKAISUSI TÄHÄN:
from random import choice

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    result = "".join((choice(kirjaimet) for x in range(len(kirjaimet))))
    return (result[i : i + pituus] for i in range(maara))


if __name__ == "__main__":
    sanagen = sanageneraattori("abcdefg", 3, 5)
    for sana in sanagen:
        print(sana)