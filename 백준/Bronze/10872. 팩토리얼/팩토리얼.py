def Fact(n):
    if n == 0: 
        return 1
    return Fact(n-1)*n

N = int(input())
print(Fact(N))