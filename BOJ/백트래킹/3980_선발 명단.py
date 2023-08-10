# 선발 명단
# 챔스 결승 4-4-2 전술 / 11명의 포지션 결정
# 각 포지션에서의 능력을 0~100까지 수치화(0은 적합하지 않음)
# 모든 선수의 포지션을 정하는 프로그램
# 모든 포지션에 선수 배치, 능력치가 0인 포지션에 배치X

# 입력 : 테스트케이스 수 c
# 11행 11열에 능력치 sij(0~100) : i번 선수가 j번 포지션에서 뛸때의 능력
    # 적합한 포지션 수(능력치>0 수) 는 최대 5개
# 출력 : 각 테스트케이스에 대해 능력치 합의 최댓값을 한줄에 하나씩 출력

import sys

c = int(sys.stdin.readline())

# 백트래킹 함수
def backtracking(num,arr):
    global maxS
    if num == 11:
        maxS = max(maxS, sum(arr))
        return
    
    for (i,s) in position[num]:
        if not checked[i]:
            checked[i] = True
            backtracking(num+1, arr + [s])
            checked[i] = False

for _ in range(c):
    position = [[] for _ in range(11)]
    checked = [False]*11
    maxS = 0
    for i in range(11):
        pos = list(map(int,sys.stdin.readline().split()))
        for j in range(11):
            if pos[j] != 0:
                position[i].append((j,pos[j]))
    # print(*position,sep="\n")
    backtracking(0,[])
    print(maxS)

            






# 1
# 100 0 0 0 0 0 0 0 0 0 0
# 0 80 70 70 60 0 0 0 0 0 0
# 0 40 90 90 40 0 0 0 0 0 0
# 0 40 85 85 33 0 0 0 0 0 0
# 0 70 60 60 85 0 0 0 0 0 0
# 0 0 0 0 0 95 70 60 60 0 0
# 0 45 0 0 0 80 90 50 70 0 0
# 0 0 0 0 0 40 90 90 40 70 0
# 0 0 0 0 0 0 50 70 85 50 0
# 0 0 0 0 0 0 66 60 0 80 80
# 0 0 0 0 0 0 50 50 0 90 88       # 970