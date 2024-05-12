import sys
from dataclasses import dataclass
from typing import List
import numpy as np

from readData import readTestFromFile


@dataclass
class Player:
    num_resources: int
    strategy: List[float]


# battlefield can just be a list of ints


def bestPureResponseAtt(num_resources, def_strat, battlefields):
    assert len(def_strat) == len(battlefields)
    for v in def_strat:
        assert v >= 0.0 and v <= 1.0
    field_val = []
    for i, prob, util in enumerate(zip(def_strat, battlefields)):
        field_val[i] = ((1 - prob) * util, i)
    field_val = sorted(field_val)[
        -num_resources:
    ]  # find nth largest then iterate for O(n) or serach kth largest individually
    res = [0.0] * len(def_strat)
    for _, i in field_val:
        res[i] = 1.0  # todo maybe ints or bools
    return res


def bestPureResponseDef(num_resources, att_strat, battlefields):
    assert len(att_strat) == len(battlefields)
    for v in att_strat:
        assert v >= 0.0 and v <= 1.0
    field_val = []
    for i, prob, util in enumerate(zip(att_strat, battlefields)):
        field_val[i] = (prob * util, i)
    field_val = sorted(field_val)[
        -num_resources:
    ]  # find nth largest then iterate for O(n) or serach kth largest individually
    res = [0.0] * len(att_strat)
    for _, i in field_val:
        res[i] = 1.0  # todo maybe ints or bools
    return res


def ficticiousPlay(
    battlefields, num_res_att, num_res_def, epsilon=0.1, max_iters=1_000_000
):
    assert num_res_att > 0 and num_res_att < len(battlefields)
    assert num_res_def > 0 and num_res_def < len(battlefields)
    assert num_res_att < num_res_def
    num_battlefields = len(battlefields)
    att_play = Player(num_res_att, [0.0] * num_battlefields)
    def_play = Player(num_res_def, [0.0] * num_battlefields)
    err = float("inf")
    for t in range(1, max_iters + 1):
        resp_att = bestPureResponseAtt(
            att_play.num_resources, def_play.strategy, battlefields
        )
        resp_def = bestPureResponseDef(
            def_play.num_resources, att_play.strategy, battlefields
        )
        for i, cur, new in enumerate(zip(att_play.strategy, resp_att)):
           att_play.strategy[i] = (cur * (t-1) + new) / t
        for i, cur, new in enumerate(zip(def_play.strategy, resp_def)):
            def_play.strategy[i] = (cur * (t-1) + new) / t
        if err <= epsilon:
            break

    return att_play.strategy, def_play.strategy, err, t


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
