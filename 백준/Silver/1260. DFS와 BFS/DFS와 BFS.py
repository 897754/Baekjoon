import sys
from collections import deque

class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
    def addAdj(self, value):
        if value in self.adj:
            return
        self.adj.append(value)

input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])
V = int(input[2])

visited = [0]*(N+1)
deq = deque()
# 정점 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))

def DFS(cur:Node):
    visited[cur.value] = 1
    print(cur.value, end=" ")
    for i in cur.adj:
        if visited[i] == 0:
            DFS(nodes[i])
    

def BFS(cur:Node):
    visited[cur.value] = 1
    deq.append(cur)
    while len(deq):
        cur = deq.popleft()
        print(cur.value, end=" ")
        for i in cur.adj:
            if visited[i] == 0:
                deq.append(nodes[i])
                visited[i] = 1
        

# 간선 배열 초기화
for i in range(M):
    input = sys.stdin.readline().split()
    nodes[int(input[0])].addAdj(int(input[1]))
    nodes[int(input[1])].addAdj(int(input[0]))

for i in range(N):
    nodes[i+1].adj.sort()

DFS(nodes[V])
print()
visited = [0]*(N+1)
BFS(nodes[V])
# 로직 구현