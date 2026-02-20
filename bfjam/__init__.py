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
