import sys


input = sys.stdin.readline

while(True):
    stack = []
    s = input().rstrip()
    if(s == '.'):
        break
    flag = True
    for c in s:
        if (c == "("):
            stack.append(c)
        elif (c == "["):
            stack.append(c)
        elif (c == ")"):
            if(len(stack) == 0 or stack.pop() != "("):
                flag = False
                break
        elif (c == "]"):
            if(len(stack) == 0 or stack.pop() != "["):
                flag = False
                break
    if flag == False or len(stack)>0:
        print("no")
    else:
        print("yes")
