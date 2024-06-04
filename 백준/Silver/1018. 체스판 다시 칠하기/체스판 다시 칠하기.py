N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

boolTypeW = lambda i,j: (((i+j)%2 == 0 and original[i][j] == 'W')
                             or ((i+j)%2 == 1 and original[i][j] == 'B'))
for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if boolTypeW(i,j):
                    index1 += 1
                else:
                    index2 += 1
        count.append(min(index1, index2))

print(min(count))