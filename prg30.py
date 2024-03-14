# player_word = input("Zadej slovo, které se bude hádat:")
# player_word.lower
player_word = "python"
doplnovane_slovo = []
zivoty = 9
doplnovani_pismena = 0

for i in range(len(player_word)):
    doplnovane_slovo += "_ "

while zivoty != 0:
    if len(player_word) == doplnovani_pismena:
        print("Vyhrál jsi!")
        break
    
    print(f'Máš {zivoty} životů.')
    print("".join(doplnovane_slovo))
    hadane_pismeno = input("Zadej písmeno, které si myslíš, že patří do slova:")
    if hadane_pismeno in player_word:
        if hadane_pismeno in doplnovane_slovo:
            print("Zadané písmeno už je v hádaném slově!")
        elif hadane_pismeno not in doplnovane_slovo:
            doplnovani_pismena += 1
            x = player_word.index(hadane_pismeno)
            doplnovane_slovo.pop(x*2)
            doplnovane_slovo.insert(x*2, f"{hadane_pismeno}")
    elif hadane_pismeno not in player_word:
        zivoty -= 1
        if zivoty == 0:
            print("Prohrál jsi!")
            break
        print("".join(doplnovane_slovo))
        print(f'Netrefil ses, zbývá ti {zivoty} životů.')