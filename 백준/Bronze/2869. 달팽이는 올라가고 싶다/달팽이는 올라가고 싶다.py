import sys

input = (sys.stdin.readline()).split()

a = int(input[0])
b = int(input[1])
v = int(input[2])

if a>=v:
    print(1)
else:
    v = v-a
    a = a-b
    result = v//a+1
    if v % a != 0:
        result+=1
    print(result)
