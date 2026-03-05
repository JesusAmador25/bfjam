from bfjam import is_hamiltonian_cycle
import networkx as nx

def test_is_hamiltonian_cycle():

    G = nx.Graph()
    G.add_edges_from([(0, 1),(1, 2),(2, 0)])
    assert is_hamiltonian_cycle(G, [0, 1, 2]) == True
    assert is_hamiltonian_cycle(G, [0, 2, 1]) == True
    assert is_hamiltonian_cycle(G, [0, 1]) == False
    assert is_hamiltonian_cycle(G, [0, 1, 3]) == False