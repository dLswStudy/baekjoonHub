n, m = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True) 

rank = 1
target_rank = 0

for i in range(n):
    if i > 0 and (medals[i][1], medals[i][2], medals[i][3]) != (medals[i-1][1], medals[i-1][2], medals[i-1][3]):
        rank = i + 1

    if medals[i][0] == m:
        target_rank = rank
        break

print(target_rank)