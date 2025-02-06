import sys

input = sys.stdin.readline

arr = input().split()

result = 0
for i in range(5):
    result += (int(arr[i])**2)

print(result%10)