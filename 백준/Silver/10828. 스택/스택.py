import sys


class Stack:
    def __init__(self) -> None:
        self.arr = []

    arr = []
    def Execute(self, op, value = 0):
        if op == "push":
            self.push(value)
        elif op == "top":
            self.top()
        elif op == "size":
            self.size()
        elif op == "empty":
            self.empty()
        elif op == "pop":
            self.pop()

    def push(self, value):
        self.arr.append(value)
        return
    def top(self):
        if len(self.arr) == 0:
            print("-1")
            return -1
        print(self.arr[len(self.arr)-1])
        return self.arr[len(self.arr)-1]
    def size(self):
        print(len(self.arr))
        return len(self.arr)
    def empty(self):
        if len(self.arr) > 0:
            print("0")
        else:
            print("1")
        return
    def pop(self):
        if len(self.arr) == 0:
            print("-1")
            return -1
        ret = self.top()
        del self.arr[len(self.arr)-1]
        return ret


# N : 전체 크기
N = int(sys.stdin.readline())

s = Stack()
for i in range(N):
    input = sys.stdin.readline().split()
    if len(input) == 2:
        s.Execute(input[0], int(input[1]))
    else:
        s.Execute(input[0])
