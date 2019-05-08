import networkx as nx
from functions.local_properties import *
from functions.global_properties import V, n


def is_independent(G, S):
    for v in S:
        N = neighbors(G, v)
        if list(set(N) & set(S)) != []:
            return False
    return True

def is_dominating(G, S):
    S_complement = list(set(V(G)) - set(S))
    for v in S_complement:
        N = neighbors(G, v)
        if list(set(N) & set(S)) == []:
            return False
    return True    
    
def is_matching(G, M):
    for edge1 in M:
        v,w = edge1
        for edge2 in M:
            if edge2 != edge1:
                if v in edge1 or w in edge1:
                    return False
            return True
        
def is_clique(G, S):
    for i in range(len(S)):
        N = neighbors(G, S[i])
        for j in range(i + 1, len(S)):
            if S[1 + j] not in N:
                return False
            
def is_spanning(g,h):
    return set(V(g)) == set (V(h))



