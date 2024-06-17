nums = list(map(int, input().split()))
multiple = min(nums)

while True:
    cnt = 0
    for num in nums:
        if multiple % num == 0:
            cnt += 1
    if cnt > 2:
        break
    multiple += 1
print(multiple)
