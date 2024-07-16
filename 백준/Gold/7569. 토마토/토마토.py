import sys
import heapq

#sys.setrecursionlimit(10**8)

inf = 9999999999
max = 0

class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.distance = inf
    def addAdj(self, target):
        self.adj.append(target)

    def __lt__(self, other):
        return  self.distance < other.distance
         
def indexToID(z,y,x):
    return ((z*M*N) + (y*N) + x)

def setAdjNodes(z,y,x):
    curNode:Node = nodes[indexToID(z,y,x)]
    
    curX = x+1
    curY = y
    curZ = z
    if curX < N:
        targetNode:Node = nodes[indexToID(curZ,curY,curX)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    curX = x
    curY = y+1
    curZ = z
    if curY < M:
        targetNode:Node = nodes[indexToID(curZ,curY,curX)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    curX = x
    curY = y
    curZ = z+1
    if curZ < H:
        targetNode:Node = nodes[indexToID(curZ,curY,curX)]
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
            if n.value == 1:
                if n.distance > 0:
                    n.distance = 0
                    heapq.heappush(q, n)
            elif n.value == 0:
                if n.distance > cur.distance+1:
                    n.distance = cur.distance+1
                    heapq.heappush(q, n)

# 입력
input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])
H = int(input[2])

# 노드 배열 초기화
nodes = []
inputArr = []
for i in range(H):
    inputArr.append([])
    for j in range(M):
        input = sys.stdin.readline().split()
        inputArr[i].append([])
        for k in range(N):
            inputArr[i][j].append(int(input[k]))
            nodes.append(Node(int(input[k])))

# 인접 노드 배열 초기화
for i in range(H):
    for j in range(M):
        for k in range(N):
            setAdjNodes(i,j,k)

def main():
    global max
    # 로직 구현
    for i in range(H):
        for j in range(M):
            for k in range(N):
                node = nodes[indexToID(i,j,k)]
                if node.value == 1 and node.distance >= inf:
                    Dijkstra(node)
                    
    for i in range(H):
        for j in range(M):
            for k in range(N):
                node = nodes[indexToID(i,j,k)]
                if node.value == 0:
                    if node.distance >= inf:
                        return -1
                    if max < node.distance:
                        max = node.distance
    return max

print(main())