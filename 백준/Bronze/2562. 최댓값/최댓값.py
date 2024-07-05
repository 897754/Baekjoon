n = []
for a in range(9):
    n.append(int(input()))

maxIndex = 0
for a in range(9):
    if n[maxIndex] < n[a]:
        maxIndex = a
print(n[maxIndex])
print(maxIndex+1)