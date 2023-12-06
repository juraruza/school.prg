try:
    x = int(input("Zadej číslo: "))
    result = 10 / x
    print(result)
except ZeroDivisionError:
    print("Nelze dělit nulou.")
except ValueError:
    print("Zadej platné číslo.")