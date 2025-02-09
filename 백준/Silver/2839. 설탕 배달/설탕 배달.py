import sys


input = sys.stdin.readline

N = int(input())

f = N//5
t = 0
flag = False
while (f >= 0):
    while True:
        sum = f*5+t*3
        if(sum >= N):
            if(sum==N):
                flag = True
            break
        t+=1
    if(flag):
        break
    f -= 1
    t = 0

print(f+t)