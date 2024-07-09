import sys

def PrintStack(stack):
    print("="*5,end="")
    for i in stack:
        print(i,end=" ")
    print("="*5,end="")
    print("")
def IsNum(a):
    return not (a == "(" or a == ")" or a == "[" or a == "]" or a == 0)
def Top(stack):
    if len(stack) == 0:
        return 0
    return stack[len(stack)-1]

# (()[[]])([])
# 2 x (2+3x3)
# 28

isError = False
input = input()

stack = []
for i in input:
    if isError:
        break
    # 괄호 닫는 조건
    if i == ")":
        # "(" 만날때까지 스택 팝
        current = 1
        while True:
            top = Top(stack)
            if top == "(":
                stack.pop()
                current *= 2
                while(IsNum(Top(stack))):
                    current += Top(stack)
                    stack.pop()
                stack.append(current)
                break
            # 잘못된 괄호 입력
            elif top == "[" or len(stack) == 0:
                isError = True
                break
            # 정수
            else:
                stack.pop()
                current *= top
    elif i == "]":
        # "[" 만날때까지 스택 팝
        current = 1
        while True:
            top = Top(stack)
            if top == "[":
                stack.pop()
                current *= 3
                while(IsNum(Top(stack))):
                    current += Top(stack)
                    stack.pop()
                stack.append(current)
                break
            # 잘못된 괄호 입력
            elif top == "(" or len(stack) == 0:
                isError = True
                break
            # 정수
            else:
                stack.pop()
                current *= top
    elif i == "(" or i == "[":
        stack.append(i)
    # print(f"\ninput : {i}")
    # PrintStack(stack)

result = Top(stack)
if isError or not IsNum(result) or len(stack) > 1:
    print(0)
else:
    print(result)