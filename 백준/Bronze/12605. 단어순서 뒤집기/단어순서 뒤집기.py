n = int(input())
cases = [input().split() for _ in range(n)]

# 풀이 1: [::=1] 사용
for i in range(n):
    print(f"Case #{i+1}: {' '.join(cases[i][::-1])}")