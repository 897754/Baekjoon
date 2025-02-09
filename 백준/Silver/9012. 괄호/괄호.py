import sys


input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    s = input().rstrip()
    flag = True
    for c in s:
        if (c == "("):
            stack.append(c)
        elif (c == ")"):
            if(len(stack) == 0 or stack.pop() != "("):
                flag = False
                break
    if flag == False or len(stack)>0:
        print("NO")
    else:
        print("YES")
