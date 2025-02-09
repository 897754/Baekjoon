import sys
from collections import deque

q = deque()

def operate(op, value):
    if op == "push":
        q.append(value)
    elif op == "front":
        if(len(q) == 0):
            print("-1")
        else:
            print(q[0])
    elif op == "back":
        if(len(q) == 0):
            print("-1")
        else:
            print(q[-1])
    elif op == "pop":
        if(len(q) == 0):
            print("-1")
        else:
            print(q.popleft())
    elif op == "size":
        print(len(q))
    elif op == "empty":
        print("1" if len(q) == 0 else "0")



input = sys.stdin.readline

N = int(input())

for i in range(N):
    s = input().split()
    if(len(s) > 1):
        operate(s[0], int(s[1]))
    else:
        operate(s[0], 0)