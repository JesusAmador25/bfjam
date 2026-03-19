import networkx as nx
import random
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

def generate_random_graph(n):
    """
    Generate a graph with n nodes with random integer weights in each node.

    Args:
        The number of nodes in the graph.

    Returns:
        The graph with random weights.
    """
    g = nx.Graph()
    nodes = [str(i) for i in range(n)]
    g.add_nodes_from(nodes)

    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, 20)
            g.add_edge(nodes[i], nodes[j], weight=weight)
    return g

import matplotlib.pyplot as plt

def random_red_points(n):
    """
    Retuurn n red points in the rectangle (0, 0) x (1, 1)

    Args:
        The number of red points.

    Returns:
        The plot of red points.
    """
    coords = []
    for _ in range(n):
        x = random.random()
        y = random.random()
        coords.append((x, y))

    return coords

def graph_from_random_points(n):
    """
    Return a graph with n red points in the rectangle (0, 0) x (1, 1)

    Args:
        The number of red points.

    Returns:
        The graph with red points.
    """
    g = nx.Graph()
    nodes = random_red_points(n)
    g.add_nodes_from(nodes)
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean(nodes[i], nodes[j])
            g.add_edge(nodes[i], nodes[j], weight = distance)
            plt.plot([nodes[i][0], nodes[j][0]], [nodes[i][1], nodes[j][1]], color='blue')
        plt.scatter(nodes[i][0], nodes[i][1], color='red')
    plt.show()

    return g

def minimum_spanning_tree(graph):
    """
    Find the minimum spanning tree of a graph using Prim's algorithm.
    Args:
        The graph (networkx.Graph with 'weight' attributes).
    Returns:
        The minimum spanning tree of the graph as a set of edges.
    """
    if len(graph.nodes()) == 0:
        return set()
    
    g = graph.copy()
    initial_node = list(g.nodes())[0]
    visited = {initial_node}
    path = []
    edges = []

    for neighbor in g.neighbors(initial_node):
        weight = graph[initial_node][neighbor]['weight']
        edges.append((weight, initial_node, neighbor))
    edges.sort()

    while len(visited) < len(g.nodes()) and edges:
        weight, u, v = edges.pop(0)
        
        if v in visited:
            continue
        

        path.append((u,v,weight))
        visited.add(v)
        
        for neighbor in g.neighbors(v):
            if neighbor not in visited:
                new_weight = graph[v][neighbor]['weight']
                edges.append((new_weight, v, neighbor))
        
        edges.sort()
    
    return path

import matplotlib.pyplot as plt

def draw_mst(graph):

    mst = minimum_spanning_tree(graph)
    mst_graph = nx.Graph()
    mst_graph.add_weighted_edges_from(mst)
    
    position = {node: node for node in graph.nodes()} 
    
    for u, v, weight in mst: 
        x1, y1 = u
        x2, y2 = v 

        plt.plot([x1, x2], [y1, y2], 'b-')


    for nodo in graph.nodes():
        x, y = nodo
        plt.scatter(x, y, color='red')
    
    plt.axis('on')
    plt.show()