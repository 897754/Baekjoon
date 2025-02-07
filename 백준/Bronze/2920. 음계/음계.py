import sys

input = sys.stdin.readline().split()

a = int(input[0])
b = int(input[1])
gap = a-b

if gap==1 or gap==-1:
    for i in range(6):
        a = int(input[i+1])
        b = int(input[i+2])
        if(a-b != gap):
            gap = 0
            break

if(gap == 1):
    print("descending")
elif(gap == -1):
    print("ascending")
else:
    print("mixed")