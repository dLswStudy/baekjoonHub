n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
count = []

boolTypeW = lambda i,j: (((i+j)%2 == 0 and matrix[i][j] == 'W')
                             or ((i+j)%2 == 1 and matrix[i][j] == 'B'))
matrix = [
    [('TW' if boolTypeW(i, j) else 'TB') for j in range(m)] 
    for i in range(n)]
for a in range(n-7):
    for b in range(m-7):
        cntTypeW = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if matrix[i][j] == 'TW':
                    cntTypeW += 1
        count.append(min(cntTypeW, 64-cntTypeW))

print(min(count))