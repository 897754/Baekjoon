import sys
#sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, value) -> None:
        self.parent = self
        self.value = value
    def getHead(self):
        cur = self
        while cur != cur.parent:
            cur = cur.parent
        return cur
    




input = sys.stdin.readline().split()
V = int(input[0])
E = int(input[1])

vertexes = []
for i in range(V):
    vertexes.append(Node(i))

edges = []
for i in range(E):
    input = sys.stdin.readline().split()
    edges.append([])
    # 출발
    edges[i].append(int(input[0])-1)
    # 도착
    edges[i].append(int(input[1])-1)
    # 비용
    edges[i].append(int(input[2]))

# 로직 구현
edges.sort(key=lambda x:x[2])


count = 0
for e in edges:
    v0:Node = vertexes[e[0]]
    v1:Node = vertexes[e[1]]
    # 사이클 나옴
    if v0.getHead() == v1.getHead():
        continue
    v1.getHead().parent = v0.getHead()
    count += e[2]

print(count)