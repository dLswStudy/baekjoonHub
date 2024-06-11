from collections import deque

n, k = map(int, input().split())

visited = [-1]*(10**5+1)  # time 기록

queue = deque()
time = 0
queue.append((n, time))
while queue:
    current, time = queue.popleft()

    if current == k:
        break

    if visited[current] != -1:
        continue
    visited[current] = time

    time += 1
    nexts = [current*2, current+1, current-1]
    for next in nexts:
        if 0 <= next <= 10**5 and visited[next] == -1:
            queue.append((next, time))

print(time)