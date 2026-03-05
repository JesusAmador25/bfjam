from bfjam import is_hamiltonian
import networkx as nx

atlas = nx.graph_atlas_g()

def test_is_hamiltonian():
    assert is_hamiltonian(atlas[314]) == False
    assert is_hamiltonian(atlas[47]) == (0, 1, 2, 3, 4)
    