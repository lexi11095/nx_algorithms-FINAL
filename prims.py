import networkx as nx
from functions.weighted_functions import min_cost_edge, tree_cost
from functions.bool_functions import is_spanning
from functions.global_properties import V, E

# Final Project Grade: A-


def prims(G, starting_vertex):
    G = nx.read_weighted_edgelist(f'sample_graphs/{G}.txt')
    T = nx.Graph()
    T.add_node(starting_vertex)
    while is_spanning(G, T) == False:
        e = min_cost_edge(G, T)
        T.add_edge(e[0], e[1])
    return V(T), E(T), f'Optimal Cost = {tree_cost(G, T)}'

print(prims('WeightedG1', 'a'))
