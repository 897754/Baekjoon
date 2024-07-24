import sys
from typing import List

class NewMan:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


T = int(sys.stdin.readline())

for _ in range(T):


    N = int(sys.stdin.readline())


    arr:List[NewMan] = []
    for i in range(N):
        input = sys.stdin.readline().split()
        arr.append(NewMan(int(input[0]), int(input[1])))

    arr.sort(key=lambda x:x.a)

    count = 1
    max = arr[0].b
    for i in range(N-1):
        if arr[i+1].b > max:
            continue
        count+=1
        max = arr[i+1].b
    print(count)