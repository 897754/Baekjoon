import sys

# 최소 힙
class MinHeap:
    def __init__(self) -> None:
        self.arr = []

    def left(self):
        if self.__len__() > 0:
            return self.arr[0]
        return 0
    def push(self, x):
        self.arr.append(x)
        index = self.__len__()-1
        
        # 자신의 상위노드가 값이 더 크거나 최상위 노드에 왔을 경우 반복문 종료
        while True:
            if index == 0:
                break
            target = index
            # 짝수
            if target % 2 == 0:
                target -= 2
            # 홀수
            else:
                target -= 1
            
            target = target // 2

            if self.arr[index] > self.arr[target]:
                break

            self.arr[index], self.arr[target] =  self.arr[target], self.arr[index]
            index = target


        return x
    def pop(self):
        if self.__len__() == 0:
            return 0
        result = self.arr[0]
        
        self.arr[0] = self.arr[self.__len__()-1]
        self.downShift(0)
        del self.arr[self.__len__()-1]


        return result
    
    def downShift(self, index):
        # index = 0
        max = index
        # len = 3
        len = self.__len__()
        
        if len-2 < index * 2 + 1:
            return
        if self.arr[max] > self.arr[index*2+1]:
            max = index*2+1
        
        if len-2 >= index * 2 + 2:
            if self.arr[max] > self.arr[index*2+2]:
                max = index*2+2

        if index == max:
            return
        self.arr[index], self.arr[max] = self.arr[max], self.arr[index]
        self.downShift(max)
    def __len__(self):
        return len(self.arr)
    

arr = []
# 입력
N = int(sys.stdin.readline())

# 사람들 입력
for i in range(N):
    X = sys.stdin.readline().split()
    a, b = int(X[0]), int(X[1])
    if a > b:
        tup = (b, a)
    else:
        tup = (a, b)
    arr.append(tup)

# 설치할 철로의 길이
D = int(sys.stdin.readline())

# ==========================입    력==========================
# ==========================로직 구현==========================



arr.sort(key=lambda x: (x[1], x[0]))

# print(arr)

max = 0
d = MinHeap()
for a in arr:
    d.push(a[0])
    while d.__len__() and d.left() < a[1] - D:
        d.pop()
    if max < len(d):
        max = len(d)

print(max)

