import sys
from collections import deque

sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.visited = 0
        self.depth = 0
      
def BFS(cur:Node):
    cur.visited = 1
    deq.append(cur)
    while True:
        if len(deq) == 0:
            return
        if deq[0].depth == K:
            return
        cur = deq.popleft()
        for i in cur.adj:
            if i.visited == 0:
                deq.append(i)
                i.visited = 1
                i.depth = cur.depth+1

# 입력
input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])
K = int(input[2])
X = int(input[3])

deq = deque()
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))
for _ in range(M):
    input = sys.stdin.readline().split()
    a = nodes[int(input[0])]
    b = nodes[int(input[1])]
    if not (b in a.adj):
        a.adj.append(b)

# 로직 구현
BFS(nodes[X])

if len(deq):
    for i in sorted(deq, key=lambda x:x.value):
        print(i.value)
else:
    print(-1)