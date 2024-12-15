
#zadanie 8
from pydoc import stripid

wiek = int(input("Podaj swój wiek: "))
if (wiek > 0 ) and (wiek < 150) :
    if wiek >= 18:
        print("Jesteś pełnoletni")
    else:
        print("Jesteś niepełnoletni")
else:
    print("Podane dane są nie poprawne")

#zadanie 9
wiek = int(input("Podaj swój wiek: "))

if wiek <= 4 :
    print("Wstęp bezpłatny")
elif (wiek < 18) and (wiek > 4):
         print("Wstęp kosztuje 10zł")
elif wiek >= 18:
    student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()
    if student=="tak" :
        print("Wstęp kosztuje 15zł")
    else:
        print("Wstęp kosztuje 20zł")


#zadanie 10
x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
z = int(input("Podaj trzecią liczbę: "))
print(f"Twoje liczby to x = {x}, y = {y}, z = {z} ")
if x <= y and x <= z:
    if y <= z:
        print(f"Liczby rosnąco: {x}, {y}, {z}")
    else:
        print(f"Liczby rosnąco: {x}, {z}, {y}")
elif y <= x and y <= z:
    if x <= z:
        print(f"Liczby rosnąco: {y}, {x}, {z}")
    else:
        print(f"Liczby rosnąco: {y}, {z}, {x}")
else:
    if x <= y:
        print(f"Liczby rosnąco: {z}, {x}, {y}")
    else:
        print(f"Liczby rosnąco: {z}, {y}, {x}")

#zadanie 11
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
print(f"a = {a}, b = {b}, c = {c} ")
d = b**2 - 4 * a * c
print(f"delta = {d}")
if d > 0 :
    if d > 0:
        x1 = (-b + d ** (1 / 2)) / 2 * a
        x2 = (-b - d ** (1 / 2)) / 2 * a
        print(f"x1 = {x1}, x2 = {x1}")
    else:
        x = -b / 2*a
        print(f"x = {x}")
else :
    print("Brak rozwiąząń")

#zadanie12
#a
x = int(input("Podaj liczbę: "))
print(f"Twoja liczba to: {x}")
if x > 0:
    print(f"Wynik twojego działania to: {2*x}")
elif x == 0:
    print(f"Wynik twojego działania to: 0")
else:
    print(f"Wynik twojego działania to: {(-3) * x}")

#b
x = int(input("Podaj liczbę: "))
print(f"Twoja liczba to: {x}")
if x < 1:
    print(f"Wynik twojego działania to: {x}")
elif x >= 1:
    print(f"Wynik twojego działania to: {x**2}")
else:
    print("błąd")

#c
x = int(input("Podaj liczbę: "))
print(f"Twoja liczba to: {x}")
if x > 2:
    print(f"Wynik twojego działania to: {2+x}")
elif x == 2:
    print(f"Wynik twojego działania to: 8")
else:
    print(f"Wynik twojego działania to: {x-4}")

#zadanie 13
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
print(f"a = {a}, b = {b}" )
d = input("Podaj działanie matematyczne (znak działaknia): ")
if d == "*":
    print(f"Wynik mnożenia twoich liczb: {a*b}")
elif d == "+":
    print(f"Wynik dodawania twoich liczb wynosi: {a+b}")
elif d == "-":
    print(f"Wynik odejmowania twoich liczb wynosi: {a-b}")
elif d == "/":
    print(f"Wynik dzielenia twoich liczb wynosi: {a/b}")
elif d == "%":
    print(f"Wynik modluo twoich liczb wynosi: {a%b}")
elif d == "**":
    print(f"Wynik potegowania twoich liczb twoich liczb wynosi: {a**b}")
elif d == "//":
    print(f"Wynik dzielenia całkowitego twoich liczb twoich liczb wynosi: {a**b}")
else:
    print("Wpisz poprawne działanie")
'''
Instrukcja SWITCH umożliwia wybór jednej z kilku opcji na podstawie wartości zmiennej, 
nie jest ona wbudowaną konstrukcją w Pythonie, jednak że odpowiednio użyte 
funkcje if, elif i else pomogą uzyskać nam podobny efekt.
'''

#zadanie14
nazwa_pliku = input("Podaj nazwę pliku")
if nazwa_pliku.endswith('.xls') or nazwa_pliku.endswith('.xlsx'):
    print("Plik jest arkuszem Excel ")
else:
    print("Plik nie jest arkuszem Excel")
'''
ENDSWITH() jest wbudowaną medotą dla obietków str w pythonie, 
sprawdza ona czy łańcuch znaków kończy się określonym ciągiem znaków.
'''

#zadanie15
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
print(f"a = {a}, b = {b}" )
if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań")
    else:
        print("Równanie nie ma rozwiązań")
else:
    x = -b / a
    print(f"Rozwiązanie równania: x = {x}")

#zadanie16
a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
c = float(input("Podaj długośc trzeciego boku trókąta: "))
print(f"a = {a}, b = {b}, c = {c}")
if a + b > c and a + c > b and b + c > a:
    obw = a+b+c
    print(f"Obwód trójkąta wynosi: {obw}")
    p = (a+b+c)/2
    pt = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print(f"Pole trójkąta wynosi: {pt}")
else:
    print("Trójkąt o podanych bokach nie może istnieć")

#zadanie17
litera = input("Wprowadź jedną literę: ")
print(f"Podałeś literę: {litera}")
if len(litera) != 1:
    print("Wprowadź tylko jedną literę!")
else:
    ka = ord(litera) #ka = kod_ASCII
    if 65 <= ka <= 90: #A-Z
        print("Litera jest duża.")
    elif 97 <= ka <= 122: #a-z
        print("Litera jest mała")
    else:
        print("To nie jest litera.")

#zadanie19
litera = input("Wprowadź jedną literę: ")
print(f"Podałeś literę: {litera}")
if len(litera) != 1:
    print("Wprowadź tylko jedną literę!")
else:
    ka = ord(litera) #ka = kod_ASCII
    if 65 <= ka <= 90: #A-Z
        zmieniona_litera = chr(ord(litera) + 32)
        print(f"Zmieniona litera to: {zmieniona_litera}")
    elif 97 <= ka <= 122: #a-z
        zmieniona_litera=chr(ord(litera) - 32)
        print(f"Zmieniona litera to: {zmieniona_litera}")
    else:
        print("To nie jest litera.")
'''
CHR() przyjmuje jako argument liczbę całkowitą, a zwraca odpowiadający jej znak, 
natomiast funkcja ORD() przyjmuje znak a zwraca odpowiadający mu kod ASCII.
Dzięki róznicy 32 pomiędzy kodami ASCII dużych i małych liter program wyświetla prawidłową literę
'''
