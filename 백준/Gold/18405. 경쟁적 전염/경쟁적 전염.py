import sys
from collections import deque

sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
    def addAdj(self, target):
        self.adj.append(target)

def indexToID(i,j):
    return i*N+j
        

def BFS():
    deq = deque()
    depth = 0
    for i in virus:
        deq.append(i)
    while len(deq):
        qSize = len(deq)
        for i in range(qSize):
            cur = deq.popleft()
            
            for i in cur.adj:
                if i.value == 0:
                    deq.append(i)
                    i.value = cur.value
                    if i == target:
                        return
                    
        depth +=1
        if depth == S:
            return


def setAdjNodes(x,y):
    curNode:Node = nodes[indexToID(x,y)]
    
    i = indexToID(x, y+1)
    if y+1 < N:
        targetNode:Node = nodes[i]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    i = indexToID(x+1, y)
    if x+1 < N:
        targetNode:Node = nodes[i]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)


input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])

# 정점 배열 초기화
virus = []
nodes = {}
for i in range(N):
    input = sys.stdin.readline().split()
    for j in range(N):
        value = int(input[j])
        nodes[indexToID(i,j)] = Node(value)
        # 초기 바이러스 배열에 해당 노드 넣기 
        if value != 0:
            virus.append(nodes[indexToID(i,j)])

virus.sort(key=lambda x:x.value)
input = sys.stdin.readline().split()
S = int(input[0])
X = int(input[1])
Y = int(input[2])

target = nodes[indexToID(X-1,Y-1)]

# 인접 노드 배열 초기화
for i in range(N):
    for j in range(N):
        setAdjNodes(i,j)


if S > 0:
    BFS()

print(target.value)