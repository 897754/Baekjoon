import sys
from collections import deque

sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, value) -> None:
        self.adj = {}
        self.value = value
        self.visited = 0
        self.distance = 9999999999
         
def Dijkstra(cur:Node):
    cur.visited = 1
    keys = list(cur.adj.keys())
    keys.sort(key= lambda x:cur.adj[x])
    
    for n in keys:
        if n.distance > cur.distance+cur.adj[n]:
            n.visited = 0
            n.distance = cur.distance+cur.adj[n]
    for n in keys:
        if n.visited == 0:
            Dijkstra(n)

# 입력
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 노드 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))

# 간선 배열 초기화
for _ in range(M):
    input = sys.stdin.readline().split()
    a = nodes[int(input[0])]
    b = nodes[int(input[1])]
    dist = int(input[2])
    
    if b in a.adj and a.adj[b] < dist:
        continue
    a.adj[b] = dist

# 시작, 끝점
input = sys.stdin.readline().split()
start = nodes[int(input[0])]
end = nodes[int(input[1])]

# 로직 구현
start.distance = 0
Dijkstra(start)

print(end.distance)