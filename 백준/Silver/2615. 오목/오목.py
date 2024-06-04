# 입력 ----
baduk = [list(map(int, input().split())) for _ in range(19)]

# 풀이 ----
dolsB, dolsW = [], []
linesB, linesW = [], []
lineDol5 = []

# dolB, dolW 생성
for i, line in enumerate(baduk):
    for j, dol in enumerate(line):
        if dol == 1:
            # 튜플은 원소에 불변성 이 있어서 채택
            dolsB.append((i, j))
        elif dol == 2:
            dolsW.append((i, j))

# 4 가지 방향 루프
# 방향별로 첫번째, 두번째 돌 조합이 lines에 있는지 체크
#   있으면 다음 방향 진행
#   없으면 라인 만들기 진행
# 방향1 i+1, j-1
# 방향2 i+1, j
# 방향3 i+1, j+1
# 방향4 i, j+1

def isWin(isBorW):
    global lineDol5
    global dolsB
    global dolsW
    global linesB
    global linesW
    dols = dolsB if isBorW == 'B' else dolsW
    lines = linesB if isBorW == 'B' else linesW
    way1 = (1, -1) # 방향1
    way2 = (1,  0) # 방향2
    way3 = (1,  1) # 방향3
    way4 = (0,  1) # 방향4
    ways = [way1, way2, way3, way4]

    # print('dols', dols)
    for dol in dols:
        dol1 = (dol[0], dol[1])
        # print(' dol1', dol1)
        for wayIdx, way in enumerate(ways):
            # print('     방향',wayIdx+1)
            dol2 = (dol[0]+way[0], dol[1]+way[1])
            # 두 조합이 있는 라인이 있는지 체크
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

            # 다음 방향 진행
            if isExist:
                # print('         다음 방향 진행')
                continue
            # 라인 만들기
            else:
                # print('         라인 프로세스')
                line = [dol1]
                n = 2
                i = dol1[0]
                j = dol1[1]
                while 0 <= i < 19 and 0 <= j < 19 and 2 <= n:
                    i = dol1[0] + (n - 1) * way[0]
                    j = dol1[1] + (n - 1) * way[1]
                    doln = (i, j)
                    if doln in dols:
                        # print('             라인 생성, 돌 추가:', doln)
                        line.append(doln)
                        n += 1
                    else:
                        n = -1
                if len(line) >= 2:
                    lines.append(line)
                    # print('         line:',line)
                if len(line) == 5:
                    lineDol5 = line
                    # print('win! line:',lineDol5)
                    return True
    return False

# 출력 ----
isWinB = isWin('B')
isWinW = isWin('W')

sortedLine = sorted(lineDol5, key=lambda x: (x[1], x[0]))
print(1 if isWinB else (2 if isWinW else 0))
if isWinB or isWinW:
    # print(*sortedLine[0])
    print(f'{sortedLine[0][0]+1} {sortedLine[0][1]+1}')


