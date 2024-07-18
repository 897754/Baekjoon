import sys

def Fib(n):
    a = 0
    b = 1
    result = 1
    for i in range(n-1):
        result = a+b
        a = b
        b = result
    return result

N = int(sys.stdin.readline())
if N < 2:
    print(N)
else:
    print(Fib(N))