import sys

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

visited = [0]*(N+1)
# 정점 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))
visited[0] = 1

def DFS(cur:Node):
    visited[cur.value] = 1
   #print(cur.value, end=" ")
    for i in cur.adj:
        if visited[i] == 0:
            DFS(nodes[i])
    

# 간선 배열 초기화
for i in range(M):
    input = sys.stdin.readline().split()
    nodes[int(input[0])].addAdj(int(input[1]))
    nodes[int(input[1])].addAdj(int(input[0]))

count = 0
for i in range(N):
    if visited[i+1] == 0:
        DFS(nodes[i+1])
        count+=1

print(count)
# 로직 구현