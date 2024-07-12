import sys
sys.setrecursionlimit(10**8)


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
for i in range(V):
    input = sys.stdin.readline()
    t.push(int(input))

N = int(sys.stdin.readline())
for i in range(N):
    input = sys.stdin.readline()
    t.remove(int(input))

