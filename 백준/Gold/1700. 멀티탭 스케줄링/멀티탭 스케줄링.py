import sys
from collections import deque 


input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])

input = sys.stdin.readline().split()
arr = []
for i in range(K):
    arr.append(int(input[i]))

# qwer = deque()
# qwer.popleft

#로직 구현
dic = {}
for i in range(K):
    if arr[i] in dic:
        dic[arr[i]].append(i)
    else:
        dic[arr[i]] = deque()
        dic[arr[i]].append(i)

plugs = [0]*N
count = 0
for i in range(K):
    count += 1
    maxCount = 0
    maxIndex = -1
    q = dic[arr[i]]
    for j in range(N):
        if plugs[j] == 0:
            count -= 1
            maxIndex = j
            break
        if plugs[j] == arr[i]:
            count -= 1
            maxIndex = j
            break
        pQ = dic[plugs[j]]
        if len(pQ) == 0:
            maxCount = 1000000
            maxIndex = j
            continue
        if pQ[0] > maxCount:
            maxCount = pQ[0]
            maxIndex = j
    
    plugs[maxIndex] = arr[i]

    q.popleft()
        


print(count)