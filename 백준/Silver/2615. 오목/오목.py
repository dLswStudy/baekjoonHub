baduk = [list(map(int, input().split())) for _ in range(19)]

dolsB, dolsW = [], []
linesB, linesW = [], []
lineDol5 = []

for i, line in enumerate(baduk):
    for j, dol in enumerate(line):
        if dol == 1:
            dolsB.append((i, j))
        elif dol == 2:
            dolsW.append((i, j))

def isWin(isBorW):
    global lineDol5
    global dolsB
    global dolsW
    global linesB
    global linesW
    dols = dolsB if isBorW == 'B' else dolsW
    lines = linesB if isBorW == 'B' else linesW
    way1 = (1, -1)
    way2 = (1,  0) 
    way3 = (1,  1) 
    way4 = (0,  1) 
    ways = [way1, way2, way3, way4]

    for dol in dols:
        dol1 = (dol[0], dol[1])
        for wayIdx, way in enumerate(ways):
            dol2 = (dol[0]+way[0], dol[1]+way[1])
            isExist = False
            for line in lines:
                isExist = (
                        dol2 in dols
                           and
                        dol1 in line
                           and
                        dol2 in line
                )
                if isExist:
                    break

            if isExist:
                continue
            else:
                line = [dol1]
                n = 2
                i = dol1[0]
                j = dol1[1]
                while 0 <= i < 19 and 0 <= j < 19 and 2 <= n:
                    i = dol1[0] + (n - 1) * way[0]
                    j = dol1[1] + (n - 1) * way[1]
                    doln = (i, j)
                    if doln in dols:
                        line.append(doln)
                        n += 1
                    else:
                        n = -1
                if len(line) >= 2:
                    lines.append(line)
                if len(line) == 5:
                    lineDol5 = line
                    return True
    return False

isWinB = isWin('B')
isWinW = isWin('W')

sortedLine = sorted(lineDol5, key=lambda x: (x[1], x[0]))
print(1 if isWinB else (2 if isWinW else 0))
if isWinB or isWinW:
    print(f'{sortedLine[0][0]+1} {sortedLine[0][1]+1}')


