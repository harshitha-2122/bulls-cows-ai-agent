import re

from agent import SYSTEM_PROMPT, get_model_response
from game_engine import check_guess, generate_number
from solver import choose_next_guess

MAX_ATTEMPTS = 20

# Generate the secret number
secret = generate_number()

previous_feedback = []
previous_guesses = set()

# Start the conversation with the LLM
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "user",
        "content": (
            "Play Bulls and Cows. Make one guess using four unique digits. "
            'Return it as JSON: {"guess": "1234"}.'
        ),
    },
]

print("Welcome to the Bulls and Cows AI Agent!")
print("The AI must guess a secret 4-digit number.")
print("-" * 45)

won = False

for turn in range(MAX_ATTEMPTS):
    print(f"\nTurn {turn + 1}")

    guess = None

    # Step 1: Ask the LLM for a guess
    try:
        response = get_model_response(messages)
        content = response.content or ""

        # Extract a guess from JSON text
        match = re.search(r'"guess"\s*:\s*"(\d{4})"', content)

        if match:
            candidate = match.group(1)

            # Accept only four unique digits not guessed before
            if len(set(candidate)) == 4 and candidate not in previous_guesses:
                guess = candidate

    except Exception as error:
        print("LLM request failed:", error)

    # Step 2: Use Python solver if the LLM guess is unusable
    if guess is None:
        print("LLM did not provide a usable guess.")

        try:
            guess = choose_next_guess(previous_feedback)
            print("Python solver selected the guess.")
        except ValueError as error:
            print("Solver error:", error)
            print("Check the recorded feedback and solver.py.")
            break

    # Step 3: Record the guess
    previous_guesses.add(guess)

    # IMPORTANT: check_guess returns (cows, bulls)
    cows, bulls = check_guess(secret, guess)

    print("AI guess:", guess)
    print("Bulls:", bulls)
    print("Cows:", cows)

    # Step 4: Store feedback as (guess, bulls, cows)
    previous_feedback.append((guess, bulls, cows))

    # Step 5: Send feedback to the LLM
    messages.append(
        {
            "role": "user",
            "content": (
                f"Your guess was {guess}. "
                f"Feedback: {bulls} bulls and {cows} cows. "
                "Do not repeat previous guesses. "
                'Return one new guess as JSON: {"guess": "5678"}.'
            ),
        }
    )

    # Step 6: Check if the AI won
    if bulls == 4:
        won = True
        print("\nThe AI guessed the secret number!")
        break

# Step 7: Display the final result
print("\n" + "-" * 45)
print("GAME OVER")
print("Attempts used:", len(previous_guesses))

if won:
    print("Result: AI WON!")
else:
    print("Result: AI DID NOT WIN.")
    print("Secret number:", secret)
