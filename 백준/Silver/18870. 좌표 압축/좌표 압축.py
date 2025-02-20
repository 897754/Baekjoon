import sys


input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

sortedArr = sorted(arr)

i = 0
dic = {}
for cur in sortedArr:
    if(dic.__contains__(cur)):
        continue
    dic[cur] = i
    i+=1

for i in range(N):
    print(dic[arr[i]], end=" ")