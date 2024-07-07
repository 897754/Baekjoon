import sys

def Distance(sr, pos):
    return abs(sr-pos[0])+pos[1]

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

    # y좌표 너무 멀면 배열에 안넣음
    # 여기는 나중에 빼고 해보자
    if L >= pos[1]:
        animals.append(pos)
animals.sort(key= lambda x : x[0])

# 여기서부터 로직 시작

sr.sort()

# j 1 4 6 9
# i (1,4)
count = 0
for i in animals:
    # 동물 기준
    for j in sr:
        # 사대가 너무 왼쪽에 있는 경우
        if i[0] - L > j:
            #print(f"Left : {i} {j}")
            continue
        # 사대가 너무 오른쪽에 있는 경우
        if i[0] + L < j:
            #print(f"Right : {i} {j}")
            break
        #동물 기준 한개의 사대라도 사거리 안에 있으면 count++, break.
        if Distance(j,i) <= L:
            count+=1
            break


print(count)