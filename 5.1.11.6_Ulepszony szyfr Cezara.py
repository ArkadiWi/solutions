# Ultimate version

def podajKlucz():
    global klucz
    try:
        klucz = int(input('Wprowadź długość klucza szyfrującego: '))
    except ValueError:
        print('Klucz ma być liczbą całkowitą')
        podajKlucz()


tekst = input("Wpisz wiadomość: ")
klucz = 0
podajKlucz()


szyfr = ''

for char in tekst:
    if not char.isalpha():
        szyfr += char
    elif ord(char) >= 97 and ord(char) <= 122:
        kod = ord(char) + klucz
        if kod > ord('z'):
            kod = ord('a')
        szyfr += chr(kod)

    elif ord(char) >= 65 and ord(char) <= 90:
        kod = ord(char) + klucz
        if kod > ord('Z'):
            kod = ord('A')
        szyfr += chr(kod)

print(szyfr)
