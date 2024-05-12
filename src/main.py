import sys
from dataclasses import dataclass
from typing import List
import numpy as np

from readData import readTestFromFile


@dataclass
class Player:
    num_resources: int
    strategy: List[float]


@dataclass
class Battlefield:
    num_arenas: int
    arena_utils: List[int]


def bestPureResponseAtt(num_resources, def_strat, battlefield_utils):
    for v in def_strat:
        assert(v >= 0.0 and v <= 1.0)
    field_val = []
    for i, prob, util in enumerate(zip(def_strat, battlefield_utils)):
        field_val[i] = ((1-prob) * util, i)
    field_val = sorted(field_val)[-num_resources:] # find nth largest then iterate for O(n) or serach kth largest individually
    res = [0]*len(def_strat)
    for _, i in field_val:
        res[i] = 1.0 # todo maybe ints or bools
    return res


def bestPureResponseDef(num_resources, att_strat, battlefield_utils):
    for v in att_strat:
        assert(v >= 0.0 and v <= 1.0)
    field_val = []
    for i, prob, util in enumerate(zip(att_strat, battlefield_utils)):
        field_val[i] = (prob * util, i)
    field_val = sorted(field_val)[-num_resources:] # find nth largest then iterate for O(n) or serach kth largest individually
    res = [0]*len(att_strat)
    for _, i in field_val:
        res[i] = 1.0 # todo maybe ints or bools
    return res

def getPayouts(stratA, stratD):
    if len(stratA) < n or len(stratD) < n:
        raise Exception("Players' strategies have to be of length n")

    res1 = res2 = used1 = used2 = 0

    for i in range(n):
        if (stratA[i] != 0 and stratA[i] != 1) or (stratD[i] != 0 and stratD[i] != 1):
            raise Exception(
                "Players' strategies have to be 0 or 1 for each battlefield"
            )

        used1 += stratA[i]
        used2 += stratD[i]

        if stratA[i] > stratD[i]:
            res1 += bfs[i]
            res2 -= bfs[i]

    if used1 != bA or used2 != bD:
        raise Exception(
            "Players' strategies have to add up to number of their resources"
        )

    return res1, res2


n, bA, bD, bfs = readTestFromFile(sys.argv[1])

print(n, bA, bD, bfs)
