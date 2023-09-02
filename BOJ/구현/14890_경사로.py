# 경사로 - 문제 너무 불친절
# n*n 지도+높이 -> 이 지도에서 지나갈 수 있는 길이 몇개인지
# 길 : 한 행 or 한 열 전부
    # 길에 속한 모든 칸의 높이가 모두 같아야함
    # 경사로(길이 1)를 놓아서 지나갈 수 있는 길을 만듦
    # 경사로 : 낮은칸과 높은 칸을 연결
# 경사로 조건
    # 낮은칸에 놓임, L개의 연속된 칸에 경사로의 바닥이 모두 접해야함
    # 낮은칸과 높은 칸의 높이차이가 1이어야함
    # 경사로를 놓을 낮은 칸의 높이는 모두 같아야함
    # 경사로를 놓을 L개의 칸이 연속되어야함
    # 한 칸에 한번만 놓을 수 있음
# 지도 -> 지나갈 수 있는 길의 개수
# 가로와 세로가 겹치는 경우는 해당X , 같은 라인에서만 해당
    # https://www.acmicpc.net/board/view/104604 게시판 글 참고(문제 설명 부족)

# 입력 : n(2~100) , L(1~n)
# n개의 줄에 지도에 높이 (1~10)
# 출력 : 지나갈 수 있는 길의 개수

# 너무 욕심부리지 말고 빠르게 해결하는 방법 선택하기
# 오르막길 구하는 함수와 내리막길을 구하는 함수를 따로 생성하여 답을 구함

import sys

n,l = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 경사로 함수(오르막길)
def findUphill(path,done):
    # 배열의 처음 값 체크
    pre = path[0]
    ramp = [0]
    down = False
    for i in range(1,n):
        # 같은 높이
        if path[i] == pre:
            if len(ramp) < l:
                ramp.append(i)
            else:
                del ramp[0]
                ramp.append(i)
        # 1칸 올라감
        elif path[i] == pre+1:
            if len(ramp) < l and down:
                return False
            ramp = [i]
            down = False
        # 1칸 내려감
        elif path[i] == pre-1:
            if len(ramp) < l and down:
                return False
            down = True
            ramp = [i]
        # 높이 차이가 2이상인 경우
        else:
            return False
        # 오르막길 경사로 생성
        if len(ramp) == l and down:
            while ramp:
                j = ramp.pop()
                done[j] = True
            down = False
        pre = path[i]
    if len(ramp) < l and down:
        return False
    return True

# 경사로 함수(내리막길)
def findDownhill(path,done):
    # 배열의 처음 값 체크
    pre = path[0]
    ramp = []
    if not done[0]:
        ramp.append(0)
    for i in range(1,n):
        # 경사로가 없는 위치
        if not done[i]:
            # 같은 높이로 이동
            if path[i] == pre:
                if len(ramp) < l:
                    ramp.append(i)
                else:
                    del ramp[0]
                    ramp.append(i)
            # 1칸 올라감
            elif path[i] == pre+1:
                if len(ramp) < l:
                    return False
                while ramp:
                    j = ramp.pop()
                    done[j] = True
                ramp = [i]
            # 1칸 내려가는 경우와, 높이 차이가 2이상인 경우는 findUphill함수로 판별됨
        # 경사로가 이미 있는 경우는 제외
        else:
            ramp = []
        pre = path[i]

    return True

road = 0
# 행,열 탐색
for i in range(n):
    # i행 탐색
    done = [False]*n
    if findUphill(graph[i],done) and findDownhill(graph[i],done):
        road += 1
    # i열 탐색
    done = [False]*n
    arr = [graph[k][i] for k in range(n)]
    if findUphill(arr,done) and findDownhill(arr,done):
        road += 1
print(road)

# 6 2
# 3 3 3 3 3 3
# 2 3 3 3 3 3
# 2 2 2 3 2 3
# 1 1 1 2 2 2
# 1 1 1 3 3 1
# 1 1 2 3 3 2         # 3

# 6 2
# 3 2 1 1 2 3
# 3 2 2 1 2 3
# 3 2 2 2 3 3
# 3 3 3 3 3 3
# 3 3 3 3 2 2
# 3 3 3 3 2 2         # 7

# 6 3
# 3 2 1 1 2 3
# 3 2 2 1 2 3
# 3 2 2 2 3 3
# 3 3 3 3 3 3
# 3 3 3 3 2 2
# 3 3 3 3 2 2         # 3

# 6 1
# 3 2 1 1 2 3
# 3 2 2 1 2 3
# 3 2 2 2 3 3
# 3 3 3 3 3 3
# 3 3 3 3 2 2
# 3 3 3 3 2 2         # 11