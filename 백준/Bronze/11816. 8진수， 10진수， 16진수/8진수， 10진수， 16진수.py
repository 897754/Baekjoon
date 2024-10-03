N = input()

result = 0
if(N[0] == '0'):
    if(N[1] == 'x'):
        #16진수
        result = int(N, 16)
    else:
        #8진수
        result = int(N, 8)
else:
    #10진수
    result = int(N)
    
print(result)