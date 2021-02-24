h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

h_to_min = h * 60
time_tot = h_to_min + m + d
h_end = time_tot // 60
min_end = time_tot % 60
h_end %= 24

print("Godzina zakończenia wydarzenia: ", h_end, ":", min_end)


# Wersja Mariusza:

minZak = (m + d) % 60
godzZak = ((m + d) // 60 + h) % 24

print("Godzina zakończenia wydarzenia: ", godzZak, ":", minZak)
