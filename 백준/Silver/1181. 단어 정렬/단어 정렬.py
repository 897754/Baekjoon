import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(sys.stdin.readline())


arr.sort()
arr.sort(key=len)
i = 0
while i < len(arr)-1:
    if arr[i] == arr[i+1]:
        arr.remove(arr[i])
    else:
        i+=1

for i in arr:
    print(i,end="")