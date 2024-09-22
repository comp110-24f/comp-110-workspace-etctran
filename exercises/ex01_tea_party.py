"""My second COMP110 excerise. A tea party!"""

__author__ = "730773157"


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for the party."""
    # Everyone will drink 2 cups of tea
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed for the party."""
    # Each tea a guest drinks will be accompanied by 1.5 treats
    return int(tea_bags(people=people) * 1.5)
    # Passing 'people' as a keyword argument to the tea_bags function.


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    # Each tea and cost 50 cents and treats cost 75 cents
    return float(0.5 * tea_count + (0.75 * treat_count))


def main_planner(guests: int) -> None:
    """Prints a summary of the tea party including tea bags, treats, and cost."""
    # Prints a message that shows how many people are attending the tea party.
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Calls the tea_bags function with the number of guests and prints how many tea bags are needed.
    print("Tea Bags: " + str(tea_bags(guests)))
    # Calls the treats function with the number of guests and prints how many treats are needed.
    print("Treats: " + str(treats(guests)))
    # Calls the cost function to calculate the total cost based on the number of tea bags and treats, then prints the total cost of the tea party, formatting the cost as a dollar amount.
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# These lines need to come after ALL function definitions.
# This line is used to see if the script is being run directly or imported as a module in another script.
# Python executes code from top to bottom, so if you placed if __name__ == "__main__" before the function "main_planner" was defined then it would result in nameerror.

if __name__ == "__main__":
    # Tells the user to enter the number of guests for the tea party and converts the input to an integer.
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

# One of the biggest issues I had with this assignment was variable assignment. I had to rewrite a lot of code because variable assingnment was not accepted.
# I overcame this issue by learning how to call functions and input arguments.
# Line 33 was a problem for me, but I solved it by calling the "treats" and "tea_bags" functions. The results of these two functions calls are then passed into the cost fucnction, which calculates the total cost.
