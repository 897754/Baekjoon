import sys



# N : 전체 크기
N = int(sys.stdin.readline())

A = []
input = sys.stdin.readline().split()
for i in range(N):
    A.append(int(input[i]))


result = [-1]
stack = [0]
i = 1
j = 0
while i < len(A):
    j = i
    while True:
        j-=1
        top = stack[len(stack)-1]
        if A[top] <= A[i]:
            stack.pop()
            if A[top] == A[i]:
                stack.append(i)
                result.append(top)
                break
        else :
            stack.append(i)
            result.append(top)
            break
        if len(stack) == 0:
            stack.append(i)
            result.append(-1)
            break
    i+=1

for i in result:
    print(i+1, end=" ")