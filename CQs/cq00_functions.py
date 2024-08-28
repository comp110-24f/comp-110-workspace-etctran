"""My first challenge question in COMP110"""

__author__ = "730773157"


def mimic(message: str) -> str:
    """Will return what you say"""
    return message


def main() -> None:
    """Pulls together functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
