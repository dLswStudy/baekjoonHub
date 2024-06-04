n, m = map(int, input().split())
matrix = []
count = []

for _ in range(n):
    matrix.append(input())

boolTypeW = lambda i,j: (((i+j)%2 == 0 and matrix[i][j] == 'W')
                             or ((i+j)%2 == 1 and matrix[i][j] == 'B'))
for a in range(n-7):
    for b in range(m-7):
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