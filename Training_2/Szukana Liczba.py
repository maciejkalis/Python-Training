"""

Program, który pozwala użytkownikowi zgadnąć ukrytą w programie liczbę.

"""

szukanaLiczba = 128

i = 0

print ("""Zgadnij jaką liczbę mam na myśli.
Jeśli nie zgadniesz będę Cię naprowadzał.""")

while (i < 1):
    x = int(input("Podaj liczbę: "))
    if (x < 118):
        print ("Podana przez Ciebie liczba jest za mała! Wybierz jakąś większą!")

    elif (x < 128) and (x >= 118):
        print ("Jesteś już blisko, ale liczba jest wciąż za mała!")

    elif (x > 128) and (x <= 138):
        print ("Jesteś już blisko, ale liczba jest wciąż za duża!")


    elif (x > 138):
        print ("Podana przez Ciebie liczba jest za duża! Wybierz jakąś mniejszą!")

    else:
        print ("Brawo miałem na myśli liczbę", szukanaLiczba, "Liczba została odgadnięta!")
        i += 1
