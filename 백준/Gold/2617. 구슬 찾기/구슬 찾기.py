import sys


#sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, value) -> None:
        self.parents = []
        self.children = []
        self.visited = False
        

def DFSTop(cur:Node):
    cur.visited = True
    
    result = 1
    for i in cur.parents:
        if not i.visited:
            result+=DFSTop(i)
    return result

def DFSBot(cur:Node):
    cur.visited = True

    result = 1
    for i in cur.children:
        if not i.visited:
            result+=DFSBot(i)
    return result

input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])

nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))

# 간선 연결
for i in range(M):
    input = sys.stdin.readline().split()
    a = nodes[int(input[0])]
    b = nodes[int(input[1])]
    a.children.append(b)
    b.parents.append(a)


# 로직 구현
count = 0
del nodes[0]
for node in nodes:
    top =  DFSTop(node)-1
    bot = DFSBot(node)-1
    val = N//2
    if top > val:
        count+=1
    elif bot > val:
        count+=1
    for node in nodes:
        node.visited = False
print(count)