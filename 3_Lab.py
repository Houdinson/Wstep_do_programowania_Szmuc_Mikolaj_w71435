#zadanie1
#a
imiona = ["Paweł", "Kacper", "Piotr", "Mikołaj"]
imiona1=sorted(imiona)
for imie in imiona1:
    print(imie, end=' ')
print()

#b
imiona.append("Michał")
imiona.append("Jan")
for imie in imiona:
    print(imie, end=' ')
print()

imie = imiona.pop()
print(imie)

#c
imiona1 = imiona.insert(2, "Mateusz")
for imie in imiona:
    print(imie, end=' ')
print()

#d
imiona.reverse()
for imie in imiona:
    print(imie , end=' ')
print()

i = imiona*2
for imie in i:
    print(imie, end=' ')
print()

#zadanie2
#a
zdanie = input("Podaj zdanie: ").lower()
litery = {litera.lower() for litera in zdanie if litera.isalpha()} #zdefiniowanie litery
alfabet = {chr(i) for i in range(ord('a'), ord('z')+1)} #zdefiniowanie alfabetu

litery_posortowane = sorted(set(zdanie))
for litera in litery_posortowane:
    print(litera, end=' ')
print()

alfabet1 = sorted(alfabet)
for litera in alfabet1:
    print(litera, end=' ')
print()

brakujace_litery = alfabet - litery
brakujace_litery1 = sorted(brakujace_litery)
for litera in brakujace_litery1:
    print(litera, end=' ')
print()

#b
znaki_p = zdanie[::2]
print(f"Zdanie o parzystych indeksach: {znaki_p}")

#c
'''
Rozwiązanie tej części sprawia mi osobiście ogromną trudność
'''

#d
dlugosc_slowa = zdanie.split(' ')
max_slowo = max(dlugosc_slowa, key=len)
print(f"Najdłuższe słowo to: {dlugosc_slowa}, posiada: {max_slowo} znaki/ów")

#e
'''
Rozwiązanie tej części sprawia mi osobiście ogromną trudność
'''

#zadanie3
tekst = input("Podaj ciąg znaków: ")
zmiana = tekst.replace(" ", "").lower()
if zmiana == zmiana[::-1]:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")


#zadanie4
import random
import string

n = int(input("Podaj ilość elementów listy: "))
x = int(input("Podaj długość ciągów znaków: "))

lista = []
for i in range(n):
    len_slowa = random.randint(1, x)
    losowe_slowo = ''.join(random.choices(string.ascii_lowercase, k=len_slowa))
    lista.append(losowe_slowo)

lista1=sorted(lista)
for i in lista:
    print(i, end=' ')
print()

#a
znaki = sum(len(losowe_slowo) for losowe_slowo in lista)
print(f"Suma liter w liście wynosi: {znaki}")

#b
k = sum(losowe_slowo.count('k') for losowe_slowo in lista)
print(f"Ilość liter 'k' w lisćie: {k}")

#c
kt = sum(losowe_slowo.count('kt') for losowe_slowo in lista)
print(f"Ilość liter 'kt' w liście wynosi: {kt}")

#d
s = int(input("Podaj dowolną wartość: "))
dlugosc = sum(len(losowe_slowo) > s for losowe_slowo in lista)
print(f"Ilość ciągów dłuższych niż podana wartość: {dlugosc}")


#zadanie 5
zakupy = {"chleb":5.0, "masło":7.0, "czekolada":12.0, "chipsy":12.0, "piwo":4.0}
suma=0
for i in zakupy:
    suma += zakupy[i]
    print(f"{i} za {zakupy[i]} zł")

suma = sum(zakupy.values())
print(suma)


#zadanie6
prad = {"listopad":300.54, "październik":324.64, "wrzesień":284.42, "sierpień":243.24, "lipiec":314.76, "czerwiec": 266.92}
suma = 0
for i in prad:
    suma += prad[i]
    print(f"{prad[i]} za miesiąc {i}")

#a
suma1 = sum(prad.values())
print(f"Opłata za ostatnie 6 miesięcy: {sum}")

avg = round(suma1 / len(prad), 2)
print(f"Średnia opłata za ostatnie 6 miesięcy: {avg}")

