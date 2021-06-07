"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
"""

#ver. 1


i = 0

slownik = {'Help': 'Jest to interaktywny slownik testowy.'}

while (i < 1):
    dzialanie = (input("""Witaj w interaktywnym słowniku!
D - Dodanie nowej definicji do słownika,
U - Usunięcie wybranej pozycji ze słownika,
W - Wyszukiwanie haseł.
S - Wyświetl aktualny stan słownika.
Wybierz operację: """))
    
    if dzialanie == 'D' or dzialanie == 'd':
        print ()        
        hasloDodawane = input ('Podaj nowe hasło do słownika: ')        
        definicja = input ('Utwórz definicję do podanego hasła: ')        
        slownik.update ({hasloDodawane: definicja})
        print ('\n')
        print('Dodano następujące hasło wraz z definicją:', hasloDodawane, '-', definicja)
        print ('\n')

    elif dzialanie == 'U' or dzialanie == 'u':        
        print ('\n')        
        hasloUsuwane = input ('Podaj hasło jakie chcesz usunąć ze słownika: ')

        if hasloUsuwane in slownik:                               
            del (slownik[hasloUsuwane])
            print ('\n')
            print('Usunięto hasło:', hasloUsuwane)
            print ('\n')

        else:
            print ('\n')
            print('Podanego hasła nie ma w słowniku')
            print ('\n')            

    elif dzialanie == 'W' or dzialanie == 'w':
        print ('\n')        
        hasloWyszukiwane = input ('Wyszukaj hasło: ')
        
        if hasloWyszukiwane in slownik:
            print ('\n')            
            print(hasloWyszukiwane, '-', slownik.get(hasloWyszukiwane))
            print ('\n')
        
        else:
            dodanieHaslaWybor = input("""Nie ma takiego hasła w słowniku.
Czy chcesz je dodać?
T - Tak, N - Nie
Wybierz działanie: """)
            
            if dodanieHaslaWybor == 'T' or dodanieHaslaWybor == 't':
                definicja2 = input ('Utwórz definicję do podanego hasła: ')            
                slownik.update ({hasloWyszukiwane: definicja2})                
                print ('\n')            
                print('Dodano następujące hasło wraz z definicją:', hasloWyszukiwane, '-', slownik[hasloWyszukiwane])
                print ('\n')

            elif dodanieHaslaWybor == 'N' or dodanieHaslaWybor == 'n':                
                print ('\n')                
                print('W porządku, powracamy do menu głównego')
                print ('\n')

            else:
                print ('\n')                
                print('Nie dokonałeś poprawnego wyboru. Powracamy do menu głównego')
                print ('\n')

    elif dzialanie == 'S' or dzialanie == 's':
        print()
        print ('W słowniku znajdują się następujące hasła:')
        
        for key in slownik:
            print()                       
            print (key, '-', slownik[key])
            print()

