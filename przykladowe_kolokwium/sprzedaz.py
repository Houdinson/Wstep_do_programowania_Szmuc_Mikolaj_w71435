def dodaj(sprzedaz, nazwa, wyniki):
    sprzedaz[nazwa] = wyniki

def wyswietl(sprzedaz):
    for produkt, wyniki in sprzedaz.items():
        print(f"{produkt}: {sum(wyniki)}")

def usun(sprzedaz, nazwa):
    if nazwa in sprzedaz:
        del sprzedaz[nazwa]
        print(f"Produkt '{nazwa}' został usunięty.")
    else:
        print(f"Produkt '{nazwa}' nie istnieje w bazie.")

def najlepszy_produkt(sprzedaz):
    max_sprzedaz = max([sum(wyniki) for wyniki in sprzedaz.values()])
    najlepsze_produkty = [produkt for produkt, wyniki in sprzedaz.items() if sum(wyniki) == max_sprzedaz]
    return najlepsze_produkty, max_sprzedaz

def srednia_sprzedaz(sprzedaz):
    for produkt, wyniki in sprzedaz.items():
        srednia = sum(wyniki) / len(wyniki)
        print(f"{produkt} - średnia sprzedaż = {srednia:.2f}")

def main():
    sprzedaz = {}

    while True:
        print("\nMenu:")
        print("1. Dodaj nowy produkt")
        print("2. Wyświetl sumaryczną sprzedaż")
        print("3. Usuń produkt")
        print("4. Znajdź produkt o najwyższej sprzedaży")
        print("5. Wyświetl średnią sprzedaż")
        print("6. Zakończ program")

        wybor = input("Wybierz opcję (1-6): ")

        if wybor == "1":
            nazwa = input("Podaj nazwę produktu: ")
            wyniki = input("Podaj trzy wyniki sprzedaży oddzielone spacjami: ")
            wyniki = list(map(int, wyniki.split()))
            if len(wyniki) == 3:
                dodaj(sprzedaz, nazwa, wyniki)
            else:
                print("Błędne dane. Podaj dokładnie trzy liczby.")

        elif wybor == "2":
            wyswietl(sprzedaz)

        elif wybor == "3":
            nazwa = input("Podaj nazwę produktu do usunięcia: ")
            usun(sprzedaz, nazwa)

        elif wybor == "4":
            najlepsze_produkty, max_sprzedaz = najlepszy_produkt(sprzedaz)
            print(f"Najwyższa sprzedaż: {max_sprzedaz}")
            print("Produkty o najwyższej sprzedaży:")
            for produkt in najlepsze_produkty:
                print(f"- {produkt}")

        elif wybor == "5":
            srednia_sprzedaz(sprzedaz)

        elif wybor == "6":
            print("Koniec programu.")
            break

        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
