from collections import deque
# 입력 ----------------------------------------------------------------
n = int(input())
d = deque()
for _ in range(n):
    d.append(int(input()))


# 풀이 ----------------------------------------------------------------
count = 1
standard = d.pop()
for i in range(n-1):
    see = d.pop()
    if see > standard:
        count += 1
        standard = see

# 출력 ----------------------------------------------------------------
print(count)