import sys

input = sys.stdin.readline


while(True):
    s = input().strip()
    if(s == "0"):
        break
    l = len(s)
    flag = True
    for i in range(l//2):
        if s[i] != s[-i-1]:
            flag = False
            break
    print("yes" if flag else "no")