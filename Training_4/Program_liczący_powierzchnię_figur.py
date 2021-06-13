"""
Program liczący powierzchnię wybranej z menu figury stworzony w celu przećwiczenia tworzenia własnych funkcji.

"""
    
import Figury

from enum import IntEnum

Menu_Figury = IntEnum ('Menu_Figury', 'PROSTOKĄT KWADRAT TRÓJKĄT TRAPEZ KOŁO')

jakaFigura = int(input("""Witaj w programie liczącym pole wybranej figury!
Pole jakiej figury chcesz obliczyć?
1 - Prostokąt, 2 - Kwadrat, 3 - Trójkąt, 4 - Trapez, 5 - Koło.
Wybierz figurę: """))

if jakaFigura == Menu_Figury.PROSTOKĄT:
    a = int(input("Podaj długość pierwszego boku prostokąta: ")) 
    b = int(input("Podaj długość drugiego boku prostokąta: "))

    print ("Pole prostokąta to:", Figury.pole_prostokata (a, b), "j^2")

elif jakaFigura == Menu_Figury.KWADRAT:
    a = int(input("Podaj długość boku kwadratu: ")) 
    
    print ("Pole kwadratu to:", Figury.pole_kwadratu (a), "j^2")

elif jakaFigura == Menu_Figury.TRÓJKĄT:
    a = int(input("Podaj długość podstawy trójkąta: ")) 
    h = int(input("Podaj wysokość trójkąta: "))
    
    print ("Pole trójkąta to:", Figury.pole_trojkata (a, h), "j^2")

elif jakaFigura == Menu_Figury.TRAPEZ:
    a = int(input("Podaj długość dłuższej podstawy trapezu: "))
    b = int(input("Podaj długość krótszej podstawy trapezu: "))
    h = int(input("Podaj wysokość trapezu: "))
    
    print ("Pole trapezu to:", Figury.pole_trapezu (a, b, h), "j^2")

elif jakaFigura == Menu_Figury.KOŁO:
    r = int(input("Podaj promień koła: ")) 
    
    print ("Pole koła to:", Figury.pole_kola (r), "j^2")

else:
    print ("Nie wybrałeś odpowiedniej figury")

