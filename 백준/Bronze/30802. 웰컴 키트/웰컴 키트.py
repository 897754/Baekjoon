import sys

input = sys.stdin.readline

N = int(input())
sizes = input().split()
T,P = map(int, input().split())

sum = 0
for i in sizes:
    if(int(i)!= 0):
        sum+=1
        sum += (int(i)-1)//T


print(sum)
print(N // P, N % P)