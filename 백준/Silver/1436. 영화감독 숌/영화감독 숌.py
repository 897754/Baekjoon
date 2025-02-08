import sys

def Check(i):
    s = str(i)
    i = 0
    for _ in s:
        if(_ == "6"):
            i += 1
            if(i == 3):
                return True
        else:
            i = 0
    return False

input = sys.stdin.readline

i = int(input())

cur = 665
j = 0
while(j < i):
    cur+=1
    if Check(cur):
        j+=1
print(cur)