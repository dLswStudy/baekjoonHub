from collections import defaultdict

T = int(input())
testCases = [(int(input()),int(input())) for _ in range(T)]

memo = defaultdict(lambda: defaultdict(int))
def dp(a, b):
    if memo[a][b]:
        return memo[a][b]
    else:
        if b == 0:
            return 0
        elif a == 0:
            memo[a][b] = b
            return b
        else:
            memo[a][b] = dp(a, b-1) + dp(a-1, b)
            return dp(a, b-1) + dp(a-1, b)

for tc in testCases:
    print(dp(*tc))