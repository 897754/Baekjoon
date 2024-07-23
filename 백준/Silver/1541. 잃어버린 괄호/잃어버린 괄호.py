import sys

input = sys.stdin.readline().rstrip()


# 로직 구현
newI = input.replace("-", "+")
arr = newI.split("+")

addCount = 0
for i in input:
    if i == "+":
        addCount+=1
    if i == "-":
        break

sum = int(arr[0])
for i in range(1,len(arr)):
    if i-1 < addCount:
        sum += int(arr[i])
    else:
        sum -= int(arr[i])


print(sum)