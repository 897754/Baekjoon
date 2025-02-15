import sys

input = sys.stdin.readline

S = {}
def execute(opt, value):
    global S
    if(opt == "add"):
        S[value] = 1 
    elif(opt == "remove"):
        if(value not in S.keys()):
            return
        del S[value]
    elif(opt == "check"):
        if(value in S.keys()):
            print("1")
        else:
            print("0")
    elif(opt == "toggle"):
        if(value in S.keys()):
            del S[value]
        else:
            S[value] = 1

    elif(opt == "all"):
        for i in range(1, 21):
            S[i] = 1 
    elif(opt == "empty"):
        S = {}

M = int(input())

for i in range(M):
    cur = input().split()
    if(len(cur) > 1):
        opt = cur[0]
        value = int(cur[1])
        execute(opt, value)
    else:
        opt = cur[0]
        execute(opt, 0)