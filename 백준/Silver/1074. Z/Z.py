import sys

count = 0
def Search(x,y,size):
    global count
    if x == r and y == c:
        print(count)
        return
    if x == r and y+1 == c:
        print(count+1)
        return
    if x+1 == r and y == c:
        print(count+2)
        return
    if x+1 == r and y+1 == c:
        print(count+3)
        return
    if size > 2:
        newSize = size//2
        if r < x+newSize:
            if c < y+newSize:
                Search(x,y,newSize)
            else:
                count += (newSize * newSize)
                Search(x,y+newSize,newSize)
        else:
            if c < y+newSize:
                count += (newSize * size)
                Search(x+newSize,y,newSize)
            else:
                count += (newSize*newSize*3)
                Search(x+newSize,y+newSize,newSize)




input = sys.stdin.readline().split()

n = int(input[0])
r = int(input[1])
c = int(input[2])

Search(0,0,2**n)