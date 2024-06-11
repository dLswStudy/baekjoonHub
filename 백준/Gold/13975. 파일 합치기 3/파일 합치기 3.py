import heapq
import sys
input = sys.stdin.readline

t = int(input().rstrip())
tests = []
for _ in range(t):
    k = int(input()) # 소설을 구성하는 장의 수  3 ≤ K ≤ 10^6
    volumesQ = list(map(int, input().split())) # 1장부터 K장까지 수록한 파일의 크기 K 개 , volume < 10^4
    heapq.heapify(volumesQ)
    tests.append(volumesQ)

def minCost(volumesQ):
    cost = 0
    while len(volumesQ) >= 2:
        a1 = heapq.heappop(volumesQ)
        a2 = heapq.heappop(volumesQ)
        a1a2 = a1 + a2
        heapq.heappush(volumesQ, a1a2)
        cost += a1a2

    return cost

for volumesQ in tests:
    print(minCost(volumesQ))