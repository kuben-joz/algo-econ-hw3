import random
import sys

seed = int(sys.argv[1])

presetValues = [2, 3, 4, 5]

def getRandomBattlefield(n):
    bfs = presetValues + random.choices(presetValues, weights = [1, 1, 1, 1], k = n - len(presetValues))
    random.shuffle(bfs)
    return bfs

def makeRandomTest(n, bfs):
    ba = 0
    bd = 0
    while (not ba < bd):
        ba = random.randint(1, n - 1)
        bd = random.randint(1, n - 1)
    f = open("../tests/random" + str(n) + ".in", "w")
    f.write("%d %d %d\n" % (n, ba, bd))
    for val in bfs:
        f.write("%d " % val)
    f.close()

def makeLowTest(n, bfs):
    ba = 0
    bd = 0
    while (not ba < bd):
        ba = random.randint(1, n // 3)
        bd = random.randint(1, n // 3)
    f = open("../tests/low" + str(n) + ".in", "w")
    f.write("%d %d %d\n" % (n, ba, bd))
    for val in bfs:
        f.write("%d " % val)
    f.close()

def makeMidTest(n, bfs):
    ba = 0
    bd = 0
    while (not ba < bd):
        ba = random.randint(n // 3 + 1, 2 * n // 3)
        bd = random.randint(n // 3 + 1, 2 * n // 3)
    f = open("../tests/mid" + str(n) + ".in", "w")
    f.write("%d %d %d\n" % (n, ba, bd))
    for val in bfs:
        f.write("%d " % val)
    f.close()

def makeHighTest(n, bfs):
    ba = 0
    bd = 0
    while (not ba < bd):
        ba = random.randint(2 * n // 3, n - 1)
        bd = random.randint(2 * n // 3, n - 1)
    f = open("../tests/high" + str(n) + ".in", "w")
    f.write("%d %d %d\n" % (n, ba, bd))
    for val in bfs:
        f.write("%d " % val)
    f.close()

def makeUnbalancedTest(n, bfs):
    ba = 0
    bd = 0
    while (not (bd - ba > n / 2)):
        ba = random.randint(1, n - 1)
        bd = random.randint(1, n - 1)
    f = open("../tests/unbalanced" + str(n) + ".in", "w")
    f.write("%d %d %d\n" % (n, ba, bd))
    for val in bfs:
        f.write("%d " % val)
    f.close()

def makeTestsOfSize(n):
    random.seed(seed * n * n * n * 1238976453234 + seed * n * n * 4895485641435 + seed * n * 98765438 + seed * 8973425 + 195537456)
    bfs = getRandomBattlefield(n)
    makeRandomTest(n, bfs)
    makeLowTest(n, bfs)
    makeMidTest(n, bfs)
    makeHighTest(n, bfs)
    makeUnbalancedTest(n, bfs)

for i in range(10, 1001):
    makeTestsOfSize(i)