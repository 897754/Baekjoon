import sys

input = sys.stdin.readline
N, M = map(int, input().split())

m = min(N,M)
while(True):
    if(N%m == 0 and M%m == 0):
        break
    m-=1
print(m)

m = max(N,M)
result = m
while(True):
    if(result%M == 0 and result%N == 0):
        break
    result += m
print(result)