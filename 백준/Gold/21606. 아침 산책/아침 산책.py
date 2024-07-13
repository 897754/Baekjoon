import sys

sys.setrecursionlimit(10**8)
class Node:
    def __init__(self, index, value, isInside) -> None:
        self.adj = []
        self.index = index
        self.value = value
        self.isInside = isInside
    def addAdj(self, value):
        # if value in self.adj:
        #     return
        self.adj.append(value)


count = 0
def DFS(cur:Node, parent:Node = None):
    global count
    visited[cur.index] = True
    for i in cur.adj:
        if visited[i]:
            continue
        DFS(nodes[i], cur)
    # 부모가 실내일때
    if parent == None:
        #count  += 1
        return

    elif parent.isInside:
        if cur.isInside:
            count += cur.value
        else:
            count += (cur.value + 1)*cur.value//2
    else:
        parent.value += cur.value

            
N = int(sys.stdin.readline())

#실내 여부 입력
isInside = sys.stdin.readline()

# 정점 배열 초기화
nodes = [None]
for i in range(N):
    if isInside[i] == "1":
        nodes.append(Node(i+1, 1, True))
    else:
        nodes.append(Node(i+1, 0, False))

visited = [False]*(N+1)
    

# 간선 배열 초기화
for i in range(N-1):
    input = sys.stdin.readline().split()
    nodes[int(input[0])].addAdj(int(input[1]))
    nodes[int(input[1])].addAdj(int(input[0]))

for i in range(N):
    if nodes[i+1].isInside:
        DFS(nodes[i+1])
        break
print(count*2)