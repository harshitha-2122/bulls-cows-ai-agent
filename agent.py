import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


SYSTEM_PROMPT = """
You are an AI agent playing Bulls and Cows.

Rules:
1. The secret contains exactly four unique digits from 0 to 9.
2. The secret may start with zero.
3. Bulls are correct digits in correct positions.
4. Cows are correct digits in incorrect positions.
5. You cannot see the secret number.
6. You receive feedback after every valid guess.

Your task:
- Make one guess at a time.
- Always use the submit_guess tool.
- Submit exactly four unique digits as a string.
- Never repeat a previous guess.
- Remember all previous guesses and their feedback.
- Use the feedback to improve your next guess.
- Stop guessing once you receive won=true.

IMPORTANT:
Return your next guess immediately.
Do not explain your reasoning before choosing.
When you cannot make a real tool call, write your guess in this exact format:
{"guess": "5678"}
Use four unique digits.
"""


# This describes the tool the AI is allowed to call.
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "submit_guess",
            "description": (
                "Submit one four-digit Bulls and Cows guess to the Python game engine."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "guess": {
                        "type": "string",
                        "description": ("Exactly four unique digits, for example 5072"),
                    }
                },
                "required": ["guess"],
                "additionalProperties": False,
            },
        },
    }
]


def get_model_response(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="required",
        temperature=0.2,
        max_tokens=200,
    )

    message = response.choices[0].message

    print("\nDEBUG: Model response =", message.content)
    print("DEBUG: Tool calls =", message.tool_calls)

    return message
