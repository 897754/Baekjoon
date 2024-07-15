import sys
from collections import deque

class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.visited = 0
    def addAdj(self, node):
        if node in self.adj:
            return
        self.adj.append(node)

def DFS(cur:Node):
    cur.visited = 1
    print(cur.value, end=" ")
    for i in cur.adj:
        if i.visited == 0:
            DFS(i)
    

def BFS(cur:Node):
    cur.visited = 1
    deq.append(cur)
    while len(deq):
        cur = deq.popleft()
        print(cur.value, end=" ")
        for i in cur.adj:
            if i.visited == 0:
                deq.append(i)
                i.visited = 1
        
input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])
V = int(input[2])

deq = deque()
# 정점 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))


# 간선 배열 초기화
for i in range(M):
    input = sys.stdin.readline().split()
    a = nodes[int(input[0])]
    b = nodes[int(input[1])]
    a.addAdj(b)
    b.addAdj(a)

# 로직 구현
for i in range(N):
    nodes[i+1].adj.sort(key=lambda x:x.value)

DFS(nodes[V])
print()
for i in range(N):
    nodes[i+1].visited = 0
    
BFS(nodes[V])