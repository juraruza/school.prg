import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    while True:
        user_guess = int(input("Hádej číslo mezi 1 a 10: "))
        attempts += 1

        if user_guess == number_to_guess:
            print(f"Správně! Hádal jsi to na {attempts}. pokus.")
            break
        elif user_guess < number_to_guess:
            print("Zkus vyšší číslo.")
        else:
            print("Zkus nižší číslo.")

guess_the_number()