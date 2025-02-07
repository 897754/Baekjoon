import sys

input = sys.stdin.readline
N, M = map(int, input().split())
inputArr = input().split()
arr = []

for a in inputArr:
    arr.append(int(a))

result = 0

def Search(d, j, sum):
    global result
    if(sum > M): 
        return
    if(d>=3):
        if(sum > result):
            result = sum
        return
    if(result == M):
        return
    for i in range(j+1,N):
        Search(d+1, i, sum + arr[i])

Search(0, -1, 0)
print(result)