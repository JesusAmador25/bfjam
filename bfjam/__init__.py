import itertools
import networkx as nx


def is_hamiltonian_cycle(graph, cycle):
    """
    Checks if a cycle is a Hamiltonian cycle in graph.
    Graph is a NetworkX graph.
    Cycle is a list of vertices.
    """
    n = len(set(cycle))
    if n != graph.order():
        return False
    for i in range(n - 1):
        if not graph.has_edge(cycle[i], cycle[i + 1]):
            return False
    if not graph.has_edge(cycle[-1], cycle[0]):
        return False
    return True

def is_hamiltonian(graph):
    if not nx.is_connected(graph):
        return False
    vertices = list(graph.nodes())
    if len(vertices) < 3:
        return False
    permutacions = itertools.permutations(vertices)
    for permutacion in permutacions:
        if is_hamiltonian_cycle(graph, permutacion):
            return permutacion
    return False

def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False
    return True

def is_three_colorable(graph):
    n = graph.order()# numero de vertices, m numero de edges
    colorings = itertools.product([0, 1, 2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring(graph, coloring):
            return coloring
    return False

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
    combinaciones = itt.product([0, 1], repeat=n)
    for combinacion in combinaciones:
        if sum_of_values(weights, combinacion) <= capacity \
        and sum_of_values(profits, combinacion) >= goal:
            return combinacion
    return False