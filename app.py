import sys


class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.visited = 0
       

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
        

sys.setrecursionlimit(10**8)

input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])

nodes = [None]
for i in range(N):
    nodes.append(Node(i))

for i in range(M):
    input = sys.stdin.readline()

for i in range(N):
    print(nodes[i+1].depth)