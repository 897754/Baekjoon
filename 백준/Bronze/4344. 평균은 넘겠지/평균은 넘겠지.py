import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().split()
    sum = 0
    for i in range(1,len(a)):
        sum += int(a[i])
    avg = sum/int(a[0])
    count = 0
    
    for i in range(1,len(a)):
        if int(a[i]) > avg:
            count += 1
    print("{:.3f}%".format(100*count/int(a[0])))
