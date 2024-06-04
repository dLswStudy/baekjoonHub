n = int(input())
switches = list(map(int, input().split()))
studentsNum = int(input())
orders = [list(map(int, input().split())) for _ in range(studentsNum)]

def fSwitch(sIdx):
    global switches
    switches[sIdx] = 0 if switches[sIdx] == 1 else 1

for order in orders:
    if order[0] == 1:
        for idx, switch in enumerate(switches):
            if (idx+1)%order[1] == 0:
                fSwitch(idx)
    else:
        midIdx = order[1]-1
        fSwitch(midIdx)

        i = 1
        while (midIdx-i >=0 and midIdx+i <= len(switches)-1
               and switches[midIdx-i] == switches[midIdx+i]):
            fSwitch(midIdx-i)
            fSwitch(midIdx+i)
            i += 1

m = 0
while m <= len(switches)-1:
    print(*switches[0+m:20+m])
    m += 20
