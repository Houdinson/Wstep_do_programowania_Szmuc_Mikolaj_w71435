#zadanie 1
for a in range(1, 101):
    print(a)

for b in range(100, -1 , -1):
    print(b)

for c in range(7, 78, 7):
    print(c)

for d in range(20, -1, -2):
    print(d)

#zadanie 2
a = int(input("Podaj liczbę wierszy: "))
for i in range(a):
    for i in range (a):
        print("*", end=" ")
    print("")

b = int(input("Podaj liczbę wierszy: "))
for i in range(b):
    for i in range(i+1):
        print("*", end=" ")
    print("")

c = int(input("Podaj liczbę wierszy: "))
for i in range(c):
    print(" " * (c - i - 1), end="")
    print("* " * (i + 1))

#zadanie3
n = int(input("Podaj liczbę naturalną (liczbę elementów do wyświetlenia): "))
a = float(input("Podaj pierwszą liczbę rzeczywistą (pierwszy element ciągu):  "))
r = float(input("Podaj drugą liczbę rzeczywistą (różnicę ciągu): "))
print(f"Podałeś liczbę: {n}, {a}, {r}")
if n > 0:
    for i in range(n):
        an = a + i * r
        print(f"Wyraz ciągu {i + 1}: {an}")

#zadanie4
n = int(input("Podaj liczbę naturalną: "))
print(f"Podałeś liczbę: {n}")
if n >= 0 :
    if n == 0 or n == 1:
        print("Silnia twojej liczby 1")
    else:
            liczba = 1
            for i in range(2, n + 1):
                liczba *= i
            print(f"Silnia liczby {n} wynosi: {liczba}")
else:
    print("Silnia można obliczyć tylko dla liczb naturalnych (większych lub równych zeru)")

#zadanie 5
tekst = "Rzeszów jest piękny"
print(tekst[1])
print(tekst[6: 12: 3], tekst[2])

#zadanie 6
tresc = "Python jest super"
print(tresc[0])
print(tresc[-1])
print(tresc[0 : : 2])
print(tresc[10 : ])
print(tresc[-1 : : -1])

#zadanie7
#a)
imie = input("Podaj swoje imię: ")
print(f"Witaj {imie}!")

#b)
wiek = int(input("Podaj swój wiek: "))
if (wiek > 0) and (wiek <150):
    print(f"Twój wiek to: {wiek}")
else:
    print("Podaj poprawny wiek")

#c)
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjal = imie[0].upper() + nazwisko[0].upper()
print(f"Twoje inicjały to: {inicjal}")

#d)
zdanie = input("Podaj łańuch znaków: ")
print(f"Podałeś: {zdanie}")
for i in range(5):
    print(zdanie)

#e)
zdanie = input("Podaj łańuch znaków: ")
zdanie2 = input("Podaj łańuch znaków: ")
print(f"Podałeś: {zdanie}, {zdanie2}")
lancuch = zdanie + zdanie2
print(f"Połączone zdania: {lancuch}")

#f)
zdanie = input("Podaj łańuch znaków: ")
zdanie2 = input("Podaj łańuch znaków: ")
print(f"Podałeś: {zdanie}, {zdanie2}")
pol1 = len(zdanie) // 2
pol2 = len(zdanie2) // 2
lancuch = zdanie[:pol1] + zdanie2[pol2:]
print(f"Połączone zdania: {lancuch}")