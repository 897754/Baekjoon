import sys


searched = 0

# 7
# 20 17 15 10
def Calc(A, h):
    global searched
    while searched < len(A):
        if A[searched] > h:
            searched+=1
        else:
            return


# 배열 크기 입력
firstInput = sys.stdin.readline().split()
N = int(firstInput[0])
M = int(firstInput[1])

max = 0

# 배열 크기만큼 자연수 입력
A = []
input = sys.stdin.readline().split()
for i in range(N):
    A.append(int(input[i]))
    if max < A[i]:
        max = A[i]

A.sort(reverse=True)

sum = 0
h = max
while sum < M:
    h -= 1
    Calc(A,h)
    sum += searched

print(h)