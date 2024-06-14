n = int(input())
stores = list(map(int, input().split()))
milk = [0,1,2]

cnt = 0
for i in range(n):
    if stores[i] == milk[(cnt+3) % 3]:
        cnt += 1

print(cnt)