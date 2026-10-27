Bulls and Cows AI Agent 

An AI-powered version of the classic Bulls and Cows number-guessing game, built using Python and a Large Language Model (LLM).

The AI attempts to guess a secret four-digit number with unique digits. It receives feedback after each guess and uses that feedback to improve its next attempt. A Python-based constraint solver provides a fallback when the LLM does not return a valid guess.

Features:

Generates a random four-digit secret number with unique digits.

Uses an LLM to generate guesses.

Calculates Bulls and Cows feedback.

Tracks previous guesses and feedback.

Uses a Python constraint solver as a fallback.

Integrates with an LLM API through OpenRouter.

Technologies Used:

Python

OpenRouter API

Large Language Models (LLMs)

Pydantic

python-dotenv

Project Structure:

bulls_cows_ai_agent/
├── agent.py
├── game_engine.py
├── main.py
├── schemas.py
├── solver.py
├── test_connection.py
├── .gitignore
├── .env                 # Create locally; do not commit
└── README.md

Setup and Installation:

1. Clone the repository

git clone https://github.com/harshitha-2122/bulls-cows-ai-agent.git
cd bulls-cows-ai-agent

2. Create a virtual environment

python -m venv .venv

Activate it on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

3. Install dependencies

python -m pip install openai python-dotenv pydantic

4. Configure your API key

Create a .env file in the project root and add your own OpenRouter API key:

OPENROUTER_API_KEY=your_api_key_here

Replace the placeholder with your key. Never commit your .env file or share your API key publicly.

Ensure .gitignore contains:

.env
.venv/
__pycache__/
*.py[cod]

5. Run the project

python main.py

How It Works:

The game generates a secret number containing four unique digits.

The LLM proposes a guess.

The game evaluates the guess and returns feedback.

Bulls count digits that are correct in both value and position.

Cows count digits that are correct but in the wrong position.

The agent uses the feedback to make another guess.

If the LLM cannot provide a usable guess, the Python solver selects a candidate consistent with the previous feedback.

The game ends when the AI guesses the secret number or reaches the maximum number of attempts.

Learning Outcomes:

Python modular programming

Working with LLM APIs

Environment-variable management

Constraint solving and candidate filtering

Handling unreliable model responses

Building an AI-assisted game

Future Improvements:

Add automated unit tests.

Compare different LLM models.

Improve guess-selection efficiency.

Track the number of attempts across multiple games.

Add a graphical user interface.

Author:

Harshitha Reddy

GitHub: harshitha-2122