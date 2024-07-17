import sys
from collections import deque
import heapq

class Node:
    def __init__(self, value) -> None:
        self.next = []
        self.value = value
        self.newValue = 0
        self.accessCount = 0
    def addAdj(self, node):
        heapq.heappush(self.next, node)
    def __lt__(self, other):
        return  self.value > other.value

count = 0
def Topology():
    global count
    q = []
    
    # 진입차수 0인 노드들 전부 큐에 넣기
    for i in range(N-1, -1, -1):
        n = nodes[i]
        if n.accessCount == 0:
            heapq.heappush(q,n)
    if not len(q):
        return False
    
    while len(q):
        qSize = len(q)
        for _ in range(qSize):
            count += 1
            n:Node = heapq.heappop(q)
            result.append(n)
            while len(n.next):
                a = heapq.heappop(n.next)
                a.accessCount -= 1
                if a.accessCount <= 0:
                    heapq.heappush(q,a)

    if count < N:
        return False
    return True

# N M 입력
N = int(sys.stdin.readline())

# 노드 배열 초기화
nodes = []
for i in range(N):
    nodes.append(Node(i))

# 인접 노드 연결
for i in range(N):
    input = sys.stdin.readline()
    for j in range(N):
        if input[j] == "1":
            a = nodes[i]
            b = nodes[j]
            b.addAdj(a)
            a.accessCount += 1

result = []
# 로직 구현
if Topology():
    index = 1
    result.reverse()
    for i in result:
        i.newValue = index
        index += 1
    for i in range(N):
        print(nodes[i].newValue, end=" ")
else:
    print("-1")