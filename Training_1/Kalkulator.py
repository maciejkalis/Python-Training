"""
Program ten, to prosty kalkulator napisany w celu przećwiczenia instrukcji warunkowych.

"""

dzialanie = input ("""Witaj w uproszczonej wersji kalkulatora!
Określ rodzaj działania jakie chcesz wykonać na dwóch liczbach wybierając jeden z poniższych symboli:
"+" - dodawanie, "-" - odejmowanie, "*" - mnożenie, "/" - dzielenie, "**" - potęgowanie, "%" - modulo.
Wybierz działanie: """)

a = int(input ("Pierwsza liczba: "))
b = int(input ("Druga liczba: "))

if (dzialanie == "+"):
    print ("Wynik:", a + b)

elif (dzialanie == "-"):
    print ("Wynik:", a - b)

elif (dzialanie == "*"):
    print ("Wynik:", a * b)

elif (dzialanie == "/"):
    print ("Wynik:", a / b)

elif (dzialanie == "**"):
    print ("Wynik:", a ** b)

elif (dzialanie == "%"):
    print ("Wynik:", a % b)

else:
    print ("Nie wprowadzono poprawnego znaku działania")
    


