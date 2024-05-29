
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
lastDates = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']

totDays = 0
for idx, date in enumerate(lastDates):
    month = idx+1

    # (idx+1)월의 일 수 더하기
    if x != month:
        totDays += date
        continue
    # y 일 더하기
    else:
        totDays += y
        break

# 요일 구하기
dayNum = totDays % 7
print(days[dayNum-1])