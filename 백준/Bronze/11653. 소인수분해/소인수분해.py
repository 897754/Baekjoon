N = int(input())

div = 2

while (N > 1):
    if(N%div == 0):
        print(div)
        N //= div
        continue
    div+=1

