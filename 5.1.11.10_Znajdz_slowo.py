# Twoim zadaniem jest napisanie programu, który odpowiada
# na następujące pytanie: czy znaki, które tworzą pierwszy
# łańcuch znaków są schowane wewnątrz drugiego łańcucha znaków?

slowo1 = input('''\tPodaj słowo, w którym będziemy szukać
\tsłowa, które podasz za chwilę: ''')
slowo2 = input('\n\tA teraz podaj slowo, które mam znależć: ')

slowo1 = slowo1.lower()
slowo1 = slowo1.replace(' ', '')
slowo2 = slowo2.lower()
slowo2 = slowo2.replace(' ', '')


if slowo1.find(slowo2) != -1:
    print('Słowo', slowo2, 'znajduje się w słowie', slowo1)
else:
    print('Słowo', slowo2, 'nie znajduje się w słowie', slowo1)
