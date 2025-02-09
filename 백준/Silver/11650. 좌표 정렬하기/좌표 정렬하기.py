import sys

class point:
    x = 0
    y = 0
    def __init__(self,x, y):
        self.x = x
        self.y = y

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    x,y = map(int, input().split())
    arr.append(point(x,y))

arr.sort(key=lambda x:x.y)
arr.sort(key=lambda x:x.x)

for p in arr:
    print(f"{p.x} {p.y}")