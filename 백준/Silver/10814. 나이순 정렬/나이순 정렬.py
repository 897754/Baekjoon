import sys

class person:
    name = ""
    age = 0
    def __init__(self, age, name):
        self.age = age
        self.name = name

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    p = input().split()
    arr.append(person(int(p[0]), p[1]))

arr.sort(key= lambda x:x.age)

for _ in arr:
    print(f"{_.age} {_.name}")