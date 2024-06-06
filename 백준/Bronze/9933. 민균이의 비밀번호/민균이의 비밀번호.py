n = int(input())
words = [input() for _ in range(n)]
hashTable = {}

# ex) word(las)
for word in words:
    if word == word[::-1] or word[::-1] in hashTable:
        midCharIdx = len(word) // 2 # 1
        print(f'{len(word)} {word[midCharIdx]}')
        break
    else:
        hashTable[word] = 1