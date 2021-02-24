light = [('***', '*', '***', '***', '* *', '***', '***', '***', '***', '***'),
         ('* *', '*', '  *', '  *', '* *', '*  ', '*  ', '  *', '* *', '* *'),
         ('* *', '*', '***', '***', '***', '***', '***', '  *', '***', '***'),
         ('* *', '*', '*  ', '  *', '  *', '  *', '* *', '  *', '* *', '  *'),
         ('***', '*', '***', '***', '  *', '***', '***', '  *', '***', '***'),
         ]


numeryDoAnalizy = input('Wprowadź cyfry do wyświetlenia...')
dane = []
for znak in numeryDoAnalizy:
    if znak.isdigit():
        dane.append(int(znak))
        # print(type(dane))


for j in range(5):
    print('')
    for i in dane:
        print(light[j][i], end=' | ')

print()
