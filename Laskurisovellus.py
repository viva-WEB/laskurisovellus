# Ikälaskuri
# 18.12.2023 Valtteri Virtanen, GitHub: https://github.com/viva-WEB/ikalaskuri

# Globaalit muuttujat
risuaita = "#" * 26
rivinvaihto = "\n" * 2

# Aliohjelma tervehdyksen tulostamiseen
def tulosta_tervehdys():
    print(risuaita, "Tervetuloa Laskurisovellukseen!", risuaita, sep="\n", end=rivinvaihto)
    print("Sovellus sisältää joukon eri laskureita ja muuntimia.", end=rivinvaihto)
        
    print("Ohjelman on kirjoitettu Python-perusteisiin ja koodin rakenteisiin keskittyvänä harjoitustyönä joulukuussa 2023",
        "Ohjelma on avoimen lähdekoodin ohjelma. Levitys ja muokkaus on vapaasti sallittua.", sep="\n", end=rivinvaihto)
    print("Valtteri Virtanen (2023)",
        "https://github.com/viva-WEB/", risuaita, sep="\n", end=rivinvaihto) 
    
    syote = input("Paina Enter jatkaaksesi...")
    print(risuaita, end=rivinvaihto)
    return None

# Aliohjelma päävalikolle
def valikko():
    while True:
        print(risuaita, "\t" + "PÄÄVALIKKO", risuaita, sep="\n", end=rivinvaihto)

        print("Valitse toiminto valitsemalla numero valikosta.", end=rivinvaihto)
        print("1. Painoindeksilaskuri")
        print("2. Ikälaskuri")
        print("3. Kuinka monta päivää jouluun?")
        print("4. Kuinka monta päivää synttäreihin?")
        print("5. Yksikkömuunnin")
        print()
        print("0. Lopeta ohjelma")

        break


    return None


# Pääohjelma
def main():
    # Tervehdys aliohjelma
    tulosta_tervehdys()
    valikko()

    print("Kiitos ohjelman käytöstä.")
    return None


main()


