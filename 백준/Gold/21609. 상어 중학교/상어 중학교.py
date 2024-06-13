from collections import deque

n, color = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
max_groupInfo = (0,0,0,0,[])
_sum = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def spread_add(i, j):
    rainbowCnt = 0
    now_group = []
    rainbows = []
    group_color = board[i][j]
    queue = deque()
    now_group.append((i, j))
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] <= -1 or visited[nx][ny]:
                continue

            next = board[nx][ny]
            if next == group_color or next == 0:
                visited[nx][ny] = True
                now_group.append((nx, ny))
                queue.append((nx, ny))

            if next == 0: # 무지개블록
                rainbows.append((nx,ny))
                rainbowCnt += 1

    # 무지개블록은 방문 다시 해제
    for x,y in rainbows:
        visited[x][y] = False

    return (rainbowCnt, now_group)

def calc_max_group():
    global _sum
    global max_groupInfo
    _sum += max_groupInfo[0] ** 2
    for x, y in max_groupInfo[4]:
        board[x][y] = -9


def clear():
    global visited
    global max_groupInfo
    max_groupInfo = (0,0,0,0,[])
    visited = [[False] * n for _ in range(n)]


def gravity():
    for j in range(n):
        for i in range(n - 2, -1, -1):
            if board[i][j] >= 0:
                nowX = i
                while True:
                    nextX = nowX + 1
                    if nextX <= n - 1 and board[nextX][j] == -9:
                        board[nextX][j] = board[nowX][j]
                        board[nowX][j] = -9
                        nowX = nextX
                    else:
                        break


def rotate():
    global board
    board = list(map(list, zip(*board)))[::-1]

    
existNormal = True
while existNormal:
    existNormal = False
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                rainbowCnt, now_group = spread_add(i, j)
                if len(now_group) >= 2:
                    existNormal = True
                    groupInfo = (len(now_group), rainbowCnt, i, j, now_group[:])
                    nowAndMax = [groupInfo, max_groupInfo]
                    nowAndMax.sort(reverse=True)
                    max_groupInfo = nowAndMax[0]
                    
    if not existNormal:
        break
    calc_max_group()
    clear()
    gravity()
    rotate()
    gravity()


print(_sum)
