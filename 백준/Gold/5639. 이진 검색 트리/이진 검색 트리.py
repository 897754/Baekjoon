import sys
sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
    
class Tree:
    def __init__(self) -> None:
        self.first = None

    def remove(self, value):
        parent = None
        cur = self.first
        while True:
            #삭제할 노드 발견
            if cur.value == value:
                child = None
                flag = False
                #현재 노드의 오른쪽 자식이 없는 경우
                if cur.right == None:
                    child = cur.left
                    flag = True
                #현재 노드의 왼쪽 자식이 없는 경우
                elif cur.left == None:
                    child = cur.right
                    flag = True
                if flag:
                    if parent == None:
                        self.first = child
                        del cur
                        return True
                    if parent.value < cur.value:
                        parent.right = child
                        del cur
                        return True
                    else:
                        parent.left = child
                        del cur
                        return True

                #현재 노드의 자식이 양쪽 다 있는 경우
                #현재 노드보다 작은 값 중 가장 큰 값 찾기
                else:
                    leftParent = cur
                    left = cur.left
                    isLeft = True
                    while left.right != None:
                        leftParent = left
                        left = left.right
                        isLeft = False
                    cur.value = left.value
                    if isLeft:
                        leftParent.left = left.left
                    else:
                        leftParent.right = left.left
                        del left
                    return True


            parent = cur
            if cur.value < value:
                cur = cur.right
                if cur == None:
                    return False

            else:
                cur = cur.left
                if cur == None:
                    parent.left
                    return False


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
        
    def Fsearch(self, node:Node):
        print(node.value)
        if node.left:
            self.Fsearch(node.left)
        if node.right:
            self.Fsearch(node.right)
    def Msearch(self, node:Node):
        if node.left:
            self.Msearch(node.left)
        print(node.value)
        if node.right:
            self.Msearch(node.right)
    def Bsearch(self, node:Node):
        if node.left:
            self.Bsearch(node.left)
        if node.right:
            self.Bsearch(node.right)
        print(node.value)



t = Tree()


N = int(sys.stdin.readline())
for i in range(N):
    input = sys.stdin.readline()
    t.push(int(input))

N = int(sys.stdin.readline())
for i in range(N):
    input = sys.stdin.readline()
    t.remove(int(input))


# while True:
#     try:
#         input = sys.stdin.readline()
#         t.push(int(input))
#     except:
#         break


t.Fsearch(t.first)
print("")
print("")
t.Msearch(t.first)
print("")
print("")
t.Bsearch(t.first)