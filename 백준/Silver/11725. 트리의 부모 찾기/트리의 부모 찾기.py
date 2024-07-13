import sys

sys.setrecursionlimit(10**8)
class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.parent = None
    def addAdj(self, value):
        # if value in self.adj:
        #     return
        self.adj.append(value)

N = int(sys.stdin.readline())

visited = [0]*(N+1)
# 정점 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))
visited[0] = 1

def DFS(cur:Node):
    global count
    visited[cur.value] = 1

    #count+=1
    #print(cur.value, end=" ")

    for i in cur.adj:
        if visited[i] == 0:
            nodes[i].parent = cur
            DFS(nodes[i])
    

# 간선 배열 초기화
for i in range(N-1):
    input = sys.stdin.readline().split()
    nodes[int(input[0])].addAdj(int(input[1]))
    nodes[int(input[1])].addAdj(int(input[0]))

nodes[1].parent = nodes[1]
DFS(nodes[1])

for i in range(N-1):
    print(nodes[i+2].parent.value)