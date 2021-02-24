def runProgram ():

    import random


    def drukujTablice ():
        print ('+-------+-------+-------+')
        print ('|       |       |       |')
        print ('|  ',stanPola[0],'  |  ',stanPola[1],'  |  ',stanPola[2],'  |')
        print ('|       |       |       |')
        print ('+-------+-------+-------+')
        print ('|       |       |       |')
        print ('|  ',stanPola[3],'  |  ',stanPola[4],'  |  ',stanPola[5],'  |')
        print ('|       |       |       |')
        print ('+-------+-------+-------+')
        print ('|       |       |       |')
        print ('|  ',stanPola[6],'  |  ',stanPola[7],'  |  ',stanPola[8],'  |')
        print ('|       |       |       |')
        print ('+-------+-------+-------+')


    def zajmijPole(nrPola):
        if nrPola <1 or nrPola > 9:
            print ("Pole poza zakresem")
            pole = int(input("Podaj swoje pole:..."))
            zajmijPole(pole)
            
        elif stanPola[nrPola-1] == 'X' or stanPola[nrPola-1] == 'O':
            print ('Pole już zajęte')
            pole = int(input("Podaj swoje pole:..."))
            zajmijPole(pole)
            
        else:
            if stanPola[nrPola-1] != 'O':
                stanPola[nrPola-1] = 'O'
                drukujTablice ()
                   


    def czyWygralGracz ():
        if stanPola[0] == 'O'and  stanPola[1] == 'O' and  stanPola[2] == 'O':
            return True    
        elif stanPola[6] == 'O'and stanPola[7] == 'O' and stanPola[8] == 'O':
            return True
        elif stanPola[0] == 'O' and stanPola[3] == 'O' and stanPola[6] == 'O':
            return True    
        elif stanPola[2] == 'O' and stanPola[5] == 'O' and stanPola[8] == 'O':
            return True
        else:
            return False
     

    def czyWszystkiePolaZajete ():
        licznik = 0
        for i in range (9):
            if stanPola[i] =='O' or stanPola[i] == 'X':
                licznik += 1

        if licznik == 9:
            print ("\n!!!!!!!!!!!!!!!!!")
            return True
        else:
            return False
       
        
    def ruchKomputera ():
        ruchOK = False
        while ruchOK == False:
            komPole = random.randint (0,8)
            print ("Wylosowałem nr:....", komPole+1)
            if stanPola[komPole] != 'O' and stanPola[komPole] != 'X':
                stanPola[komPole] = 'X'
                ruchOK = True
                drukujTablice ()
            else:
                ruchOK = False
        

    def czyWygralKomputer ():
        if stanPola[0] == 'X'and  stanPola[1] == 'X' and  stanPola[2] == 'X':
            return True
        elif stanPola[3] == 'X' and stanPola[4] == 'X' and stanPola[5] == 'X':
            return True    
        elif stanPola[6] == 'X'and stanPola[7] == 'X' and stanPola[8] == 'X':
            return True
        elif stanPola[0] == 'X' and stanPola[3] == 'X' and stanPola[6] == 'X':
            return True 
        elif stanPola[1] == 'X' and stanPola[4] == 'X' and stanPola[7] == 'X':
            return True   
        elif stanPola[2] == 'X' and stanPola[5] == 'X' and stanPola[8] == 'X':
            return True
        elif stanPola[0] == 'X' and stanPola[4] == 'X' and stanPola[8] == 'X':
            return True
        elif stanPola[2] == 'X' and stanPola[4] == 'X' and stanPola[6] == 'X':
            return True        
        else:
            return False





    stanPola = [1,2,3,4,"X",6,7,8,9]


# petla wywołująca funkcję 'While koniec != True

    print ("Zaczyna komputer stawiając znak X na środku planszy")
    print ("Wybierz swoje pole, na którym znajdzie się znak O")
    
    koniec = False
    drukujTablice ()
    while koniec != True:
    
# Wypisanie instrukcji gry i tabeli 'plansza'
    
        
   
# Komputer stawia 'X' na środku pola - nr: 5
# Ruch gracza
# Wywolanie funkcji ktora sprawdza, czy pole jest wolne
# zmiana stanu pola i drukowanie tablicy 

        pole = int(input("Podaj swoje pole:..."))
        zajmijPole(pole)

    
        # warunekPola = 1  

        # if warunekPola == 1:
        #     pole = int(input("Podaj swoje pole:..."))
        #     zajmijPole(pole)
                    
                
        

        if czyWygralGracz() == True:                  #  Wywołanie definicji - Sprawdzenie, czy zwyciestwo gracza
            print ("\nGratulacje wygrałeś tę rundę")
            koniec = True
            break
        
        else:              
            if czyWszystkiePolaZajete () == True:           # Wywołanie definicji - sprawdz czy sa wolne pola, jak nie, to koniec == True
                print ("Koniec gry.... Wszystkie pola zajęte!!!!")
                koniec = True
                break

     #  Wywołanie definicji - Ruch komputera, losowe postawienie znaku 'X'

        print ("A teraz pora na mój ruch.....")
        ruchKomputera ()

        if czyWygralKomputer() == True:                  #  Wywołanie definicji - Sprawdzenie, czy zwyciestwo gracza
            print ("\n Wygrałem tę rundę!!!")
            # drukujTablice ()
            koniec = True
            break
        
        else:              
            if czyWszystkiePolaZajete () == True:               #  Wywołanie definicji - sprawdz czy sa wolne pola, jak nie, to koniec == True
                print ("\nKoniec gry...wszystkie pola zajęte!!!")
                koniec = True
                break
            
        


x = 'y'
while x == 'y':
    runProgram ()
    print ("\nKoniec gry.....może jesze raz? ")
    x = input("\ny or n: ")
   







#  Wywołanie definicji - Jeśli pole wolne to zaznaczenie 'X' na wybranym polu,
#  zmiana wartosci tabeli 'plansza'

#  Wywołanie definicji - Sprawdzenie, czy zwyciestwo komputera




#Zakończenie programu

