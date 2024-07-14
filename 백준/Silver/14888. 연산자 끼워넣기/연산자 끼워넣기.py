import sys

isFirst = True
min = 0
max = 0


N = int(sys.stdin.readline())

arr = []
input = sys.stdin.readline().split()
for i in range(N):
    arr.append(int(input[i]))

input = sys.stdin.readline().split()
counts = {}
index = 0
for i in range(4):
    for j in range(int(input[i])):
        counts[index] = i
        index+=1

#로직 구현
selectedArr = [-1] * (N-1)
def Calc(a, b, op):
    # +
    if op == 0:
        return a+b
    # -
    if op == 1:
        return a-b
    # *
    if op == 2:
        return a*b
    # //
    if op == 3:
        if a < 0:
            if b < 0:
                a *= -1
                b *= -1
                return a//b
            else:
                a *= -1
                return -(a//b)
        elif b < 0:
            b *= -1
            return -(a//b)

        else:
            return a//b
def PrintFunction():
    print(arr[0], end="")
    for i in range(N-1):
        op = counts[selectedArr[i]]
        if op == 0:
            print('+',end="")
        elif op == 1:
            print('-',end="")
        elif op == 2:
            print('*',end="")
        elif op == 3:
            print('/',end="")
        print(arr[i+1],end="")
    print("=",end="")
def CheckResult():
    global isFirst, min, max
    cur = arr[0]
    for i in range(N-1):
        cur = Calc(cur, arr[i+1], counts[selectedArr[i]])
    
    # PrintFunction()
    # print(cur)

    if isFirst:
        min = cur
        max = cur
        isFirst = False
    else:
        if min > cur:
            min = cur
        elif max < cur:
            max = cur

def Search(d = 0):
    if d == N-1:
        CheckResult()
        return
    for i in range(N-1):
        if i in selectedArr[:d]:
            continue
        selectedArr[d] = i
        Search(d+1)
    return

Search()

print(max)
print(min)