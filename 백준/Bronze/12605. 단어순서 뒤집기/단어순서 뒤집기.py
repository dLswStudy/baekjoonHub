n = int(input())
cases = [input().split() for _ in range(n)]

# 풀이 2: for문 사용
for i in range(n):
    stack = []
    m = len(cases[i])
    for j in range(m):
        stack.append(cases[i][m-1-j])
    print(f"Case #{i+1}: {' '.join(stack)}")