import sys
import itertools

def GetSum(arr, ncr):
    sum = 0
    for i in ncr:
        sum += arr[i]
    return sum
# N : 전체 크기
input = sys.stdin.readline().split()
N = int(input[0])
S = int(input[1])



arr = []
input = sys.stdin.readline().split()
for i in range(N):
    arr.append(int(input[i]))


# 로직 구현
count = 0

com = []
for i in range(N):
    com.append(i)
for i in range(1,N+1):
    nCr = itertools.combinations(com, i)
    for j in nCr:
        if GetSum(arr, j) == S:
            count+=1
print(count)