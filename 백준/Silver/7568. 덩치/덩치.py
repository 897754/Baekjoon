import sys


class person:
    weight = 0
    height = 0
    rank = 1
    def __init__(self, w, h):
        self.weight = w
        self.height = h

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    w,h = map(int, input().split())
    arr.append(person(w,h))


newArr = sorted(arr, key=lambda x:x.height, reverse=True)
newArr.sort(key=lambda x:x.weight, reverse=True)

for i in newArr:
    for j in newArr:
        if i.weight < j.weight and i.height < j.height:
            i.rank += 1


for i in arr:
    print(i.rank, end=" ")