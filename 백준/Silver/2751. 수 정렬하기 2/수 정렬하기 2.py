def merge_sort(arr):
    if len(arr) > 1:
        # 중간 지점을 찾아 배열을 두 부분으로 나눕니다.
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 각 부분을 재귀적으로 병합 정렬합니다.
        merge_sort(left_half)
        merge_sort(right_half)

        # 병합 과정
        i = j = k = 0

        # left_half와 right_half의 요소들을 비교하여 정렬된 배열을 만듭니다.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 요소들을 추가합니다.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

merge_sort(arr)

for i in arr:
    print(i)