import sys

def FB(i):
    if(i % 3 == 0):
        if(i % 5 == 0):
            return "FizzBuzz"
        else:
            return "Fizz"
    else:
        if(i % 5 == 0):
            return "Buzz"
        else:
            return i 

input = sys.stdin.readline

result = -1
inputs = []
for _ in range(3):
    s = input().rstrip()
    if(s == "Fizz" or s == "Buzz" or s == "FizzBuzz"):
        inputs.append(s)
    else:
        result = int(s) + 3 - _
        
print(FB(result))