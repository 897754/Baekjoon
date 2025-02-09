import sys


class point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    x,y = map(int, input().split())
    arr.append(point(x,y))

arr.sort(key=lambda a:a.x)
arr.sort(key=lambda a:a.y)

for i in arr:
    print(f"{i.x} {i.y}")