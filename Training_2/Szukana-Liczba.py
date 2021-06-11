"""

Program, który pozwala użytkownikowi zgadnąć ukrytą w programie liczbę.

"""

szukanaLiczba = 128

i = 0

print ("""Zgadnij jaką liczbę mam na myśli.
Jeśli nie zgadniesz będę Cię naprowadzał.""")

while (i < 1):
    
    zgadywanaLiczba = int(input("Podaj liczbę: "))
    if (zgadywanaLiczba < (szukanaLiczba - 10)):
        print ("Podana przez Ciebie liczba jest za mała! Wybierz jakąś większą!")

    elif (zgadywanaLiczba < szukanaLiczba) and (zgadywanaLiczba >= (szukanaLiczba - 10)):
        print ("Jesteś już blisko, ale liczba jest wciąż za mała!")

    elif (zgadywanaLiczba > szukanaLiczba) and (zgadywanaLiczba <= (szukanaLiczba + 10)):
        print ("Jesteś już blisko, ale liczba jest wciąż za duża!")

    elif (zgadywanaLiczba > (szukanaLiczba + 10)):
        print ("Podana przez Ciebie liczba jest za duża! Wybierz jakąś mniejszą!")

    else:
        print ("Brawo miałem na myśli liczbę", szukanaLiczba, "- liczba została odgadnięta!")
        i += 1

"""
Altrenatywny program.

"""
"""
x = 56 #Szukana Liczba

y = 0 #Zgadywana Liczba

while y != x:
    y = int(input("Podaj liczbę: "))
    if (y < (x - 10)):
        print ("Za mała! Wybierz jakąś większą!")

    elif (y < x) and (y >= (x - 10)):
        print ("Już blisko, ale liczba jest wciąż za mała!")

    elif (y > x) and (y <= (x + 10)):
        print ("Jesteś już blisko, ale liczba jest wciąż za duża!")

    elif (y > (x + 10)):
        print ("Za duża! Wybierz jakąś mniejszą!")

    else:
        print ("Brawo, to ta liczba!")

"""
