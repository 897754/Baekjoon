import sys
from collections import deque
class Node:
    def __init__(self, value) -> None:
        self.next = []
        self.value = value
        self.accessCount = 0
    def addAdj(self, node):
        if node in self.adj:
            return
        self.adj.append(node)

def Topology():
    q = deque()

    # 진입차수 0인 노드들 전부 큐에 넣기
    for i in range(N):
        n = nodes[i+1]
        if n.accessCount == 0:
            q.append(n)

    while len(q):
        n:Node = q.popleft()
        print(n.value)
        for a in n.next:
            a.accessCount -= 1
            if a.accessCount <= 0:
                q.append(a)

# N M 입력
input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])

# 노드 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))

# 인접 노드 연결
for i in range(M):
    input = sys.stdin.readline().split()
    a = nodes[int(input[0])]
    b = nodes[int(input[1])]
    a.next.append(b)
    b.accessCount += 1

# 로직 구현
Topology()