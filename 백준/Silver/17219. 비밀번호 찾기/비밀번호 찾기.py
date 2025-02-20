import sys


input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    i = input().split()
    url = i[0]
    pw = i[1]

    dic[url] = pw

for _ in range(M):
    i = input().rstrip()
    print(dic[i])