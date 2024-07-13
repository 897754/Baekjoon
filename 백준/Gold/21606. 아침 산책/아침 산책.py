import sys

sys.setrecursionlimit(10**8)
class Node:
    def __init__(self, value) -> None:
        self.adj = []
        self.value = value
    def addAdj(self, value):
        # if value in self.adj:
        #     return
        self.adj.append(value)


count = 0
def DFS(cur:Node):
    global count
    visited[cur.value] = 1

    #print(cur.value, end=" ")

    for i in cur.adj:
        if visited[i] != 0:
            continue
        #실내에 도착했을 때 카운트 올리고 리턴
        if isInside[i-1] == '1':
            count+=1
            continue
        else:
            DFS(nodes[i])
    visited[cur.value] = 0

            
N = int(sys.stdin.readline())

#여기 최적화 가능
#실내 여부 입력
isInside = sys.stdin.readline()

visited = [0]*(N+1)
# 정점 배열 초기화
nodes = [None]
for i in range(N):
    nodes.append(Node(i+1))
visited[0] = 1
    

# 간선 배열 초기화
for i in range(N-1):
    input = sys.stdin.readline().split()
    nodes[int(input[0])].addAdj(int(input[1]))
    nodes[int(input[1])].addAdj(int(input[0]))

for i in range(N):
    if isInside[i] == '1':
        DFS(nodes[i+1])
        # for j in range(N):
        #     visited[j+1] = 0

print(count)