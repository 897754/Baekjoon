import sys

class Node:
    def __init__(self, value, x, y) -> None:
        self.value = value
        self.x = x
        self.y = y
        self.dp = 0
    def CheckNext(self):
        if self.x + self.value < N:
            target:Node = nodes[self.x + self.value][self.y]
            target.dp += self.dp
        if self.y + self.value < N:
            target:Node = nodes[self.x][self.y + self.value]
            target.dp += self.dp


N = int(sys.stdin.readline())

nodes = [[None]*N for _ in range(N)]

points = []
for i in range(N):
    input =sys.stdin.readline().split()
    for j in range(N):
        nodes[i][j] = Node(int(input[j]), i, j)


nodes[0][0].dp = 1

for i in range(N):
    for j in range(N):
        cur = nodes[i][j]
        if cur.value == 0:
            continue
        cur.CheckNext()



print(nodes[N-1][N-1].dp)