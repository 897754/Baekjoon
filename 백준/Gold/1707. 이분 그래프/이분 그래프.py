import sys

sys.setrecursionlimit(10**8)
class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
        self.parent = None
    def addAdj(self, value):
        # if value in self.adj:
        #     return
        self.adj.append(value)


def DFS(cur:Node):
    global count

    #count+=1
    #print(cur.value, end=" ")

    for i in cur.adj:
        if color[i] == 0:
            color[i] = color[cur.value]*-1
            if not DFS(nodes[i]):
                return False
        # 인접한 노드의 색이 같으면
        elif color[i] == color[cur.value]:
            return False
    return True
    

K = int(sys.stdin.readline())
for i in range(K):
    input = sys.stdin.readline().split()
    V = int(input[0])
    E = int(input[1])

    color = [0]*(V+1)
    # 정점 배열 초기화
    nodes = [None]
    for i in range(V):
        nodes.append(Node(i+1))

    #color[0] = 1


    # 간선 배열 초기화
    for i in range(E):
        input = sys.stdin.readline().split()
        nodes[int(input[0])].addAdj(int(input[1]))
        nodes[int(input[1])].addAdj(int(input[0]))

    flag = True
    for i in range(V):
        if color[i+1] == 0:
            color[i+1] = 1
            if not DFS(nodes[i+1]):
                flag = False
            
    if flag:
        print("YES")
    else:
        print("NO")
