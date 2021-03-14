import datetime

print('Program do odkodowania znaków wprowadzonych przez użytkownika')
log = ''
password = ''
solution = ''
tablZnak = [chr(x) for x in range(32, 127)]
liczFun = 0
login = ''
haslo = ''
licznik1 = 0
licznik2 = 0


def inputLogin():
    # Wprowadzanie loginu użytkownika
    global log
    log = input('\n\tPodaj login (max 4 znaki):............\n')
    if len(log) < 1 or len(log) > 4:
        inputLogin()
    else:
        print('\t....Login zaakceptowany....')
        return log


def inputPassword():
    # Wprowadzanie hasła użytkownika
    global password
    password = input('\n\tPodaj hasło (max 4 znaki):..........\n')
    if len(password) < 1 or len(password) > 4:
        inputPassword()
    else:
        print('\t....Hasło zaakceptowane....')
        return password


def solveIt(slowo):
    # Odgadnięcie wpisanych wartości przez użytkownika
    global liczFun, login, haslo, licznik1, licznik2
    licznik = 0
    liczFun += 1

    if len(slowo) == 1:
        for i in range(len(tablZnak)):
            licznik += 1
            solution = tablZnak[i]
            # print(solution, end=' ')
            if solution == slowo:
                break

    elif len(slowo) == 2:
        for i in range(len(tablZnak)):
            for j in range(len(tablZnak)):
                licznik += 1
                solution = tablZnak[i] + tablZnak[j]
                # print(solution, end=' ')
                if solution == slowo:
                    break
            if solution == slowo:
                break
    elif len(slowo) == 3:
        for i in range(len(tablZnak)):
            for j in range(len(tablZnak)):
                for k in range(len(tablZnak)):
                    licznik += 1
                    solution = tablZnak[i] + tablZnak[j] + tablZnak[k]
                    # print(solution, end=' ')
                    if solution == slowo:
                        break
                if solution == slowo:
                    break
            if solution == slowo:
                break
    elif len(slowo) == 4:
        for i in range(len(tablZnak)):
            for j in range(len(tablZnak)):
                for k in range(len(tablZnak)):
                    for l in range(len(tablZnak)):
                        licznik += 1
                        solution = tablZnak[i] + tablZnak[j] + \
                            tablZnak[k] + tablZnak[l]
                        # print(solution, end=' ')
                        if solution == slowo:
                            break
                    if solution == slowo:
                        break
                if solution == slowo:
                    break
            if solution == slowo:
                break
    if liczFun == 1:
        login = solution
        licznik1 = licznik
    elif liczFun == 2:
        haslo = solution
        licznik2 = licznik


inputLogin()
inputPassword()
startTime = datetime.datetime.now()
solveIt(log)
solveIt(password)

endTime = datetime.datetime.now()
elapsedTime = endTime - startTime

if login == log and haslo == password:
    print('\n\t.......Login znaleziony po: ', licznik1, 'próbach.')
    print('\n\t.......Hasło znalezione po: ', licznik2, 'próbach.')
    print('W czasie: ', elapsedTime)
    print('\tLogin to: ', login, '\n\tHasło to: ', haslo)
else:
    print('\n\tNie udało się odgadnąć hasła. Zajęło to: ', elapsedTime)
