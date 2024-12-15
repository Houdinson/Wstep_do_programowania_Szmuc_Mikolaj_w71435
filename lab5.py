
#zadanie1
import random
#a
losuj = random.randint(1,22)
print(f"Szczęśliwy numerek na dziś: {losuj}")

# b
tab = [2001, 2004, 2005, 2002, 2003, 2006, 2000]

rok = random.choice(tab)
print(f"Szczęśliwy rocznik to: {rok}")

#c
def lotek():
    liczby = list(range(1, 49))
    wygenerowane_liczby = random.sample(liczby, 6)
    return wygenerowane_liczby
print(f"Wygrane liczby: {lotek()}")


#zadanie2
import math
a = math.sqrt(81)
b = math.pow(8,10)
c1 = math.sqrt(2)+math.sqrt(3)+math.sqrt(6)
c2 = math.ceil(c1)
d = math.sqrt(-5 * -1)
e = math.pow(125, 1/3)

print(f" a = {a} \n b = {b} \n c = {c1} \n d = {d} \n e = {e}")


#zadanie3
import time
czas = int(input("Podaj liczbę sekund: "))
def sekundnik(czas):
    if czas < 0:
        print("Podałeś błędną liczbę")
    else:
        print(czas)
        time.sleep(1)
        if czas: sekundnik(czas - 1)
sekundnik(czas)


#zadanie4
import datetime

dzis = datetime.date.today()
kolos = datetime.date(2025, 1,7)
zajecia = datetime.date(2024, 12,3)
dni_do_kolosa = (kolos - dzis).days
ostatnie_zajecia = (dzis - zajecia).days
print(f"Data kolokwium: {kolos} - pozostało jeszcze {dni_do_kolosa} dni")
print(f"Dziesiejsza data: {dzis}")
print(f"Ostatnie zajęcia odbyły się: {zajecia} - minęło {ostatnie_zajecia} dni")


#zadanie5
import keyword
slowa = ["for", "print", "break", "done", "bad"]
for slowo in slowa:
    if keyword.iskeyword(slowo):
        print(f"{slowo} - jest słowem kluczowym")
    else:
        print(f"{slowo} - nie jest słowem kluczowym")


#zadanie6
import math
import keyword
print("Funkcje w module math: ", [f for f in dir(math) if callable(getattr(math, f))])
print("Funkcje w module tuple: ", [f for f in dir(tuple) if callable(getattr(tuple, f))])
print("Funkcje w module keyword: ", [f for f in dir(keyword) if callable(getattr(keyword, f))])


#zadanie10
import math
import random
x = int(input("Podaj pierwszą liczbę przedziału: "))
y = int(input("Podaj drugą liczbę przedziału"))

krotka = tuple(random.randint(x, y) for _ in range(10))
iloczyn = math.prod(krotka)
dlugosc = len(krotka)
srednia = math.pow(iloczyn, 1/dlugosc)

print(f"Wygenerowana krotka: {krotka}")
print(f"Średnia geometryczna krotki: {srednia}")


#zadanie 11
import random

def zgadywanie_liczby():
    print("Podaj zakres losowania.")
    dolna_granica = int(input("Podaj dolną granicę zakresu: "))
    gorna_granica = int(input("Podaj górną granicę zakresu: "))

    if dolna_granica >= gorna_granica:
        print("Dolna granica musi być mniejsza niż górna granica. Spróbuj ponownie.")
        return

    wylosowana_liczba = random.randint(dolna_granica, gorna_granica)

    print(f"Wylosowano liczbę z zakresu  {dolna_granica} - {gorna_granica}. Masz 3 próby, aby ją zgadnąć.")

    for proba in range(1, 4):
        liczba = int(input(f"Próba {proba}. Zgadnij liczbę: "))

        if liczba < wylosowana_liczba:
            print("Za mało")
        elif liczba > wylosowana_liczba:
            print("Za dużo")
        else:
            print(f"Zgadłeś liczbę {wylosowana_liczba} w {proba}. próbie.")
            return

    print(f"Nie udało ci się zgadnąć. Wylosowana liczba to: {wylosowana_liczba}.")

zgadywanie_liczby()


#zadanie 12
import math
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
kat = int(input("Podaj szerokość kąta ostrego pomiędzy bokami (w stopniach): "))
c = round(math.sqrt((a**2+b**2-2*a*b*math.cos(kat))),2)

if kat >= 90 or kat <= 0:
    print("Podaj prawidłowy kąt")
    return
elif ((a+b) < c) or ((a+c) < b) or ((b+c) < a):
    print("Trójkąt o podanych bokach nie może istnieć")
    return
else:
    pole = round(abs((math.sin(kat)*a*b)/2),2)
    print(f"Długości boków wynoszą: a = {a}, b = {b}, c = {c}. Jego pole wynosi: {pole}")


#zadanie 13
import datetime
import time
import calendar
rok = int(input("Podaj dowolny rok: "))
miesiac = int(input("Podaj miesiąc (liczba): "))
dzien = int(input("Podaj dowolny dzień: "))

def kalendarz(rok, miesiac, dzien):
    if (rok < 1900) or (dzien < 1) or (dzien > 31) or (miesiac < 1) or (miesiac > 12):
        print("Podaj prawidłowe dane")
        print("Minimalny rok - 1900")
        return
    elif dzien > calendar.monthrange(rok, miesiac)[1]:
        print("Podano nie prawidłowy dzień miesiąca.")
        return
    else:
        data = datetime.datetime(rok, miesiac, dzien)

        a = data.timetuple().tm_yday
        b = data.isocalendar()[1]
        c1 = data - datetime.timedelta(weeks=2)
        c2 = data + datetime.timedelta(weeks=2)
        d1 = (6 - data.weekday()) % 7
        d2 = data + datetime.timedelta(days=d1)

        print(f"Podałeś datę (rrrr-mm-dd): ")
        print(f"Dzień roku: {a}")
        print(f"Numer tygodnia: {b}")
        print(f"Data 2 tygodznie przed: {c1.strftime('%Y/%m/%d')}")
        print(f"Data 2 tygodnie po: {c2.strftime('%Y/%m/%d')}")
        print(f"Najbliższa niedziela: {d2.strftime('%Y/%m/%d')}")

        if rok < 1970:
            print("Nie można obliczyć czasu unixowego")
        else:
            e = int(time.mktime(data.timetuple()))
            print(f"Czas unixowy: {e}")
kalendarz(rok, miesiac, dzien)