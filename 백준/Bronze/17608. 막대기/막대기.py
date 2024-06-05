from collections import deque
# 입력 ----------------------------------------------------------------
n = int(input())
rods = [int(input()) for _ in range(n)]

# 풀이 ----------------------------------------------------------------
d = deque()
count = 0
standard = 0
for i in range(n):
    see = rods[n-1-i]
    if see > standard:
        count += 1
        standard = see

# 출력 ----------------------------------------------------------------
print(count)