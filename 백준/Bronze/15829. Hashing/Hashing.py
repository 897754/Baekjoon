import sys

r = 31
M = 1234567891
def Hash(l, s):
    result = 0
    for i in range(l):
        cur = (ord(s[i]) - ord("a") + 1)
        result += (cur * (r ** i))
    return (result % M)

    

input = sys.stdin.readline


l = int(input())
s = input().rstrip()

print(Hash(l,s))