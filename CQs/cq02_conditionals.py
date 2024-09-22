"""My third challenge question in COMP110"""

__author__ = "730773157"


def guess_a_number() -> None:
    """A fun game where the user guesses a hidden number"""
    secret: int = 7  # Secret number to guess
    guess: str = input("Guess a number:")  # User input that guesses the secret number
    print("Your guess was " + str(guess))  # Prints the users guess
    if int(guess) == 7:  # Used double equal sign and made sure I was comparing two ints
        print("You got it!")
    elif (
        int(guess) < 7
    ):  # Used elif statement to add another pathway for the conditional.
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # If guess > secret
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
