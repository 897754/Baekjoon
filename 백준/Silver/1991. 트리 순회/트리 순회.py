import sys

def AToC(A):
    return chr(A+65)
def CToA(C):
    return ord(C)-65

class Node:
    def __init__(self, value) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
    
class Tree:
    def __init__(self, N) -> None:
        self.arr = []
        for i in range(N):
            self.arr.append(Node(AToC(i)))
        self.first = self.arr[0]

    def setTree(self, s):
        inputs = s.split()
        cur = self.getNode(inputs[0])
        left = self.getNode(inputs[1])
        right = self.getNode(inputs[2])
        cur.left = left
        cur.right = right
    def getNode(self, c):
        if c == '.':
            return None
        return self.arr[CToA(c)]
    
    def Fsearch(self, node:Node):
        print(node.value, end="")
        if node.left:
            self.Fsearch(node.left)
        if node.right:
            self.Fsearch(node.right)
    def Msearch(self, node:Node):
        if node.left:
            self.Msearch(node.left)
        print(node.value, end="")
        if node.right:
            self.Msearch(node.right)
    def Bsearch(self, node:Node):
        if node.left:
            self.Bsearch(node.left)
        if node.right:
            self.Bsearch(node.right)
        print(node.value, end="")

N = int(sys.stdin.readline())
t = Tree(N)
for i in range(N):
    input = sys.stdin.readline()
    t.setTree(input)

t.Fsearch(t.first)
print("")
t.Msearch(t.first)
print("")
t.Bsearch(t.first)