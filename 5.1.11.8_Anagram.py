# Twoim zadaniem jest napisać program, który:

#     prosi użytkownika o wprowadzenie dwóch różnych wyrażeń;
#     sprawdza, czy wprowadzony tekst to anagramy i wyświetla rezultat.

# Uwaga:

#     przyjmij, że dwa puste łańcuchy znaków nie stanowią anagramów;
#     traktuj drukowane i małe litery jednakowo;
#     spacje nie są brane pod uwagę podczas sprawdzania - traktuj je jakby nie istniały
def main():
    word1 = input('Podaj wyraz nr 1 do porównania: ')
    word2 = input('Podaj wyraz nr 2 do porównania: ')
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        print('Wyrazy są takie same')
        main()

    elif not word1.isalpha() or not word2.isalpha():
        print('Błędny łańcuch znaków')
        main()

    else:

        list1 = list(word1)
        list2 = list(word2)
        list1 = sorted(list1)
        list2 = sorted(list2)

        if list1 == [] and list2 == []:
            print('Brak danych do porównania')
        elif list1 != list2:
            print('To nie są anagramy')
        else:
            print('To są anagramy')


main()
