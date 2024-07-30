import sys

input = (sys.stdin.readline()).split()
W = int(input[0])
H = int(input[1])

N = int(sys.stdin.readline())

dic0 = {}
dic1 = {}

dic0[0] = 0
dic0[H] = 0
dic1[0] = 0
dic1[W] = 0

for _ in range(N):
    input = (sys.stdin.readline()).split()
    a = int(input[0])
    b = int(input[1])
    if a == 0:
        dic0[b]=0
    else:
        dic1[b]=0

max0 = 0
a0 = sorted(list(dic0.keys()))
for i in range(1,len(a0)):
    val = a0[i] - a0[i-1]
    if max0 < val:
        max0 = val
        
max1 = 0
a1 = sorted(list(dic1.keys()))
for i in range(1,len(a1)):
    val = a1[i] - a1[i-1]
    if max1 < val:
        max1 = val
        
print(max0*max1)