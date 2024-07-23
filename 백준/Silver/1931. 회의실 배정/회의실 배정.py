import sys
from typing import List

class Meeting:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    def GetDuration(self):
        return self.end-self.start
    def PrintThis(self):
        print(f"{self.start}-{self.end}")
A = int(sys.stdin.readline())


arr:list[Meeting] = []
for i in range(A):
    input = sys.stdin.readline().split()
    arr.append(Meeting(int(input[0]), int(input[1])))

arr.sort(key= lambda x:(x.end, x.start))


count = 0
curEnd = 0
for a in arr:
    if a.start < curEnd:
        continue
    count +=1
    curEnd = a.end
    

print(count)