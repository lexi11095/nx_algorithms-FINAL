import networkx as nx
from functions.global_properties import *
from functions.local_properties import *
from functions.bool_functions import *
from sample_graphs import *





def cost(G, e):
    return G[e[0]][e[1]]['weight']


def incident_edges(G, T):
    edges = []
    for e in E(G):
        if e[0] in V(T) or e[1] in V(T):
            if e[0] not in V(T) or e[1] not in V(T):
                edges.append(e)
    return edges
    
def min_cost_edge(G, T):
    edges = incident_edges(G, T)
    min_e = edges[0]
    for e in edges:
        if cost(G, e) < cost(G, min_e):
            min_e = e
    return min_e
    

def tree_cost(G, T):
    return sum([cost(G, e) for e in E(T)])

