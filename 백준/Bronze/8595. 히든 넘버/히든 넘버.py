N = int(input())
string = input()

i = 0
sum = 0
while(i < N):
    if('0' <= string[i] and string[i] <= '9'):
        start = i
        while(i < N and '0' <= string[i] and string[i] <= '9'):
            i+=1
        end = i
        sum += int(string[start:end])
    i+=1

print(sum)