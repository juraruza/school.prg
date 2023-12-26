def ověření_zápornosti(cislo):
    if cislo > 0:
        print(f"{cislo} je kladné číslo.")
    elif cislo < 0:
        print(f"{cislo} je záporné číslo.")
    else:
        print("Číslo je nula.")

ověření_zápornosti(0)