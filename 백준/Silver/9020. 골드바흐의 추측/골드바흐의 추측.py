def sosu(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True

def gold(a):
    left = (int)(a/2)
    right = (int)(a/2)
    while left > 0:
        if sosu(left) & sosu(right):
            return (left,right)
        left-=1
        right += 1

    return None

n = int(input())

for i in range(n):
    a = int(input())
    result = gold(a)
    print("{} {}".format(result[0],result[1]))