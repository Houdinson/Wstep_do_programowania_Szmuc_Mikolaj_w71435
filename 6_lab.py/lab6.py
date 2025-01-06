import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#zadanie1
df = pd.read_csv('demografia.csv', na_values='.')
print(df)

#zadanie2
df.set_index("KRAJE", inplace=True)
df['2022'] = pd.to_numeric(df['2022'], errors='coerce')
kraj_2022_max = df['2022'].idxmax()
print(f"Kraj z największą populacją w 2022 roku: {kraj_2022_max}")

#zadanie4
dane = {
    'NumerID': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', ' Katarzyna', ' Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', ' Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}
pracownicy = pd.DataFrame(dane)
#a
wysoka_pensja = pracownicy[pracownicy['Pensja'] > 5000]
print(f"Pracownicy z pensją powyżej 5000zł: ", '\n', wysoka_pensja)
#b
wiek_pracownicy = pracownicy.sort_values(by='Wiek')
print(f"Pracownicy posortowani według wieku: ", '\n', wiek_pracownicy)
#c
srednia_pensja = pracownicy.groupby('Stanowisko')['Pensja'].mean()
print(f"Średnia penska według stanowiska: ", '\n', srednia_pensja)
#d
nowe_stanowisko = pd.DataFrame({
    'NumerID': [2, 4],
    'NoweStanowisko': ['Analityk', 'Senior Programista']
})
zmiana_stanowisk = pd.merge(pracownicy, nowe_stanowisko, on='NumerID', how='left')
print(f"Pracownicy po zmianie stanowisk: ", '\n', zmiana_stanowisk)
#e
pracownicy.to_csv('pracownicy.csv', index=False)
#f
wczytane_dane = pd.read_csv('pracownicy.csv')
print("Wczytane dane: ", '\n', wczytane_dane)

#zadanie5
dane_studenci = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}
studenci = pd.DataFrame(dane_studenci)
#a
wysokie_oceny = studenci[studenci['Ocena'] > 4.0]
print("Studenci z oceną większą od 4: ", '\n', wysokie_oceny)
#b
wiek_studenci = studenci.sort_values(by='Wiek')
print("Studenci posortowani według wieku: ", '\n', wiek_studenci)
#c
sredni_wiek = studenci.groupby('Ocena')['Wiek'].mean()
print("Średni wiek: ", '\n', sredni_wiek)
#d
poprawa_ocen = pd.DataFrame({
    'Nr_albumu': [2, 5],
    'OcenaPoprawa': [3.5, 3.0]
})
polaczeni_studenci = pd.merge(studenci, poprawa_ocen, on='Nr_albumu', how='left')
print("Studenci z poprawionymi ocenami: ", '\n', polaczeni_studenci)
#e
studenci.to_csv('studenci.csv', index=False)
#f
wczytani_studenci = pd.read_csv('studenci.csv')
print("Wczytane dane studentów: ", '\n', wczytani_studenci)
#g
nowy_student = {'Nr_albumu': 6, 'Imie': 'Ewa', 'Nazwisko': 'Kowal', 'Ocena': 4.0, 'Wiek': 22}
studenci = studenci._append(nowy_student, ignore_index=True)
print("Nowy student: ", '\n', studenci)
#h
unikalne_oceny = studenci['Ocena'].unique()
print("Unikalne oceny: ", '\n', unikalne_oceny)
#i
oceny_5 = studenci[studenci['Ocena'] == 5.0].shape[0]
print("Liczba studentów z oceną 5: ", '\n', oceny_5)

#zadanie6
kategorie = ['Alkohol', 'Przekąski', 'Wyroby tytoniowe', 'Gorące napoje', 'Zabawki']
sprzedane_produkty = [120, 90, 150, 80, 50]
plt.bar(kategorie, sprzedane_produkty)
plt.title('Udział w sprzedaży')
plt.xlabel('Kategorie')
plt.ylabel('Sprzedaż')
plt.show()

#zadanie7
kategorie = ['Alkohol', 'Przekąski', 'Wyroby tytoniowe', 'Gorące napoje', 'Zabawki']
sprzedane = [120, 90, 150, 80, 50]
sprzedaz = sum(sprzedane)
procent_sprzedazy = [s / sprzedaz * 100 for s in sprzedane]
plt.pie(procent_sprzedazy, labels=kategorie,autopct='%1.f%%', startangle=90)
plt.title('Procentowy udział w sprzedaży')
plt.show()

#zadanie8
czas = [i for i in range(11)]
predkosc = [3 * t for t in czas]
plt.figure(figsize=(10, 6))
plt.scatter(czas, predkosc, alpha=0.7)
plt.title('Zależność czasu od prędkości chwilowej')
plt.xlabel('Czas (s)')
plt.ylabel('Prędkość (m/s)')
plt.grid(True)
plt.show()

#zadanie9
ocena = [2, 3, 3.5, 4, 4.5, 5] * 15
plt.hist(ocena, bins = 6, color = 'red', edgecolor = 'black' , alpha=0.7)
plt.title('Rozkład ocen w grupie studentów')
plt.xlabel('Ocena')
plt.ylabel('Studenci')
plt.grid(True)
plt.show()

#zadanie10
wagi = np.array([128, 64, 32, 16, 8, 4, 2, 1])
liczba_bin = np.random.choice([0, 1], size=8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

wartosc = wartosc_liczby_bin(wagi, liczba_bin)
print("Liczba binarna:", liczba_bin)
print("Wartość liczby binarnej:", wartosc)

#zadanie11
macierz = np.random.randint(0, 50, size=(5, 5))
print("Macierz: ", '\n', macierz)
print("Największy element:", np.max(macierz))
print("Najmniejszy element:", np.min(macierz))
print("Największe elementy w wierszach:", np.max(macierz, axis=1))
print("Największe elementy w kolumnach:", np.max(macierz, axis=0))
print("Suma wierszy:", np.sum(macierz, axis=1))

#zadanie12
tablica_3x3 = np.zeros((3, 3))
tablica_3x3[1:3, 1:3] = 1
print("Tablica z jedynkami: ", '\n', tablica_3x3)

#zadanie13
macierz_5x5 = np.zeros((5, 5))
macierz_5x5[0, :] = 1
macierz_5x5[-1, :] = 1
macierz_5x5[:, 0] = 1
macierz_5x5[:, -1] = 1
print("Macierz z jedynkami na brzegu: ", '\n', macierz_5x5)

def zamiana(macierz):
    return np.where(macierz == 0, 1, 0)

macierz_zmieniona = zamiana(macierz_5x5)
print("Macierz po zamianie: ", '\n', macierz_zmieniona)

#zadanie14
losowa_macierz = np.random.randint(0, 50, size=(5, 5))
print("Losowa macierz: ", '\n', losowa_macierz)
print("Liczba elementów większych od 20:", np.sum(losowa_macierz > 20))
print("Średnia wartość macierzy:", np.mean(losowa_macierz))

#zadanie15
df_oceny = pd.DataFrame({
    'Termin 1': [2, 3, 4, 5, 4.5, 3.5],
    'Termin 2': [4, 4.5, 5, 4, 3.5, 3]
})
df_oceny['Ostateczna'] = df_oceny.mean(axis=1)
df_oceny.plot(kind='bar', figsize=(10, 6), title="Rozkład ocen", colormap='viridis')
plt.xlabel('Student')
plt.ylabel('Ocena')
plt.legend(title='Termin')
plt.show()