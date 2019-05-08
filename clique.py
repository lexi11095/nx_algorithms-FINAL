import networkx as nx
from itertools import combinations
from functions.bool_functions import *

def maximum_clique_set(G):
   for k in range (n(G), 1, -1):
       for S in combinations(V(G), k):
           if is_clique(G, list(S)) == True:
               return list(S)

def clique_number(G):
    return len(maximum_clique_set(G))