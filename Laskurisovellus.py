# Ikälaskuri
# 18.12.2023 Valtteri Virtanen, GitHub: https://github.com/viva-WEB/ikalaskuri

# Globaalit muuttujat
risuaita = "#" * 25
rivinvaihto = "\n" * 2

# Aliohjelma tervehdyksen tulostamiseen
def tulosta_tervehdys():
    print(risuaita, "Tervetuloa ikälaskuriin!", risuaita, sep="\n", end=rivinvaihto)
    print("Ohjelma laskee ikäsi annetulla tarkkuudella syntymäaikasi perusteella.", end=rivinvaihto)
        
    print("Ohjelman on kirjoitettu Python-perusteisiin ja koodin rakenteisiin keskittyvänä harjoitustyönä joulukuussa 2023",
        "Ohjelma on avoimen lähdekoodin ohjelma. Levitys ja muokkaus on vapaasti sallittua.", sep="\n", end=rivinvaihto)
    print("Valtteri Virtanen (2023)",
        "https://github.com/viva-WEB/", risuaita, sep="\n", end=rivinvaihto) 
    print(risuaita)

    


    return None 

# Aliohjelma päävalikolle
def valikko():


    return None


# Pääohjelma
def main():
    # Tervehdys aliohjelma
    tulosta_tervehdys()
    valikko()

    print("Kiitos ohjelman käytöstä.")
    return None


main()



