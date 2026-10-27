from itertools import permutations


def generate_all_numbers():
    """Generate every 4-digit number with unique digits."""
    return ["".join(digits) for digits in permutations("0123456789", 4)]


def get_feedback(secret, guess):
    """Return (bulls, cows) for a guess."""
    bulls = sum(secret[i] == guess[i] for i in range(4))

    cows = sum(digit in secret for digit in guess) - bulls

    return bulls, cows


def choose_next_guess(previous_feedback):
    """
    Select a guess consistent with all previous feedback.

    previous_feedback contains tuples:
    (previous_guess, bulls, cows)
    """
    candidates = generate_all_numbers()

    for old_guess, old_bulls, old_cows in previous_feedback:
        candidates = [
            candidate
            for candidate in candidates
            if get_feedback(candidate, old_guess) == (old_bulls, old_cows)
        ]

    if not candidates:
        raise ValueError("No possible secret matches the recorded feedback.")

    # Choose a candidate that has not already been guessed.
    previous_guesses = {guess for guess, _, _ in previous_feedback}

    for candidate in candidates:
        if candidate not in previous_guesses:
            return candidate

    raise ValueError("No new guesses remain.")
