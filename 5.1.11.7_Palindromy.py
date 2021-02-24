# #Twoim zadaniem jest napisać program, który:

#     prosi użytkownika o wprowadzenie tekstu;
#     sprawdza, czy wprowadzony tekst jest palindromem i wyświetla rezultat.

# Uwaga:

#     przyjmij, że pusty łańcuch znaków nie jest palindromem;
#     traktuj drukowane i małe litery jednakowo;
#     spacje nie są brane pod uwagę podczas sprawdzania - traktuj je jakby nie istniały;
#     istnieje więcej niż kilka rozwiązań - postaraj się znaleźć więcej niż jedno.

sentence = input('Podaj tekst do sprawdzenia: ')
sentence = sentence.replace(' ', '')
sentence = sentence.lower()

if not sentence.isalpha():
    print('Błędny łańcuch znaków')
else:
    listSent = list(sentence)
    listSent.reverse()
    revSentence = (''.join(listSent))
    print('\n')
    if sentence == revSentence:
        print('To jest palindrom')
    else:
        print('To nie jest palindrom')


# 2-gi sposób:
    listSent2 = list(sentence)
    d = len(listSent2)
    for i in range(d // 2):
        listSent2[i], listSent2[d - i - 1] = listSent2[d - i - 1], listSent2[i]
    revSentence2 = (''.join(listSent2))
    print('\n')
    if sentence == revSentence2:
        print('To jest palindrom')
    else:
        print('To nie jest palindrom')
