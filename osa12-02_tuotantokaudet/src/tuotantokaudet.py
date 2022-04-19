# TEE RATKAISUSI TÄHÄN:
def jarjesta_tuotantokausien_mukaan(alkiot: list):
    def tuotantokausia(alkio):
        
        return alkio['kausia']

    return sorted(alkiot, key=tuotantokausia)


if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }  ]

    for sarja in jarjesta_tuotantokausien_mukaan(sarjat):
        print(f"{sarja['nimi']}  {sarja['kausia']} tuotantokautta")