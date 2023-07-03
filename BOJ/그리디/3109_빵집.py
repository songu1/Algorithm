# 빵집
# 원웅이는 근처 빵집의 가스관에 몰래 파이프를 설치해 훔쳐서 사용
# 빵집 위치 R*C (1열 : 근처 빵집 가스관, 마지막열 : 원웅이의 빵집)
# 가스관과 빵집을 연결하는 파이프 설치(사이에 건물이 있다면 놓을 수 없음)
# 가스관 - 빵집 파이프라인은 1열에서 시작, 마지막열에서 끝
# 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선 연결 / 각 칸 중심끼리 연결
# 가스관과 빵집을 연결하는 파이프라인 여러개 설치, 경로 겹치거나 접할 수 X

# 입력 : R,C(1~10000 / 5~500)
# 빵집 근처의 모습 (.:빈칸 / x:건물) - 1열, 마지막열은 비어있음
# 출력 : 원웅이가 놓을 수 있는 파이프라인의 최대 개수

# 1차 시도 시간초과

import sys

r,c = map(int,sys.stdin.readline().split())
graph = []
for i in range(r):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))

dx=[-1,0,1]
dy=[1,1,1]
# dfs 함수
def dfs(graph,x,y):
    # 도착지에 도달
    if y == c-1:
        return True
    # 방문 처리
    graph[x][y] = 'x'
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny >= c:
            continue
        if graph[nx][ny] == '.':
            if dfs(graph,nx,ny):
                return True

    return False

# main 함수
case = 0
for i in range(r):
    if dfs(graph,i,0):
        case += 1
print(case)

# 5 5
# .xx..
# ..x..
# .....
# ...x.
# ...x.           # 2

# 6 10
# ..x.......
# .....x....
# .x....x...
# ...x...xx.
# ..........
# ....x.....      # 5