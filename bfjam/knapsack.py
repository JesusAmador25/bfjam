import itertools

def sum_of_values(values, keys):
    """
    Calculates the sum of products of corresponding elements from two lists.

    Args:
        values (list): A list of numerical values.
        keys (list): A list of numerical keys (multipliers), typically 0 or 1.

    Returns:
        float or int: The calculated weighted sum.
    """
    total_sum = 0
    n = len(values)
    for i in range(n):
        total_sum += keys[i] * values[i]
    return total_sum

def knapsack_problem(capacity, goal, weights, profits):
    """
    Solves the 0/1 Knapsack Problem to find a combination of items
    that fits within a given capacity and meets a minimum profit goal.

    Args:
        capacity (int or float): The maximum weight capacity of the knapsack.
        goal (int or float): The minimum total profit to achieve.
        weights (list): A list of weights for each item.
        profits (list): A list of profits for each item.

    Returns:
        tuple or bool: A tuple representing the chosen items (1 if chosen, 
        0 if not)
        if a valid combination is found, otherwise False.
    """
    n = len(weights)
    combinaciones = itertools.product([0, 1], repeat=n)
    for combinacion in combinaciones:
        if sum_of_values(weights, combinacion) <= capacity \
        and sum_of_values(profits, combinacion) >= goal:
            return combinacion
    return False

