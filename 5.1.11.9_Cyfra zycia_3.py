# #Twoim zadaniem jest napisać program, który:
# prosi użytkownika o podanie swojej daty urodzin
# (w formacie RRRRMMDD, or RRRRDDMM, or MMDDRRRR -
# w zasadzie kolejność cyfr nie ma znaczenia)
# zwraca Liczbę Życia dla wprowadzonej daty.

def run():

    print('''\n\tWprowadz swoją datę urodzenia w formaci RRRRMMDD
        lub jak chcesz, byle by bez spacji i innych znaków\n''')
    # lifeNum = input('Podaj date urodzenia: ')
    lifeNum = 0
    try:
        lifeNum = int(input('Podaj date urodzenia: '))
        # int(lifeNum)
    except ValueError:
        print('Wprowadź liczbę całkowitą')
        # run()

    a, a1 = 0, 0
    lista1 = []
    lista2 = []
    lifeNum = str(lifeNum)
    lifeNum = lifeNum.replace(' ', '')

    if len(lifeNum) == 8:
        lista1 = lifeNum

        for i in range(len(lista1)):
            a += (int(lista1[i]))

        if a > 9:
            lista2 = str(a)

            for i in range(len(lista2)):
                a1 += (int(lista2[i]))
            print('Liczba życia to: ', a1)

        else:
            print('Liczba życia to: ', a)

    else:
        print('Błędna ilość znaków')
        run()


run()
