from bfjam import is_proper_coloring
import networkx as nx

g = nx.cubical_graph()
atlas = nx.graph_atlas_g()

def test_is_proper_coloring():
    assert is_proper_coloring(g, [0, 0, 0, 1, 1, 0, 1, 0]) == False
    assert is_proper_coloring(atlas[64], [0, 0, 0, 1, 1, 2])== True