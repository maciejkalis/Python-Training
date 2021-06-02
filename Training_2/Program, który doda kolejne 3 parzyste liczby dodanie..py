"""

Program, który doda kolejne 3 parzyste liczby dodtanie podane przez użytkownika.

"""

wynik = 0

i = 0

while (i < 3):
    x = int(input("Podaj jakąś dodatnią, parzystą liczbę: "))       
    if ((x > 0) and ((x % 2) == 0)):
        wynik += x

    else:
        print ("Podana liczba jest niedodatnia lub nieparzysta. Spróbuj jeszcze raz")
        continue
    
    i += 1
    
print ("Suma 3 dodatnich i parzystych liczb, które zostały podane, to:", wynik)
