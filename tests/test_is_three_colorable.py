from bfjam import is_three_colorable
import networkx as nx

g = nx.cubical_graph()
atlas = nx.graph_atlas_g()

def test_is_three_colorable():
    assert is_three_colorable(g) == (0, 1, 0, 1, 1, 0, 1, 0)
    assert is_three_colorable(atlas[18]) == False