#zadanie8
from tokenize import endpats

x = -4
while x <= 4:
    y =2*x*x - 5*x - 8
    print(f"X = {x}, wartość funkcji: {y}")
    x += 0.5

#zadanie9
x = int(input("Podaj liczbę całkowitą: "))
while True:
   if x < 0:
       print("Liczba na minusie")
       break
   else:
       print(f"Liczba: {x}")
       break
'''
Po usunięciu instrukcji 'break' z 'else' pętla jest nieskończona
'''

#zadanie10
x = int(input("Podaj pierwszą liczbę całkowitą: "))
y = int(input("Podaj drugą liczbę całkowitą: "))
if x<y:
    print({x})
    x+=1
elif y<x:
    print({y})
    y+=1
else:
    print(f"Liczby są równe")
    print({x})
    x+=1

#zadanie11
x = int(input("Podaj pierwszą liczbę całkowitą: "))
y = int(input("Podaj drugą liczbę całkowitą: "))
while True:
    if x<y:
        print(x)
        x += 1
        if x%2 == 0: break

    elif y < x:
        print(y)
        y += 1
        if y % 2 == 0: break
        print(x)
    else:
        x+=1
        if x%2 == 0: break
'''
zamiana instrukcji 'break' w funkcji 'if', 'elif' i 'else' na 'continue' tworzy nieskonczona petle
'''

#zadanie12
n = int(input("Podaj liczbę studentów: "))

if n <= 0:
    print("Liczba studentów musi być większa od 0")
else:
    suma = 0    #suma punktów wszystkich studentów
    studenci = 0    #licznik studentów
    while studenci < n:
        punkty = float(input(f"Podaj liczbę punktów dla studenta {studenci + 1}: "))
        suma += punkty
        studenci += 1
avg = round(suma / n,2)
print(f"Średnia liczba punktów w grupie wynosi: {avg}")

#zadanie 13
n = int(input("Podaj liczbę studentów: "))

if n <= 0:
    print("Liczba studentów musi być większa od 0")
else:
    suma = 0    #suma punktów wszystkich studentów
    studenci = 0    #licznik studentów

    while True:
        if studenci >= n:
            break

        punkty = float(input(f"Podaj liczbę punktów dla studenta {studenci + 1}: "))
        if (punkty < 0) or (punkty > 100):
            print("Punkty poza skalą 0-100 nie są przyjmowane")
            continue
        suma += punkty
        studenci += 1

avg = suma / n
print(f"Średnia liczba punktów w grupie wynosi: {avg}")

#zadanie14
#program1
import math
while True:
    dana = float(input("Podaj dowolną liczbę: "))
    if (dana >= 0) and dana.is_integer():
        print(f"To jest liczba dodatnia: {dana}")
        continue
    else:
        print("Ta liczba jest ujemna lub nie całkowita")
        break

#program2
while True:
    dana = float(input("Podaj dowolną liczbę: "))
    if (dana >= 0) and dana.is_integer():
        pierwiastek = (dana ** 0.5)
        print(f"Pierwiastek kwadratowy podanej liczby: {pierwiastek}")
    else:
        print("Dziękujemy za skorzystanie z naszej aplikacji")
        break

