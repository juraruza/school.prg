import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_list = [rock, paper, scissors]

skore_uzivatele = 0
skore_pocitace = 0

while skore_uzivatele != 10 or skore_pocitace != 10:   
    vyber_uzivatele = int(input("Co si vyberete? Napište 0 pokud kámen, 1 pro papír a 2 pro nůžky\n"))
    if vyber_uzivatele < 3:
        fotka_uzivatele = all_list[vyber_uzivatele]
    elif vyber_uzivatele >=3:
            print("Špatné číslo! Vyber mezi 0, 1, 2")
            while vyber_uzivatele != 0 or vyber_uzivatele != 1 or vyber_uzivatele != 2:
                vyber_uzivatele = int(input("Co si vyberete? Napište 0 pokud kámen, 1 pro papír a 2 pro nůžky\n"))
                if vyber_uzivatele == 0 or vyber_uzivatele == 1 or vyber_uzivatele == 2:
                    fotka_uzivatele = all_list[vyber_uzivatele]
                    break
  
    vyber_pocitace = random.randint(0, 2)
    fotka_pocitace = all_list[vyber_pocitace]

    print(f"Uživatel si vybral:\n {fotka_uzivatele}")
    print(f"Počítač si vybral:\n {fotka_pocitace}")




    if vyber_uzivatele == vyber_pocitace:
        print(f"Nikdo nedostal skóre.")
        print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    elif vyber_uzivatele == 0 and vyber_pocitace == 1:
       print(f"Počítač dostal skóre.")
       skore_pocitace += 1
       print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    elif vyber_uzivatele == 0 and vyber_pocitace == 2:
        print(f"Skóre dostal uživatel.")
        skore_uzivatele += 1
        print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    elif vyber_uzivatele == 1 and vyber_pocitace == 0:
        print(f"Skóre dostal uživatel.")
        skore_uzivatele += 1
        print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    elif vyber_uzivatele == 1 and vyber_pocitace == 2:
        print(f"Počítač dostal skóre.")
        skore_pocitace += 1
        print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    elif vyber_uzivatele == 2 and vyber_pocitace == 0:
        print(f"Počítač dostal skóre.")
        skore_pocitace += 1
        print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    elif vyber_uzivatele == 2 and vyber_pocitace == 1:
        print(f"Skóre dostal uživatel.")
        skore_uzivatele += 1
        print(f"Skóre: PC:{skore_pocitace} Player:{skore_uzivatele}")
    if skore_uzivatele == 10:
        print("Vyhráli jste!")
        break
    elif skore_pocitace == 10:
        print("Prohráli jste!")
        break

    