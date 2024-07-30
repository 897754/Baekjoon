import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())


d1 = b%10
d2 = b//10%10
d3 = b//100

r1 = a*d1
r2 = a*d2
r3 = a*d3
print(r1)
print(r2)
print(r3)
print(a*b)
