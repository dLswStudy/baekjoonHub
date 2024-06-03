# 단어 최대 길이 maxLen, 행렬 a (5 * maxLen) -> 세로로 쭉 붙여서 읽은 문자열
def readVertically(maxLen, a):
    res = ''
    for j in range(maxLen):
        vtcLine = ''
        for i in range(5):
            if a[i][j]:
                vtcLine += a[i][j]
            # else:
            #     vtcLine += ''
        res += vtcLine
    return res

# 입력
a = []
maxLen = 0
for _ in range(5):
    l = list(input())
    a.append(l)
    if len(l) > maxLen:
        maxLen = len(l)
for i in range(5):
    lenOfi = len(a[i])
    if lenOfi < maxLen:
        for _ in range(maxLen - lenOfi):
            a[i].append('')

# 출력
print(readVertically(maxLen, a))
