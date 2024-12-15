import temperatura

c1 = 21
f1 = 89
c2 = 35

temp_f = temperatura.c_to_f(c1)
temp_c = temperatura.f_to_c(f1)
temp_k = temperatura.c_to_k(c2)

print(f"Celcius {c1} = Farenheit {temp_f}")
print(f"Farenheit {f1} = Celcius {temp_c}")
print(f"Celcius {c2} = Kelwin {temp_k}")
