import random


cislo_ke_hodnuti = random.randint(1, 10)

pokusy = 0

while True:
    hadane_cislo = int(input("Uhodni číslo mezi 1 a 10: "))
    pokusy += 1

    if hadane_cislo == cislo_ke_hodnuti:
        print(f"Skvělé! Uhodl jsi číslo {cislo_ke_hodnuti} během {pokusy} pokusů.")
        break
    else:
        print("Zkus to znovu. Špatné číslo.")
