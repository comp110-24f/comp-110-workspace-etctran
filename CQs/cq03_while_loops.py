"""My fourth challenge question in COMP110. Practicing loops!"""

__author__ = "730773157"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of characters in a phrase."""
    index: int = 0  # Local variable for index
    count: int = 0  # Local variable for the number of the character in phrase
    while index < len(
        phrase
    ):  # Loop statement, will end once index is greater then the length of the phrase
        if search_char == phrase[index]:
            count += 1  # If the character is equal to the specific index, it adds to the count
        index += 1  # Adds to the index
    return count  # Returns count


print(num_instances(phrase="HelloheLloHEllo", search_char="l"))  # Prints it
