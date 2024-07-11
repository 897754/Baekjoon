import sys

# N : 전체 크기
N = int(sys.stdin.readline())
count = 0

def Calc(n):
    global count
    count += 1

    newN = n
    if n < 10:
        newN *= 10
    newVal = (newN//10) + (newN%10)
    n = (n%10)*10 + (newVal % 10)

    if N == n:
        return
    Calc(n)


Calc(N)

print(count)