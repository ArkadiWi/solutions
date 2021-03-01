blokow = int(input("Wprowadź liczbę bloków: "))
wysokosc = 0
uzytychBlokow = 0
zostaloBlokow = blokow

while zostaloBlokow > wysokosc:
    wysokosc += 1
    uzytychBlokow += 1 * wysokosc
    zostaloBlokow = blokow - uzytychBlokow


print("Wysokość piramidy wynosi:", wysokosc)
