import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def PrintArr(arr):
    for i in arr:
        print(i, end=" ")
    print()
def DFS(arr, depth):
    if len(arr) == depth:
        PrintArr(arr)
        return
    
    for i in range(len(nums)):
        if(nums[i] in arr):
            continue
        arr[depth] = nums[i]
        DFS(arr, depth+1)
        arr[depth] = -1

arr = [-1]*M
DFS(arr, 0)