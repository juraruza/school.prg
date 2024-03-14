hmotnost = float(input("Jaká je vaše hmotnost v kilogramech?\n"))
vyska = float(input("Jaká je vaše výška v metrech?\n"))

bmi = hmotnost / vyska**2

if bmi < 18.5:
    print(f"Vaše BMI je {round(bmi, 1)}, máte podváhu.")
elif bmi < 24.9:
    print(f"Vaše BMI je {round(bmi, 1)}, jste v normálu.")
elif bmi < 29.9:
    print(f"Vaše BMI je {round(bmi, 1)}, máte nadváhu.")
elif bmi < 34.9:
    print(f"Vaše BMI je {round(bmi, 1)}, jste obézní.")
else:
    print(f"Vaše BMI je {round(bmi, 1)}, máte extrémní obezitu.")