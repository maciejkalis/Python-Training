"""
Program liczący powierzchnię wybranej z menu figury stworzony w celu przećwiczenia tworzenia własnych funkcji.

"""
import math

def pole_prostokąta (a, b):
    return a * b

def pole_kwadratu (a):
    return a ** 2

def pole_trójkąta (a, h):
    return 0.5 * a * h

def pole_trapezu (a, b, h):
    return ((a + b) * h) * 0.5

def pole_koła (r):
    return math.pi * (r ** 2)    


jakaFigura = input("""Witaj w programie liczącym pole wybranej figury!
Pole jakiej figury chcesz obliczyć?
Prostokąt, kwadrat, trójkąt, trapez, koło.
Wybierz figurę: """)

if jakaFigura == "prostokąt":
    a = int(input("Podaj długość pierwszego boku prostokąta: ")) 
    b = int(input("Podaj długość drugiego boku prostokąta: "))

    print ("Pole prostokąta to:", pole_prostokąta (a, b), "j^2")

elif jakaFigura == "kwadrat":
    a = int(input("Podaj długość boku kwadratu: ")) 
    
    print ("Pole kwadratu to:", pole_kwadratu (a), "j^2")

elif jakaFigura == "trójkąt":
    a = int(input("Podaj długość podstawy trójkąta: ")) 
    h = int(input("Podaj wysokość trójkąta: "))
    
    print ("Pole trójkąta to:", pole_trójkąta (a, h), "j^2")

elif jakaFigura == "trapez":
    a = int(input("Podaj długość dłuższej podstawy trapezu: "))
    b = int(input("Podaj długość krótszej podstawy trapezu: "))
    h = int(input("Podaj wysokość trapezu: "))
    
    print ("Pole trapezu to:", pole_trapezu (a, b, h), "j^2")

elif jakaFigura == "koło":
    r = int(input("Podaj promień koła: ")) 
    
    print ("Pole koła to:", pole_koła (r), "j^2")

else:
    print ("Nie wybrałeś odpowiedniej figury")
