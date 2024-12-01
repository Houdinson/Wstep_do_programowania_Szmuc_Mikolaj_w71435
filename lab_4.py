#zadanie1
import math
liczba = float(input("Podaj promień koła: "))
def polekola(r):
    if (r >0):
        A = (math.pi)*(r**2)
        print(f"Pole koła wynosi: {A}")
    else:
        print("Koło nie może posiadać ujemnego promienia")
polekola(liczba)
if liczba >=0:
    print(f"Promień wynosi: {liczba}")
else:
    print("Promień nie może być ujemny")

#zadanie2
import math

a = float(input("Podaj pierwszy bok trapezu: "))
b = float(input("Podaj drugi bok trapezu: "))
h = float(input("Podaj wysokość trapezu: "))

def poletrapezu(a, b, h):
    if (a > 0) and (b > 0) and (h > 0):
        p = ((a+b)*h)/2
        print(f"pole trapezu wynosi: {p}")
    else:
        print("Podany trapez nie istnieje")
poletrapezu(a, b, h)
print(f"Pierwszy bok: {a}, drugi bok: {b}, wysokość: {h}")

#zadanie3
x = float(input("Podaj dowolną liczbę: "))
def check(l):
    if l > 0:
        print(f"Liczba dodatnia: {x}")
    elif l == 0:
        print(f"Liczba to 0")
    else:
        print(f"Liczba ujemna: {x}")
check(x)

#zadanie4
wzrost = float(input("Podaj swój wzrost (cm): "))
waga = float(input("Podaj swoją wagę (kg): "))
bmi_suma = (waga)/(wzrost/100)**2
def bmi(i):
    if i < 18.5:
        print(f"Niedowaga: {bmi_suma}")
    elif i <= 25 and i >= 18.5:
        print(f"Norma: {bmi_suma}")
    elif i <= 30 and i > 25:
        print(f"Nadwaga: {bmi_suma}")
    else:
        print(f"Otyłość: {bmi_suma}")
bmi(bmi_suma)

#zadanie6
imie = input("Podaj swoje imię: ")
w = input("Podaj swój wiek (lub pomiń): ")
if w.strip() and w.isdigit():
    wiek = int(w)
else:
    wiek = 20
def dane(imie, wiek = 20):
    """
    Funkcja wczytuje imię oraz wiek podany przez użytkownika.
    Jeżeli użytkownik nie podał wieku automatycznie zostanie przypisany wiek = 20.
    """
    print(f"Imię: {imie}, wiek: {wiek}")
    
dane(imie, wiek)
print(dane.__doc__)

#zadanie7
a = float(input("Podaj pierwszy bok trójkąta: "))
b = float(input("Podaj drugi bok trójkąta: "))
c = float(input("Podaj trzeci bok trójkąta: "))
def poletrojkata(a, b, c):
    if (a > 0) and (b > 0) and (c > 0):
        pole = (a+b+c)/2
        print(f"Pole trójkąta wynosi: {pole}")
    elif (a+b) < c or (a+c) < b or (b+c) <a:
        print("Podany trójkąt nie istnieje")
    else:
        print("Podany trójkąt nie istnieje")
poletrojkata(a, b, c)
print(f"Pierwszy bok: {a}, drugi bok: {b}, trzeci bok: {c}")

#zadanie8
a = int(input("Podaj liczbę całkowitą: "))
n= int(input("Podaj stopien potegi: "))
def funkcja (a, n):
    if n == 1:
        print("Potęga pierwszego stopnia wynosi 1")
        return a
    else:
        print(f"{a} * funkcja(a, n-1)")
        return a * funkcja(a, n-1)
funkcja(a, n)

#zadanie9
n = int(input("Podaj liczbę n: "))
def ciag(n):
    if n == 1 or n == 2:
        return 1
    else:
        return ciag(n-1) + ciag(n-2)
print(ciag(n))

#zadanie10
n = int(input("Podaj liczbę elementów: "))
def hanoi(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return hanoi(n-1) + 2**(n-1)
print(hanoi(n))

#zadanie11
tekst = input("Podaj dowolny tekst: ")

def obrot(tekst):
    return tekst[::-1]
tekst_obrocony = obrot(tekst)
print(f"Podałeś: {tekst}")
print(f"Odwrócony tekst: {tekst_obrocony}")

#zadanie14
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(f"NWD ({a}, {b}) = {nwd(a,b)}")

#zadanie15
tekst = input("Podaj ciąg znaków: ")
zmiana = tekst.replace(" ", "").lower()
if zmiana == zmiana[::-1]:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

#zadanie16
slowo1 = input("Podaj pierwsze słowo: ")  #  pyta uzytkownika o słowo 1
slowo2 = input("Podaj drugie słowo: ")    #  pyta uzytkownika o slowo 2
licznik_liter = {}                        #  tworzy slownik

def anagram(slowo1, slowo2):
    if len(slowo1) != len(slowo2):
        return False

    for i in slowo1:
        if i in licznik_liter:
            licznik_liter[i] += 1
        else:
            licznik_liter[i] = 1
    for i in slowo2:
        if i not in licznik_liter:
            return False
        licznik_liter[i] -= 1
        if licznik_liter[i] < 0:
            return False
    return all(litera == 0 for litera in licznik_liter.values())

if anagram(slowo1,slowo2):
    print("To są anagramy.")
else:
    print("To nie są anagramy.")