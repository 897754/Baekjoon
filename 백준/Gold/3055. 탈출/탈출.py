import sys
from collections import deque
class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.visited = 0
    def addAdj(self, node):
        if node in self.adj:
            return
        self.adj.append(node)



def BFS(cur:Node):
    deq = deque()
    watQ = deque()
    depth = 0
    cur.visited = 1

    deq.append(cur)
    watQ.extend(waters)

    while len(deq):
        qSize = len(deq)
        # 뎁스 오를때마다 물 한칸씩 퍼트리기
        for _ in range(qSize):
            cur = deq.popleft()
            if cur == end:
                return depth
            if cur.value == '*':
                continue
            #print(cur.value, end=" ")
            for i in cur.adj:
                if i.visited == 0:
                    deq.append(i)
                    i.visited = 1
        wqSize = len(watQ)
        for _ in range(wqSize):
            curW = watQ.popleft()
            for i in curW.adj:
                if i.value == "X":
                    continue
                if i.value == ".":
                    i.value = "*"
                    watQ.append(i)
        depth+=1
    return -1

def indexToID(i,j):
    return i*C+j

def setAdjNodes(x,y):
    curNode:Node = nodes[indexToID(x,y)]
    
    curX = x+1
    curY = y
    if curX < R and indexToID(curX, curY) in nodes and nodes[indexToID(curX,curY)].value != "X":
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    curX = x
    curY = y+1
    if curY < C and indexToID(curX, curY) in nodes and nodes[indexToID(curX,curY)].value != "X":
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)

# R C 입력
input = sys.stdin.readline().split()
R = int(input[0])
C = int(input[1])

start = None
end = None
waters = []
# 맵 입력 
nodes = {}
for r in range(R):
    input = sys.stdin.readline().replace("\n","")
    for c in range(C):
        n = Node(input[c])
        nodes[indexToID(r,c)] = n
        if n.value == "D":
            end = n
        elif n.value == "S":
            start = n
        elif n.value == "*":
            waters.append(n)

# 인접 노드 배열 초기화
for r in range(R):
    for c in range(C):
        if nodes[indexToID(r,c)].value != 'X':
            setAdjNodes(r,c)




# 로직 구현
result = BFS(start)

if result == -1:
    print("KAKTUS")
else:
    print(result)