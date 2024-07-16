import sys
from collections import deque 


def Calc(arr):
    sum = 0
    for i in range(N):
        sum += arr[i] * costs[i]
    # -1 : 이미 탐색된 배열
    if sum in visited:
        return -1
    visited[sum] = None
    # 1 : 정답 탐색 완료
    if sum == K:
        return 1
    # 0 : 계속 탐색
    return 0
        

visited = {}
def Search():
    #함수 최초 실행 시
    q = deque()
    arr = [0]*N
    depth = 0
    q.append(tuple(arr))
    while True:
        qSize = len(q)

        depth += 1
        if depth * costs[0] > K:
            break
        for _ in range(qSize):
            arr = list(q.popleft())

            arr[0] += 1
            c = Calc(arr)
            if c == 1:
                print(depth)
                return
            elif c == 0:
                q.append(tuple(arr))
            for i in range(N-1):
                arr[i]-=1
                arr[i+1]+=1
                c = Calc(arr)
                if c == 1:
                    print(depth)
                    return
                elif c == 0:
                    q.append(tuple(arr))
    print(-1)


# N K 입력
input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])
flag = False
costs = {}
for node in range(N):
    input = int(sys.stdin.readline())
    if input == K:
        print("1")
        flag = True
        break
    if not(input in costs) and input < K:
        costs[input] = 0

costs = sorted(list(costs.keys()))
N = len(costs)

if not flag:
    Search()