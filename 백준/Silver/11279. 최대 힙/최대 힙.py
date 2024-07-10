import heapq
import sys

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, item):
        """ 최대 힙에 요소를 추가합니다. """
        heapq.heappush(self.heap, -item)
        
    def pop(self):
        if self.__len__() == 0:
            return 0
        """ 최대 힙에서 최대 값을 제거하고 반환합니다. """
        return -heapq.heappop(self.heap)
        
    def peek(self):
        """ 최대 힙의 최대 값을 반환합니다. """
        return -self.heap[0] if self.heap else None
    
    def __len__(self):
        """ 힙의 크기를 반환합니다. """
        return len(self.heap)
    
    def __str__(self):
        """ 힙의 문자열 표현을 반환합니다. """
        return str([-item for item in self.heap])


h = MaxHeap()
N = int(sys.stdin.readline())
for i in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        val = h.pop()
        print(val)
    else:
        h.push(X)