x = int(input())

i = 1

while (x > i):
    x -= i
    i+=1


a = x if i%2==0 else (i-x+1) 
b = (i-x+1) if i%2==0 else x

print(f"{a}/{b}")