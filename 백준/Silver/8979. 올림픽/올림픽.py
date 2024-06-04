# 8979번 올림픽
# 입력 ----------------------------------------------------------------
n, k = map(int, input().split())
infos = []
for _ in range(n):
    data = input().split()
    infos.append([int(data[0]), tuple(map(int, data[1:]))])

# 풀이 ----------------------------------------------------------------
# 국가 K 정보 찾기
infoK = []
for info in infos:
    if info[0] == k:
        infoK = info

# 국가번호 제거해서 메달정보 튜플만 남기기
infos = list(set(map(lambda x:x[1], infos)))
infoK = infoK[1]

# 중복제거 & 정렬
infos = sorted(infos, key=lambda x:(x[0],x[1],x[2]), reverse=True)
rate = infos.index(infoK) + 1

# 출력 ----------------------------------------------------------------
print(rate)