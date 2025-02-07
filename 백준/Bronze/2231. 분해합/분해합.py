import sys

def Calc(n):
    s = str(n)
    sum = n
    for i in s:
        sum += int(i)
    return sum


N = int(sys.stdin.readline())
flag = True
for i in range(N):
    if Calc(i) == N:
        print(i)
        flag = False
        break

if(flag):
    print(0)