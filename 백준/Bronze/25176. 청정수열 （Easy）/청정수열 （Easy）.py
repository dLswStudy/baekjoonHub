from itertools import permutations
n = int(input())
print(len(list(permutations([i for i in range(n)],n))))