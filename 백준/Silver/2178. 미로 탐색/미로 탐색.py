import sys
from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.visited = 0
        self.depth = 1
       

def indexToID(i,j):
    return i*M+j
def setAdjNodes(x,y):
    if inputArr[x][y] == '0':
        return
    # print(x,y)
    curNode:Node = nodes[indexToID(x,y)]
    
    curX = x
    curY = y+1
    if curY < M and inputArr[curX][curY] != '0':

        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.adj.append(targetNode)
        targetNode.adj.append(curNode)
    curX = x+1
    curY = y
    if curX < N and inputArr[curX][curY] != '0':
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.adj.append(targetNode)
        targetNode.adj.append(curNode)

count = 0
deq = deque()
def BFS(cur:Node):
    global count
    cur.visited = 1
    count+=1
    deq.append(cur)
    while len(deq):
        cur = deq.popleft()
        if cur.value == targetIndex:
            return
       # print(cur.value, end=" ")
        for i in cur.adj:
            if i.visited == 0:
                deq.append(i)
                i.depth = cur.depth+1
                i.visited = 1
        

# 입력
nm = sys.stdin.readline().split()
N = int(nm[0])
M = int(nm[1])

nodes = {}
inputArr = []
for i in range(N):
    inputArr.append(input())
    for j in range(M):
        if inputArr[i][j] == "0":
            continue
        nodes[indexToID(i,j)] = Node(indexToID(i,j))

targetIndex = indexToID(N-1, M-1)


# 인접 노드 배열 초기화
for node in range(N):
    for j in range(M):
        if inputArr[node][j] != 0:
            setAdjNodes(node,j)

BFS(nodes[0])

print(nodes[indexToID(N-1,M-1)].depth)