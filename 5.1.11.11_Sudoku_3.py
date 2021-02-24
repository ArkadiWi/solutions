def getRows():
    global tup
    try:
        row0 = int(input('Podaj 9 cyfr w rzędzie nr 1: '))
        row1 = int(input('Podaj 9 cyfr w rzędzie nr 2: '))
        row2 = int(input('Podaj 9 cyfr w rzędzie nr 3: '))
        row3 = int(input('Podaj 9 cyfr w rzędzie nr 4: '))
        row4 = int(input('Podaj 9 cyfr w rzędzie nr 5: '))
        row5 = int(input('Podaj 9 cyfr w rzędzie nr 6: '))
        row6 = int(input('Podaj 9 cyfr w rzędzie nr 7: '))
        row7 = int(input('Podaj 9 cyfr w rzędzie nr 8: '))
        row8 = int(input('Podaj 9 cyfr w rzędzie nr 9: '))

        tup = str(row0) + str(row1) + str(row2) + \
            str(row3) + str(row4) + str(row5) + \
            str(row6) + str(row7) + str(row8)

    except ValueError:
        print('Niewłaściwe dane')
        getRows()


def checkRows(tup, tekst):
    a = 0
    for i in range(9):
        for j in range(9):
            j2 = str(j+1)
            z = (tup.find(j2, a, a+9))
            if z == -1:
                break
        a += 9

    if z == -1:
        print('\t!!!Błąd - źle skonstruowane Sudoku ')
    else:
        print('\t', tekst, ' są OK....')


def checkColumn(tup, tekst):
    # make a new column
    column = ''
    for i in range(9):
        a = 0
        a += i
        for j in range(9):
            column += tup[a]
            a += 9
    # teraz sprawdź w zakresach wystepowanie wszystkich 9 ciu cyfr
    checkRows(column, tekst)


def checkSquares(tup, tekst):
    # make a squares
    square = ''
    square += tup[0:3]+tup[9:12]+tup[18:21]
    square += tup[3:6]+tup[12:15]+tup[21:24]
    square += tup[6:9]+tup[15:18]+tup[24:27]
    square += tup[27:30]+tup[36:39]+tup[45:48]
    square += tup[30:33]+tup[39:42]+tup[48:51]
    square += tup[33:36]+tup[42:45]+tup[51:54]
    square += tup[54:57]+tup[63:66]+tup[72:75]
    square += tup[57:60]+tup[66:69]+tup[75:78]
    square += tup[60:63]+tup[69:72]+tup[78:81]

    checkRows(square, tekst)


getRows()

if len(tup) != 81:
    print('\n\tPodano złą ilość znaków')
    getRows()


print('Sprawdzam wiersze...')
tekst = '...Wiersze'
checkRows(tup, tekst)

print('Sprawdzam kolumny...')
tekst = '...Kolumny'
checkColumn(tup, tekst)

tekst = '"...Kwadraty"'
print('Sprawdzam "kwadraty"...')
checkSquares(tup, tekst)
