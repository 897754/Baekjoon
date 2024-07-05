def sosu(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True

N = int(input())
arr = []
s = input().split(' ')
for i in s:
    arr.append(int(i))

count = 0

for i in arr:
    if sosu(i):
        count+=1


print(count)