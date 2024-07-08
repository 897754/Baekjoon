import sys

# def Distance(sr, pos):
#     return abs(sr-pos[0])+pos[1]

#해당 동물이 사거리 내에 있는 sr이 있는지 반환
def Check(srArr, a, L):
    start = 0
    end = len(sr)
    range = L-a[1]

    while start < end:
        mid = (start + end) // 2
        # 사거리 내에 sr 확인
        if abs(srArr[mid] - a[0]) <= range:
            return True
        if srArr[mid] > a[0]:
            end = mid
        else:
            start = mid + 1
    
    return False



# M : 사대의 수
# N : 동물의 수
# L : 사거리
firstInput = sys.stdin.readline().split()
M = int(firstInput[0])
N = int(firstInput[1])
L = int(firstInput[2])

max = 0

# 사대 X좌표 입력
sr = []
input = sys.stdin.readline().split()
for i in range(M):
    sr.append(int(input[i]))
    

# 배열 크기만큼 좌표 입력
animals = []
for i in range(N):
    input = sys.stdin.readline().split()
    pos = (int(input[0]),int(input[1]))
    if pos[1] <= L:
        animals.append(pos)

# 여기서부터 로직 시작

sr.sort()

count = 0
for a in animals:
    if Check(sr, a, L):
        count+=1
print(count)