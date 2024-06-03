import sys
input = sys.stdin.readline

num = int(input())
room = [list(input().rstrip()) for i in range(num)]

result = [0,0]

for i in range(num):
    garo, sero  = 0,0

    for j in range(num):
        if room[i][j] == '.':
            garo += 1
        else:
            garo = 0

        if garo == 2:
            result[0] += 1

        if room[j][i] == '.':
            sero += 1
        else:
            sero = 0
        if sero == 2:
            result[1] += 1
print(*result)