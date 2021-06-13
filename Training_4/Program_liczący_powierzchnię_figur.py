"""
Program liczący powierzchnię wybranej z menu figury stworzony w celu przećwiczenia tworzenia własnych funkcji.

"""
    
import Figury

jakaFigura = input("""Witaj w programie liczącym pole wybranej figury!
Pole jakiej figury chcesz obliczyć?
Prostokąt, kwadrat, trójkąt, trapez, koło.
Wybierz figurę: """)

if jakaFigura == "prostokąt":
    a = int(input("Podaj długość pierwszego boku prostokąta: ")) 
    b = int(input("Podaj długość drugiego boku prostokąta: "))

    print ("Pole prostokąta to:", Figury.pole_prostokąta (a, b), "j^2")

elif jakaFigura == "kwadrat":
    a = int(input("Podaj długość boku kwadratu: ")) 
    
    print ("Pole kwadratu to:", Figury.pole_kwadratu (a), "j^2")

elif jakaFigura == "trójkąt":
    a = int(input("Podaj długość podstawy trójkąta: ")) 
    h = int(input("Podaj wysokość trójkąta: "))
    
    print ("Pole trójkąta to:", Figury.pole_trójkąta (a, h), "j^2")

elif jakaFigura == "trapez":
    a = int(input("Podaj długość dłuższej podstawy trapezu: "))
    b = int(input("Podaj długość krótszej podstawy trapezu: "))
    h = int(input("Podaj wysokość trapezu: "))
    
    print ("Pole trapezu to:", Figury.pole_trapezu (a, b, h), "j^2")

elif jakaFigura == "koło":
    r = int(input("Podaj promień koła: ")) 
    
    print ("Pole koła to:", Figury.pole_koła (r), "j^2")

else:
    print ("Nie wybrałeś odpowiedniej figury")

