import sys


input = sys.stdin.readline

N = int(input())

dic = {}
s = input().split()
for i in range(N):
    if(dic.__contains__(int(s[i]))):
        dic[int(s[i])] += 1
    else:
        dic[int(s[i])] = 1

    
N = int(input())
s = input().split()
for i in range(N):
    if(dic.__contains__(int(s[i]))):
        print(dic[int(s[i])],end=" ")
    else:
        print(0, end=" ")
