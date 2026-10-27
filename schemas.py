from pydantic import BaseModel, field_validator


class GuessInput(BaseModel):
    guess: str

    @field_validator("guess")
    @classmethod
    def validate_guess(cls, value):
        if len(value) != 4:
            raise ValueError("Guess must contain exactly 4 digits")

        if not value.isdigit():
            raise ValueError("Guess must contain only digits")

        if len(set(value)) != 4:
            raise ValueError("All four digits must be unique")

        return value
