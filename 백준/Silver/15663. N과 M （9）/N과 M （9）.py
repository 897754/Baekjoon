import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def PrintArr(arr):
    for i in arr:
        print(nums[i], end=" ")
    print()
def DFS(arr, depth):
    if len(arr) == depth:
        PrintArr(arr)
        return
    
    for i in range(len(nums)):
        if(nums[arr[depth]] == nums[i] and arr[depth] != -1):
            continue
        arr[depth] = -1
        if(i in arr[:depth]):
            continue
        arr[depth] = i
        DFS(arr, depth+1)

arr = [-1]*M
DFS(arr, 0)