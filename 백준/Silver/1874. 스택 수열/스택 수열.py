import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    cur = int(input())
    arr.append(cur)

flag = True
stack = []
cur = 1
result = ""
for i in range(n):
    target = arr[i]
    while(cur <= target):
        result += "+\n"
        stack.append(cur)
        cur+=1
    if(len(stack) == 0 or stack[-1] != target):
        flag = False
        break
    result += "-\n"
    stack.pop()

if(flag):
    print(result)
else:
    print("NO")