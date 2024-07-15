import sys


#sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, value) -> None:
        self.parents = []
        self.children = []
        self.value = value
        self.visited = False
        self.top = 0
        self.bot = 0
        self.others = 0
        

def DFSTop(cur:Node):
    cur.visited = True
    #print(cur.value, end=" ")
    result = 1
    for i in cur.parents:
        if not i.visited:
            result+=DFSTop(i)
    return result

def DFSBot(cur:Node):
    cur.visited = True
    #print(cur.value, end=" ")
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
    others = N - top - bot
    if top > bot + others:
        #print(f"Top : {node.value} || {top} {bot} {others}")
        count+=1
    elif bot > top + others:
        #print(f"Bot : {node.value} || {bot} {top} {others}")
        count+=1
    for node in nodes:
        node.visited = False
print(count)