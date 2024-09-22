"""My third COMP110 excerise. A simpler version of Wordle!"""

__author__ = "730773157"


def main() -> None:
    """Main function that controls the game by calling input functions and checking the character in the word."""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:  # Function definition and signature for input_word
    """Asks the user to enter a 5 letter word"""
    five_character: str = input(
        "Enter a 5-character word: "
    )  # Variable for user to input a five character word
    if len(five_character) != 5:
        # Uses the len function to decide if the word is five characters
        print(
            "Error: Word must contain 5 characters."
        )  # If it is not five characters print an error
        exit()  # Exits the program early because user did not enter a five character word
    return five_character  # Returns five character


def input_letter() -> str:  # Function definition and signature for input_letter
    """Asks the user to enter a single character"""
    character: str = input(
        "Enter a single character: "
    )  # Variable for the character that will search for itself in the five character word.
    if len(character) != 1:  # Checks if the character length is 1
        print(
            "Error: Character must be a single character."
        )  # Will print an error if character length is not 1
        exit()  # Exits early
    return character  # Returns character


def contains_char(
    word: str, letter: str
) -> None:  # Function def and sig for contains_char
    """Checks each index of the word to see if it matches the letter."""
    print("Searching for " + letter + " in " + word)
    x: int = 0  # Variable to count the number of times the letter is found in the word
    if letter == word[0]:  # If the letter is in index 0 of the word, then
        print(letter + " found at index 0")  # print found at index 0
        x += 1  # and add 1 to the count.
        # I used a reassignment operator because it shortens the code
        # Instead of x = x + 1, I used += to shorten it.
    if letter == word[1]:
        print(letter + " found at index 1")
        x += +1
    if letter == word[2]:
        print(letter + " found at index 2")
        x += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        x += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        x += 1
    if x == 0:  # If the character is not found in the letter
        print(
            "No instances of " + letter + " found in " + word
        )  # Then print no instanes of _ found in ____
    elif x == 1:  # If the character was found once in the word
        print(
            str(x) + " instance of " + letter + " found in " + word
        )  # Then print 1 instace of _ found in _____
        # Had to make this line because if there is 1 instance, instance has to be singular and not plural
    else:  # If x >= 2,
        print(
            str(x) + " instances of " + letter + " found in " + word
        )  # Then print x instances of _ found in _____


if __name__ == "__main__":
    main()
    # Makes it possible to run your Python program as a module
    # Makes it possible for other modules to import your functions and reuse them
