"""Practing my conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num is < 10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:  # check if this is true
        print("Small Number!")  # "then block"
    else:
        print("Big Number!")
    print("This is the end of the function!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110"
    else:
        return "Keep sleeping. You deserve it. :)"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if the letter ist he first chaacter of the word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"
