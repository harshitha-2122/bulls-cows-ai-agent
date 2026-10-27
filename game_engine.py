import random


def generate_number():
    digits = random.sample("0123456789", 4)
    return "".join(digits)


def check_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return cows, bulls
