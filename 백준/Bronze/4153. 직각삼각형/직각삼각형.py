import sys

input = sys.stdin.readline

while(True):
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    
    sum = a+b+c
    C = max(a,b,c)
    A = min(a,b,c)
    B = sum - C - A

    if(A**2 + B**2 == C**2):
        print("right")
    else:
        print("wrong")