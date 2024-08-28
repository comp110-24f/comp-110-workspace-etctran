"""My second COMP110 excerise"""

__author__ = "730773157"


def tea_bags(people: int) -> int:
    """Returns the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Returns the number of treats needed"""
    treats = tea_bags(people) * 1.5
    return int(treats)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the cost"""
    # Defining the cost for tea bags and treat counts
    tea_bag_cost = 0.5
    treat_cost = 0.75
    cost = tea_bag_cost * tea_count + (treat_cost * treat_count)
    return float(cost)


def main_planner(guests: int) -> None:
    tea_bags(guests)
    treats(guests)
    total_cost = cost(tea_count, treat_count)
    cost(treat_count, tea_count)
    print(tea_bags)
    print(treats)
    print(cost)
