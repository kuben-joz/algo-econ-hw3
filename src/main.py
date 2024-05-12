import sys
from dataclasses import dataclass
from typing import List
import numpy as np

from readData import readTestFromFile


@dataclass
class Player:
    num_resources: int
    strategy: np.ndarray

# this is equivalent to finding k'th (k = num_resources) largest element and then all larger so O(n) instead of O(nlog(n))
def bestPureResponseAtt(att_player, def_player, battlefields):
    num_resources = att_player.num_resources
    def_strat = def_player.strategy
    for v in def_strat: # todo remove
        assert v >= 0.0 and v <= 1.0
    utils = (1.0-def_strat) * battlefields
    util_idxs = np.argpartition(utils, -num_resources) 
    res = np.zeros_like(def_strat)
    res[util_idxs[-num_resources:]] = 1.0
    return res

# this is equivalent to finding k'th (k = num_resources) largest element and then all larger so O(n) instead of O(nlog(n))
def bestPureResponseDef(att_player, def_player, battlefields):
    num_resources = def_player.num_resources
    att_strat = att_player.strategy
    for v in att_strat: #todo remove
        assert v >= 0.0 and v <= 1.0
    utils = att_strat * battlefields
    util_idxs = np.argpartition(utils, -num_resources)
    res = np.zeros_like(att_strat)
    res[util_idxs[-num_resources:]] = 1.0
    return res


def getEpsilon(
    att_player, def_player, battlefields, best_resp_att=None, best_resp_def=None
):
    att_strat = att_player.strategy
    def_strat = def_player.strategy
    if best_resp_att is None:
        best_resp_att = bestPureResponseAtt(att_player, def_player, battlefields)
    if best_resp_def is None:
        best_resp_def = bestPureResponseDef(att_player, def_player, battlefields)
    pay_att = np.sum(best_resp_att * battlefields * (1 - def_strat))
    pay_def = np.sum((1 - best_resp_def) * battlefields * att_strat)

    return abs(pay_att - pay_def)


def ficticiousPlay(  # todo intial conditions player
    battlefields, num_res_att, num_res_def, epsilon=0.001, max_iters=1_000_000
):
    assert num_res_att > 0 and num_res_att < len(battlefields)
    assert num_res_def > 0 and num_res_def < len(battlefields)
    assert num_res_att < num_res_def
    #battlefields = np.array(battlefields, dtype=np.double)
    num_battlefields = battlefields.shape[0]
    att_play = Player(num_res_att, np.array([num_res_att/num_battlefields] * num_battlefields, dtype=np.double)) # good default init
    def_play = Player(num_res_def, np.array([num_res_def/num_battlefields] * num_battlefields, dtype=np.double)) # good default init
    epsilons = []
    for t in range(1, max_iters + 1):
        resp_att = bestPureResponseAtt(att_play, def_play, battlefields)
        resp_def = bestPureResponseDef(att_play, def_play, battlefields)
        err = getEpsilon(att_play, def_play, battlefields, resp_att, resp_def)
        epsilons.append(err)
        if err <= epsilon:
            break
        for i, (cur, new) in enumerate(zip(att_play.strategy, resp_att)):
            att_play.strategy[i] = (cur * (t - 1) + new) / t
        for i, (cur, new) in enumerate(zip(def_play.strategy, resp_def)):
            def_play.strategy[i] = (cur * (t - 1) + new) / t

    return att_play.strategy, def_play.strategy, np.array(epsilons) # len(epsilons) gives us the number of iterations the algorithm ran for


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


#n, bA, bD, bfs = readTestFromFile(sys.argv[1])
n, bA, bD, bfs = readTestFromFile("../tests/high50.in")


print(n, bA, bD, bfs)

att_strat, def_strat, epsilons = ficticiousPlay(np.array(bfs), bA, bD, max_iters=10_000)
num_iters = len(epsilons)

print(att_strat)
print(def_strat)
print(len(epsilons))
print(epsilons[-1])
