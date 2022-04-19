# TEE RATKAISUSI TÄHÄN:
import re


def on_viikonpaiva(merkkijono: str):
    # palauttaa True jos on viikonpäivät, muuten palauttaa False
    return re.search("ma|ti|ke|to|pe|la|su", merkkijono) is not None


def kaikki_vokaaleja(merkkijono: str):
    # palauttaa True jos sisältää vain vokaalit, muuten palauttaa False
    return re.search("^[aeiouyåäö]*$", merkkijono) is not None


def kellonaika(merkkijono: str):
    # palauttaa True jos on oikean muotoinen hh:mm:ss, muuten palauttaa False
    if re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", merkkijono):
        return True
    return False


if __name__ == "__main__":
    print(kellonaika("12:43:01"))
    print(kellonaika("19:zz:04"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("33:66:77"))
