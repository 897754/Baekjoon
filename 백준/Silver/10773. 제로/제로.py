import sys


input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    i = int(input())
    if(i == 0):
        arr.pop()
    else:
        arr.append(i)

sum = 0
for i in arr:
    sum += i

print(sum)