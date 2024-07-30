import sys
import heapq

N = int(sys.stdin.readline())

d = {}
for _ in range(N):
    val = int(sys.stdin.readline())
    if val in d:
        d[val]+=1
    else:
        d[val] = 1

a = sorted(list(d.keys()))
for i in a:
    for j in range(d[i]):
        print(i)