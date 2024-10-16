#zadanie 1
a = 1+2 #dodawanie / typ liczb całkowitych
b = 1+4.5 #dodawanie / typ liczb rzeczywistych (zmiennoprzcinkowych)
c = 3/2 #dzielenie / typ liczb zmiennoprzecinkowych
d = 4/2 #dzielenie / typ liczb zmiennoprzecinkowych
e = 3//2 #dzielenie całkowite (zaokrągla w dół)/ typ liczb całkowitych
f = -3//2 #dzielenie całkowite (zaokrągla w dół) / typ liczb całkowitych
g = 11%2 #modulo (dzielenie z resztą, wyświetla resztę z dzielenia) / typ liczb całkowitych
h = 2**10 #potęgowanie / typ liczb całkowitych
i = 8**(1/3) #potęgowanie (pierwiastkowanie) / typ zmiennoprzecinkowy
print("\n", "Typ a = ", type (a),"\n","Typ b = ",type (b),"\n", "Typ c = ",type (c),"\n", "Typ d = ",type (d),"\n", "Typ e = ",type (e),"\n", "Typ f = ",type (f),"\n", "Typ g = ",type (g),"\n", "Typ h = ",type (h),"\n", "Typ i = ",type (i))

#zadanie 2
a = int(3.0) #zmienia liczby rzeczywiste na całkowite /typ liczb całkowitych
b = float(3) #zmienia liczby całkowite na rzeczywiste / typ liczb zmiennoprzecinkowych
c = float("3") #wyświetla liczby rzeczywiste jako tekst / typ liczb zespolonych
d = str(12.4) #wyświetla liczby jako tekst / typ tekstowy
e = bool(0) #przymuje jedną z dwóch wartości "prawda" lub "fałsz" / typ logiczny
print("\n", a ,"\n", b,"\n", c ,"\n", d  ,"\n", e )

#zadanie 3

imie = "Mikołaj"
kierunek = "IID"
uczelnia = "WSIZ"
print("\n" + "Nazywam się " + imie + ", mój kierunek to " + kierunek + " na " + uczelnia)
'''
print może przyjmować jako argumenty łańcuchy 
znaków ograniczone cudzysłowami (""), liczby, 
wartości logiczne lub obiekty
'''

#zadanie 4
name = input("Jak masz na imię? ")
print(f"Cześć {name}, miło cię poznać")
'''
Na początku program definiuje zmienną (w tym przypdaku name)
Następnie wysyła zapytanie do użytkownika, aby podał mu swoje imię
Ostatni etap to wyświetlenie przez program imienia podanego przez użytkownika i miłe powitanie go
'''

#zadanie 5
a = int(input("Podaj długość pierwszego boku prostokąta: "))
b = int(input("Podaj długość drugiego prostokąta: "))
print("Pole twojego prostokąta wynosi: " + str(a*b) ,"\n", "Obwód twojego prostokąta wynosi: " + str(2*(a+b)))
'''
funkcja input - pozwala użytkownikowi na wprowadzanie własnych danych do programu po przez wysyłanie go niego zapytania
'''

#zadanie 6
d = int(input("Podaj przebytą drogę: ")) #d = droga
s = float(input("Podaj średnie spalanie (l/100km): ")) #s = spalanie
p = 6.5 #p = cena paliwa
z = (d/100) * s #z = zużycie paliwa
k = z*p #k = koszt podróży
print(f"Szacowany koszt podróży wynosi: {k}zł, szacowane zużycie paliwa wynosi: {z}l")

#zadanie 7
import random
d = random.randint(0, 1000) #d = droga, która jest generowana losowo od 0 do 1000 wyrazona w km
s = float(input("Podaj średnie spalanie (l/100km): ")) #s = spalanie
p = 6.5 #p = cena paliwa
z = (d/100) * s #z = zużycie paliwa
k = z*p #k = koszt podróży
print(f"Szacowany koszt podróży wynosi: {k}zł, szacowane zużycie paliwa wynosi: {z}l")
print("Wygenerowana długość przebytej drogi wynosi: ", d)
'''
Wartości zwracane przez algorytm są pseudolosowe, 
ponieważ są one generowane przez program, który generuje ciąg bitów,
natomiast liczby losowe używają zewnętrznej nie przewidywalnej  zmiennej fizycznej
'''