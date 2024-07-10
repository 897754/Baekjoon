import sys

def BinarySearch(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # 없을 경우를 대비한 기본값

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # target을 찾으면 해당 인덱스를 반환
        elif arr[mid] < target:
            result = mid  # target보다 작지만 가장 큰 값의 인덱스 저장
            left = mid + 1
        else:
            right = mid - 1

    return result  # target을 찾지 못했을 경우 가장 가까운 작은 값의 인덱스 반환



arr = []
# 입력
N = int(sys.stdin.readline())
for i in range(N):
    X = int(sys.stdin.readline())
    index = BinarySearch(arr, X)+1
    arr.insert(index, X)
    print(arr[(len(arr)-1)//2])

