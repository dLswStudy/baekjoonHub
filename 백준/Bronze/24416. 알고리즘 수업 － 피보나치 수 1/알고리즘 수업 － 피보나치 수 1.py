n = int(input())
fList = [0, 1, 1]
for m in range(3, 41):
    fList.append(fList[m-1] + fList[m-2])
print(fList[n], n-2)