import sys
sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, value) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
    
class Tree:
    def __init__(self) -> None:
        self.first = None
    def push(self, value):
        N = Node(value)

        # 트리에 노드가 없을 경우 최상단에 넣는다.
        if self.first == None:
            self.first = N
            return
        

        parent = None
        cur = self.first
        while True:
            parent = cur
            if cur.value < value:
                cur = cur.right
                if cur == None:
                    parent.right = N
                    return

            else:
                cur = cur.left
                if cur == None:
                    parent.left = N
                    return
        
    def Bsearch(self, node:Node):
        if node.left:
            self.Bsearch(node.left)
        if node.right:
            self.Bsearch(node.right)
        print(node.value)



t = Tree()


# N = int(sys.stdin.readline())
# for i in range(N):
#     input = sys.stdin.readline()
#     t.push(int(input))


while True:
    try:
        input = sys.stdin.readline()
        t.push(int(input))
    except:
        break



t.Bsearch(t.first)