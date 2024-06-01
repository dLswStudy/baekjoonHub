alpha = ['A','B','C','D','E','F','G','H','I'
    ,'J','K','L','M','N','O','P','Q','R'
    ,'S','T','U','V','W','X','Y','Z']

def to10jinsu(jinStr, jinNum):
    global alpha
    jinNum = int(jinNum)
    l = len(jinStr)
    res = 0
    for c in jinStr:
        if c.isdigit():
            _10jin = int(c)
        else:
            _10jin = alpha.index(c) + 10
        res += _10jin * jinNum**(l-1)
        l -= 1
    return res

jinStr, jinNum = input().split()
print(to10jinsu(jinStr, jinNum))