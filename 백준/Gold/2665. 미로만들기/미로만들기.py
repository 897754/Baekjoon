import sys
import heapq

sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, value, isWhite) -> None:
        self.adj = []
        self.value = value
        self.distance = 9999999999
        self.isWhite = isWhite
    def addAdj(self, target):
        self.adj.append(target)

    def __lt__(self, other):
        return  self.distance < other.distance
         
def indexToID(i,j):
    return i*N+j

def setAdjNodes(x,y):
    curNode:Node = nodes[indexToID(x,y)]
    
    curX = x
    curY = y+1
    if curY < N:
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    curX = x+1
    curY = y
    if curX < N:
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)


def Dijkstra(start:Node):
    q = []
    heapq.heappush(q, start)
    
    q.append(start)
    start.distance = 0
    
    while len(q):
        cur = heapq.heappop(q)
        for n in cur.adj:
            if n.isWhite == '1':
                if n.distance > cur.distance:
                    n.distance = cur.distance
                    heapq.heappush(q, n)
            else:
                if n.distance > cur.distance+1:
                    n.distance = cur.distance+1
                    heapq.heappush(q, n)

# 입력
N = int(sys.stdin.readline())

# 노드 배열 초기화
nodes = []
inputArr = []
for i in range(N):
    input = sys.stdin.readline()
    inputArr.append(input)
    for j in range(N):
        nodes.append(Node(indexToID(i,j), input[j]))

# 인접 노드 배열 초기화
for i in range(N):
    for j in range(N):
        if inputArr[i][j] != 0:
            setAdjNodes(i,j)

# 로직 구현
Dijkstra(nodes[0])

print(nodes[N**2-1].distance)