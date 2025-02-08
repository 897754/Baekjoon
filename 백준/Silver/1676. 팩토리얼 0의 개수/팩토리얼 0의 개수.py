import sys
import math

input = sys.stdin.readline

f = str(math.factorial(int(input())))

for i in range(1, len(f)+1):
    if(f[-i] != '0'):
        print(i-1)
        break