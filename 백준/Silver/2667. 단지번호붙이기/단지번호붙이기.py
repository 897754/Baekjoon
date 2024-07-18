import sys
import heapq

sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, value) -> None:
        self.adjNodes = []
        self.value = value
        self.visited = False
    def addAdj(self, target):
        self.adjNodes.append(target)

def indexToID(i,j):
    return i*N+j
        
def DFS(cur:Node):
    global curCount
    cur.visited = 1
    curCount += 1
    for i in cur.adjNodes:
        if i.visited == 0:
            DFS(i)
    

def setAdjNodes(x,y):
    curNode:Node = nodes[indexToID(x,y)]
    
    i = indexToID(x, y+1)
    if i in nodes and y+1 < N:
        targetNode:Node = nodes[i]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    i = indexToID(x+1, y)
    if i in nodes and x+1 < N:
        targetNode:Node = nodes[i]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)

N = int(sys.stdin.readline())

nodes = {}
for i in range(N):
    input = sys.stdin.readline().replace("\n","")
    for j in range(N):
        if input[j] == "1":
            nodes[indexToID(i,j)] = Node(int(input[j]))

# 인접 노드 배열 초기화
for i in range(N):
    for j in range(N):
        if indexToID(i,j) in nodes:
            setAdjNodes(i,j)

count = 0
curCount = 0
h = []
nodes = list(nodes.values())
for i in nodes:
    if i.visited:
        continue
    count+=1
    DFS(i)
    heapq.heappush(h, curCount)
    curCount = 0

print(count)
while len(h):
    print(heapq.heappop(h))