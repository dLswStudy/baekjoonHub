# 2차례 중 최고점수, 다섯차례 중 상위2개  모두 더한값이 최종점수
import sys
input = sys.stdin.readline

totScores = []
n = int(input())
for _ in range(n):
    scores = list(map(int, input().split()))
    runScores = scores[0:2]
    trickScores = sorted(scores[2:])
    totScores.append(max(runScores)+trickScores[-1]+trickScores[-2])
print(max(totScores))