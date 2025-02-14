import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h = deque()
    N, M = map(int, input().split())
    pri = input().split()
    
    for i in range(N):
        h.append((int(pri[i]), i))

    i = 1
    while(len(h)>0):
        cur = h.popleft()
        flag = True
        for j in h:
            if(j[0] > cur[0]):
                flag = False
                h.append(cur)
                break
        if(flag):
            if(cur[1] == M):
                print(i)
                break
            i += 1

