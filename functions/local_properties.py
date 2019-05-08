import networkx as nx
from functions.global_properties import *

def neighbors(G, v):
    return list(nx.neighbors(G,v))

def degree(G, v):
    return len(neighbors(G, v))

def eccentricity(G, v):
    return len(neighbors(G, v))-1

def degree_sequence(G):
    D = [degree(G, v) for v in V(G)]
    D.sort(reverse = True)
    return D

        
    