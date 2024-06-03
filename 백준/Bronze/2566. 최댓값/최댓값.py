def findMax(a):
    max = 0
    n, m = 0, 0
    for i in range(9):
        for j in range(9):
            if a[i][j] > max:
                max = a[i][j]
                n, m = i, j
    return [max, n, m]

a = []
for _ in range(9):
    a.append(list(map(int, input().split())))
    
b = findMax(a)
print(b[0])
print(f'{b[1]+1} {b[2]+1}')