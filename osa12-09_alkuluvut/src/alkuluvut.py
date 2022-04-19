# TEE RATKAISUSI TÄHÄN:
def alkuluvut():
    luku = 1
    while True:
        if onko_alkuluku(luku):
            yield luku
        luku += 1

def onko_alkuluku(n: int):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True



if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))
