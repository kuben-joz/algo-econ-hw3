def readTestFromFile(fileName):
    f = open(fileName, "r")
    input = f.read().split("\n")
    l1 = input[0].split(" ")
    l2 = input[1].split(" ")

    n, ba, bd = int(l1[0]), int(l1[1]), int(l1[2])
    vec = [int(x) for x in l2]

    if n != len(vec):
        raise Exception("n has to be equal to the number of battlefields")
    
    if ba < bd:
        raise Exception("Attacker has to have less resources than Defender")

    return n, ba, bd, vec