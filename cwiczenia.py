#sposób I
import f_mat

x = 10
x1 = 3
a = 10
b = 5
kwadrat = f_mat.kwadrat(x)
szescian = f_mat.szescian(x1)
dodaj = f_mat.dodaj(a, b)

print(f"Kwadrat liczby 10 wynosi: {kwadrat}")
print(f"Sześcian liczby 3 wynosi: {szescian}")
print(f"Suma liczb 10 i 5 wynosi: {dodaj}")


#sposób II
from f_mat import kwadrat
from f_mat import szescian
from f_mat import dodaj

kwadrat1 = kwadrat(x)
szescian1 = szescian(x1)
dodaj1 = dodaj(a, b)

print(f"Kwadrat liczby 10 wynosi: {kwadrat1}")
print(f"Sześcian liczby 3 wynosi: {szescian1}")
print(f"Suma liczb 10 i 5 wynosi: {dodaj1}")