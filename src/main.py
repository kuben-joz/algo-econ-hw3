import sys

from readData import readTestFromFile

def getPayouts(stratA, stratD):
    if len(stratA) < n or len(stratD) < n:
        raise Exception("Players' strategies have to be of length n")

    res1 = res2 = used1 = used2 = 0

    for i in range(n):
        if (stratA[i] != 0 and stratA[i] != 1) or (stratD[i] != 0 and stratD[i] != 1):
            raise Exception("Players' strategies have to be 0 or 1 for each battlefield")

        used1 += stratA[i]
        used2 += stratD[i]

        if stratA[i] > stratD[i]:
            res1 += bfs[i]
            res2 -= bfs[i]

    if used1 != bA or used2 != bD:
        raise Exception("Players' strategies have to add up to number of their resources")
        
    return res1, res2


n, bA, bD, bfs = readTestFromFile(sys.argv[1])

print (n, bA, bD, bfs)