N = int(input())
nums = list(map(int, input().split()))
nums = nums[::-1]
dp = [0] * 1001
for num in nums:
    dp[num] = max(dp[:num])+1
print(max(dp))