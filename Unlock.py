print('Program do odkodowania znaków wprowadzonych przez użytkownika')
log = ''
password = ''
solution = ''


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


tablZnak = [chr(x) for x in range(32, 127)]
tablZnak.insert(0, chr(0))
print(tablZnak)


def solveIt(slowo):
    # Odgadnięcie wpisanych wartości przez użytkownika
    print('Jestem w funkcji i szukam: ' + slowo)
    wait = input('wait')
    lst = []
    licznik = 0
    global solution

    if len(log) > 0:
        for i in range(len(tablZnak)):
            for j in range(len(tablZnak)):
                licznik += 1
                solution = tablZnak[i]+tablZnak[j]
                lst.append(solution)
                print(solution)
                if solution == slowo:
                    print('Szukane słowo to: ' + solution)
                    break
    print(lst)
    print(licznik)

    # for i in range(len(tablZnak)):
    #     for j in range(len(tablZnak)):
    #         for k in range(len(tablZnak)):
    #             for l in range(len(tablZnak)):
    #                 solution = chr(tablZnak[l]) + \
    #                     chr(tablZnak[k])+chr(tablZnak[j])+chr(tablZnak[i])
    #                 print(solution)


inputLogin()
print(len(tablZnak))
print(len(log))
solveIt(log)


# log1 = chr(tablZnak[4])+chr(tablZnak[60])
# print(log1)

# for znak in tablZnak:
#     print(chr(znak))
