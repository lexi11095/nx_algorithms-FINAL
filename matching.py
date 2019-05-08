from functions.bool_functions import is_matching
from functions.global_properties import n, E
from itertools import combinations
from math import floor


def maximum_matching(G):
    for k in range(floor(n(G)/2), 1, -1):
        for M in combinations(E(G), k):
            if is_matching(G, list(M)) == True:
                return list(M)
            
def matching_number(G):
    return len(maximum_matching(G))