oplata_max= max(prad.values())
oplata_min = min(prad.values())
miesiac_max = [miesiac for miesiac, oplata in prad.items() if oplata == oplata_max][0]
miesiac_min = [miesiac for miesiac, oplata in prad.items() if oplata == oplata_min][0]

print(f"Najwyższa opłata: {miesiac_max} - {oplata_max}, najniższa opłata: {miesiac_min} - {oplata_min}")

#b
ostani_mies = list(prad.keys())[0]
cena_ost_miec = prad[ostani_mies]
if cena_ost_miec > avg:
    print(f"Trzeba zacisnąc pasa")
else:
    print("Wszystko okay")

#zadanie7
import random
a = random.randint(3, 7)
b = random.randint(3, 7)
X={random.randint(0, 10) for _ in range(a)}
Y={random.randint(0, 10) for _ in range(b)}

print(f"Zbiór 'X': {X}")
print(f"Zbiór 'Y': {Y}")
#a
print(f"Czy zbiór 'X' zawiera liczbę 5: {5 in X}")

#b
print(f"Czy zbiór 'X' jest podzbiorem zbioru 'Y': {X.issubset(Y)}")

#c
print(f"Czy zbiór 'Y' jest podzbiorem zbioru 'X': {Y.issubset(X)}")

#d
print(f"Suma zbiorów 'X' i 'Y': {X.union(Y)}")

#e
print(f"Różnica zbiorów 'Y' i 'X': {Y.difference(X)}")

#f
print(f"Różnica zbiorów 'X' i 'Y': {X.difference(Y)}")

#g
print(f"Iloczyń zbiorów 'X' i 'Y': {X.intersection(Y)}")

#h
x_max = max(X)
y_max = max(Y)

if y_max > x_max:
    print(f"Największa liczba obu zbiorów to: {y_max}")
elif y_max < x_max:
    print(f"Największa liczba obu zbiorów to: {x_max}")
else:
    print(f"Największa liczba obu zbiorów to: {x_max}")

#i
usuniety_element = X.pop()
Y.add(usuniety_element)
print(f"Usunięty element: {usuniety_element}")
print(f"Zbiór 'X' po usunięciu elementu: {X}")
print(f"Zbiór 'Y' po dodaniu usuniętego elementu: {Y}")

#j
Y.update(X)
print(f"Zbiór 'X' po przekopiowaniu elementów: {X}")
print(f"Zbiór 'Y' po przekopiowaniu elementów: {Y}")

#k
pusty_x = X.clear()
pusty_y = Y.clear()
print(f"Zbiór 'X' po usunięciu elementów: {pusty_x}")
print(f"Zbiór 'Y' po usunięciu elementów: {pusty_y}")


#zadanie8
import random
while True:
    x = input("Podaj pięć cyfr (rozdzielonych przecinkiem/ bez spacji): ")
    lista = x.split(",")
    if len(lista) != 5:
        print("Podałeś złą ilość elementów.")
        break
    else:
        lista = [int(x) for x in lista]
        for i in lista:
            print(i, end=' ')
        print()
        Y = set(lista)
        print(f"Zbiór 'Y' utworzony z listy: {Y}")
        wylosowany_element = random.choice(list(Y))
        print(f"Wylosowany element: {wylosowany_element}")
        if wylosowany_element == min(Y):
            print("Wylosowany element jest najmniejszą liczbą z podanych.")
        elif wylosowany_element == max(Y):
            print("Wylosowany element jest największą liczbą z podanych.")
        else:
            print("Wylosowany element nie jest ani najmniejszy, ani największy.")
    break

#zadanie9
x = 6 #szerokość planszy
y = 5 # wysokość planszy

przeciwnik = [(0, 1), (2, 3), (2, 4), (3, 4)]
monety = [(1, 1), (2, 0), (3, 3), (5, 3)]
rzeka = 2
print(f"Legenda gry: 'x' - przeciwnik | '*' - moneta | '=' - rzeka | '.' - trawa")
for i in range(y):
    for j in range(x):
        if (i, j) in przeciwnik:
            print("x", end="")
        elif (i, j) in monety:
            print("*", end="")
        elif i == rzeka:
            print("=", end="")
        else:
            print(".", end="")
    print()



