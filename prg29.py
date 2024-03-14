rok = int(input("Zadejte rok:\n"))
if rok % 4 == 0:
    if rok % 100 == 0:
        if rok % 400 == 0:
            print(f"Rok {rok} je přestupný.")
        else:
            print(f"Rok {rok} není přesupný.")
    else:
        print(f"Rok {rok} je přestupný.")
else:
    print(f"Rok {rok} není přestupný.")