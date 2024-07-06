import sys

minCost = -1
minArr = []

def setRoute(costArr, arr, n, curIndex=0):
    if n == curIndex:
        arr[n] = arr[0]
        checkValue(costArr, arr, n)
    for i in range(n):
        if i in arr[0:curIndex]:
            continue
        arr[curIndex] = i
        setRoute(costArr, arr, n, curIndex+1)

def checkValue(costArr, route, n):
    global minCost
    global minArr
    sum = 0
    for i in range(n):
        if costArr[route[i]][route[i+1]] == 0:
            return
        sum += costArr[route[i]][route[i+1]]
    if minCost < 0 or minCost > sum:
        minCost = sum


n = int(sys.stdin.readline())

costArr = []
for i in range(n):
    costArr.append([])
    input = sys.stdin.readline().split()
    for j in range(n):
        costArr[i].append(int(input[j]))




arr = []
for i in range(n+1):
    arr.append(-1)


setRoute(costArr, arr, n)

print(minCost)