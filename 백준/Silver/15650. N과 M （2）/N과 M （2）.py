import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def PrintArr(arr):
    for i in arr:
        print(i+1, end=" ")
    print()
def DFS(arr, depth, max):
    if len(arr) == depth:
        PrintArr(arr)
        return
    
    for i in range(max+1, N):
        arr[depth] = i
        DFS(arr, depth+1, i)

arr = [-1]*M
DFS(arr, 0, -1)