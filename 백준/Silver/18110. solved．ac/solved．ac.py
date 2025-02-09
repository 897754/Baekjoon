import sys
import math

def round(n):
    i = math.floor(n)
    if(n-i >= 0.5):
        return math.ceil(n)
    else:
        return i

input = sys.stdin.readline

N = int(input())

cut = round(N / 20 * 3)

arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

sum = 0
for i in range(cut, N - cut):
    sum += arr[i]

if(N == 0):
    print(0)
else:
    print(round(sum/(N-cut-cut)))