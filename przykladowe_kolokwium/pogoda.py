import pomiary
temp_c = 25
vmps = 10
chpa = 1013

temp_f = pomiary.c_to_f(temp_c)
vkmh = pomiary.predkosc_wiatru(vmps)
cmmhg = pomiary.cisnienie_atmosferyczne(chpa)

print(f"temperatura: {temp_c} C = {temp_f} F")
print(f"Predkosc wiatru: {vmps} m/s = {vkmh} km/h")
print(f"cisnienie atmosferyczne: {chpa} hPa = {cmmhg} mmHg")

dane_pogodowe = [
    {"temperatura": 21, "predkosc_wiatru": 14, "cisnienie": 980},
    {"temperatura": 30, "predkosc_wiatru": 6, "cisnienie": 1070},
    {"temperatura": 17, "predkosc_wiatru": 20, "cisnienie": 1210}
]
for dzien in dane_pogodowe:
    print(dzien)
cisnienie_mmhg = [pomiary.cisnienie_atmosferyczne(dzien["cisnienie"]) for dzien in dane_pogodowe]
srednie_cisnienie = sum(cisnienie_mmhg) / len(cisnienie_mmhg)
print(f"Średnie cisnienie atmosferyczne z trzech ostatnich dni: {srednie_cisnienie:.2f} mmHg")