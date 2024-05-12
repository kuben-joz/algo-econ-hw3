import re


def readTestFromFile(fileName):
    with open(fileName) as f:
        input = f.readlines()
    l1 = re.findall("\d+", input[0])
    l2 = re.findall("\d+", input[1])
    n, ba, bd = int(l1[0]), int(l1[1]), int(l1[2])
    vec = [int(x) for x in l2]

    if n != len(vec):
        raise Exception("n has to be equal to the number of battlefields")

    if ba >= bd:
        raise Exception("Attacker has to have less resources than Defender")

    return n, ba, bd, vec
