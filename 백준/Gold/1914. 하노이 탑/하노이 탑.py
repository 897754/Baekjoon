def Hanoi(N, curPos, targetPos):
    result = ""
    if N == 1:
        return "{} {}\n".format(curPos,targetPos)
    else:
        result += Hanoi(N-1, curPos, GetOther(curPos,targetPos))
        result += "{} {}\n".format(curPos,targetPos)
        result += Hanoi(N-1, GetOther(curPos,targetPos), targetPos)
        return result
        

def GetOther(a, b):
    for i in range(1,4):
        if (a != i) & (b != i):
            return i

n = int(input())
print(2**n-1)
if (n <= 20):
    print(Hanoi(n,1,3))