import sys
input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])

arr = [N]
for i in range(N-1):
    arr.append(i+1)

print("<", end="")
index = 0
l = len(arr)
while l:
    index = (index + K)%l
    print(arr[index], end="")
    del arr[index]
    l = len(arr)
    if l:
        print(", ", end="")
        index-=1
print(">")