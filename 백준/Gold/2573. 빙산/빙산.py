import sys

sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, value) -> None:
        self.adjNodes = []
        self.value = value
        self.visited = False
    def addAdj(self, target):
        # if value in self.adj:
        #     return
        self.adjNodes.append(target)
    def Reduce(self):
        l = len(self.adjNodes)
        self.value -= (4-l)
    def ZeroCheck(self, index):
        if self.value > 0:
            return
        while len(self.adjNodes) > 0:
            targetNode = self.adjNodes[0]
            targetNode.adjNodes.remove(self)
            self.adjNodes.remove(targetNode)
        del nodes[index]
        

        
def DFS(cur:Node):
    cur.visited = 1
    for i in cur.adjNodes:
        if i.visited == 0:
            DFS(i)
    


input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])


def indexToID(i,j):
    return i*M+j

def setAdjNodes(x,y):
    curNode:Node = nodes[indexToID(x,y)]
    
    curX = x
    curY = y+1
    if indexToID(curX, curY) in nodes:
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)
    curX = x+1
    curY = y
    if indexToID(curX, curY) in nodes:
        targetNode:Node = nodes[indexToID(curX,curY)]
        curNode.addAdj(targetNode)
        targetNode.addAdj(curNode)

# 정점 배열 초기화
nodes = {}
inputArr = [[0]*M for _ in range(N)]
for node in range(N):
    input = sys.stdin.readline().split()
    for j in range(M):
        inputArr[node][j] = int(input[j])
        if inputArr[node][j] != 0:
            nodes[indexToID(node,j)] = Node(inputArr[node][j])

# 인접 노드 배열 초기화
for node in range(N):
    for j in range(M):
        if inputArr[node][j] != 0:
            setAdjNodes(node,j)
count = 0
flag = True
# Reduce 시작
while flag:
    if len(nodes) == 0:
        print("0")
        break
    # 섬 2개 이상인지 체크
    for node in nodes.values():
        node.visited = False
    DFS(list(nodes.values())[0])
    for node in nodes.values():
        if not node.visited:
            print(count)
            flag = False
            break
    if not flag:
        break
    
    

    # 녹이기
    for node in nodes.values():
        node.Reduce()
    # 다 녹은거 제거
    keys = list(nodes.keys())
    for node in keys:
        curNode:Node = nodes[node]
        curNode.ZeroCheck(node)
    
    count += 1
    #print(f"count = {count}")


