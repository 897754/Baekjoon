import sys

input = sys.stdin.readline

A = input()
B = input()
C = input()

print(int(A)+int(B)-int(C))
print(int(A.strip()+B)-int(C))