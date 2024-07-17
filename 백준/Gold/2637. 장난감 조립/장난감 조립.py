import sys
from collections import deque
class Node:
    def __init__(self, value) -> None:
        self.next = []
        self.before = []
        self.value = value
        self.count = 0
        self.accessCount = 0
    def addAdj(self, node):
        if node in self.adj:
            return
        self.adj.append(node)

def Topology():
    q = deque()
    result = []
    # 진입차수 0인 노드들 전부 큐에 넣기
    for i in range(N):
        n = nodes[i+1]
        if n.accessCount == 0:
            q.append(n)

    while len(q):
        n:Node = q.popleft()
        result.append(n)
        
        for a in n.next:
            a.accessCount -= 1
            if a.accessCount <= 0:
                q.append(a)
    return result
def Calc():
    result.reverse()
    for n in result:
        for bef in n.before:
            bef[0].count += bef[1] * n.count
        if len(n.before):
            n.count = 0
            


# N M 입력
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 노드 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))
nodes[N].count = 1

# 인접 노드 연결
for i in range(M):
    input = sys.stdin.readline().split()
    a = nodes[int(input[0])]
    b = nodes[int(input[1])]
    b.next.append(a)
    a.before.append((b,int(input[2])))
    a.accessCount += 1

# 로직 구현
result = Topology()
Calc()

for i in range(N):
    node = nodes[i+1]
    if node.count > 0:
        print(f"{node.value} {node.count}")