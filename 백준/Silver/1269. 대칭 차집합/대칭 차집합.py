import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()
#교집합 총합 찾기
interSum = 0

a2index = 0
for i in arr1:
    while(arr2[a2index] < i):
        a2index+=1
        if(a2index >= len(arr2)):
            break
    if(a2index >= len(arr2)):
        break
    if(arr2[a2index] == i):
        interSum += 1

sum = N+M-(interSum*2)

print(sum)