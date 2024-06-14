coins = [500, 100, 50, 10, 5, 1]
toPayMoney = int(input())
handOver = 1000
takeCoinCnt = 0

takeAmount = handOver - toPayMoney
for coin in coins:
    if takeAmount == 0:
        break
    takeCoinCnt += takeAmount // coin
    takeAmount %= coin

print(takeCoinCnt)