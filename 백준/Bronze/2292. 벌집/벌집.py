import sys


N = int(sys.stdin.readline())

gap = 0
sum = 1
i = 1
while(True):
    if(sum >= N):
        break
    gap += 6
    sum += gap
    i += 1

print(i)