T = int(input())

for a in range(T):
    R,S = input().split(' ')
    R = int(R)

    result = ""
    for i in S:
        for j in range(R):
            result += i
    print(result)
