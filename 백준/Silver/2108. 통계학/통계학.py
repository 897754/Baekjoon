import sys
import math
import heapq

def round(n):
    i = math.floor(n)
    if(n-i >= 0.5):
        return math.ceil(n)
    else:
        return i

input = sys.stdin.readline

N = int(input())

dic = {}
arr = []
sum = 0
min = 4000
max = -4000
maxCount = 1
for _ in range(N):
    cur = int(input())
    sum += cur
    arr.append(cur)
    if(cur < min):
        min = cur
    if(cur > max):
        max = cur
    if(dic.__contains__(cur)):
        dic[cur] += 1
        if(dic[cur] > maxCount):
            maxCount = dic[cur]
    else:
        dic[cur] = 1


#산술 평균
print(round(sum / N))

#중앙값
arr.sort()
print(arr[N//2])

#최빈값
keys = dic.keys()
h = []
for k in keys:
    if dic[k] == maxCount:
        heapq.heappush(h, k)
if(len(h) == 1):
    print(h[0])
else:
    heapq.heappop(h)
    print(heapq.heappop(h))

#범위
print(max - min)