import sys


input = sys.stdin.readline

N, M = map(int, input().split())

ItoN = {}
NtoI = {}
for i in range(N):
    cur = input().rstrip()
    ItoN[i+1] = cur
    NtoI[cur] = i+1

for i in range(M):
    cur = input().rstrip()
    if(cur.isdigit()):
        print(ItoN[int(cur)])
    else:
        print(NtoI[cur])