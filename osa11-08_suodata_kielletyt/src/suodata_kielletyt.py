# TEE RATKAISUSI TÄHÄN:



def suodata_kielletyt(merkkijono: str, kielletyt: str):
    return "".join([ sana for sana in merkkijono if sana not in kielletyt ])


if __name__ == '__main__':
    lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)