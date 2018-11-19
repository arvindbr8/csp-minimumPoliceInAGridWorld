    # solutions:15,5,41

def main():
    def conflict(element):
        if element >= n*n:
            return False
        xj, yj = scoreMatKey[element]
        for i in range(len(sol)):
            xi, yi = scoreMatKey[sol[i]]
            if xi == xj or yi == yj or (float(yj - yi) / float(xj - xi) in [1.0, -1.0]):
                return True
        return False

    f = open('input.txt', 'r')

    n = int(f.readline().strip())
    # n = 9
    p = int(f.readline().strip())
    # p = 9

    #n, p = 12,7

    s = int(f.readline().strip())

    timesteps = []
    for _ in range(s):
        builder = []
        for _ in range(12):
            x, y = [int(x) for x in f.readline().strip().split(',')]

            builder.append([x, y])
        timesteps.append(builder)
    scoreMat = {}
    f.close()
    for i in timesteps:
        for j in i:
            try:
                # index = (j[1]*n)+j[0]
                index = j[0], j[1]
                scoreMat[index] = scoreMat[index] + 1
            except:
                scoreMat[index] = 1

    for i in range(n):
        str1 = ''
        for j in range(n):
            index = j, i
            try:
                str1 = str1 + str(scoreMat[index]) + " "

            except:
                scoreMat[index] = 0
                str1 = str1 + "0 "
        #print str1
    # scoreMat has the key value as x,y and value as the sum of timesteps

    scoreMatKey = []
    scoreMatVal = []
    for key, value in sorted(scoreMat.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        # print "%s: %s" % (key, value)
        scoreMatKey.append(key)
        scoreMatVal.append(value)
    #print scoreMatKey
    #print scoreMatVal
    # print zip(scoreMatVal, scoreMatKey)
    subsum = []
    for i in range(len(scoreMatVal)):
        subsum.append(sum(scoreMatVal[i:i + p]))

    # subsum has the max sum from that index to the end

    sol = []
    nextelement = 0
    finalsol = []
    maxsum = 0
    #print subsum
    while True:
        if p == 1:
            finalsol = [0]
            break
        try:
            if subsum[sol[0]] <= maxsum:
                break
        except:
            pass

        sol.append(nextelement)
        nextelement = nextelement + 1
        while nextelement >= n * n:
            nextelement = sol.pop() + 1

        if len(sol) == p:

            currsum = sum([scoreMatVal[x] for x in sol])
            # print sol
            if maxsum < currsum:
                maxsum = currsum
                finalsol = list(sol)
            nextelement = sol.pop() + 1
            while nextelement >= n * n:
                nextelement = sol.pop() + 1

        while (conflict(nextelement)):
            nextelement = nextelement + 1
            while nextelement >= n * n:
                nextelement = sol.pop() + 1

    #print finalsol

    #print [scoreMatKey[x] for x in finalsol]
    #print sum([scoreMatVal[x] for x in finalsol])
    #print [scoreMatVal[x] for x in finalsol]
    f = open("output.txt","w")
    string = str(sum([scoreMatVal[x] for x in finalsol]))
    f.write(string)
    f.close()

if __name__ == '__main__':
    main()
