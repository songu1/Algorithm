# 어른 상어
# 상어 1~M 번호 / 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아냄
# 1번 가장 강력해서 모두를 쫓아낼 수 있음
# N*N 크기의 격자 중 M개의 칸에 상어 한마리씩
# (1) 모든 상어가 자신의 위치에 냄새를 부림
# (2) 1초마다 모든 상어가 동시에 상하좌우 인접한 칸 중 하나로 이동, 냄새를 뿌림
    # 이동방향 : 인접한 칸 중 아무 냄새 없는칸
        # 없으면 자신의 냄새가 있는 칸의 방향 (우선순위를 따름)
            # 상어가 맨 처음 보고 있는 방향 입력, 그 후 방금 이동한 방향이 보고 있는 방향
# (3) 상어가 K번 이동하고 나면 냄새 사라짐
# 모든 상어가 이동한 후 한 칸에 여러마리 상어 -> 가장 작은 번호만 남고 쫒겨남
# 이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇초가 걸리는지

# 입력 : N,M,K (n:2~20 / 2 <= m <= n^2, k:1~1000)
# n개의 줄에 격자의 모습 0:빈칸 , x번 : x번 상어가 들어있는 칸
# 각 상어의 방향 (1위,2아래,3왼쪽,4오른쪽)
# 각 상어의 방향 우선순위가 상어당 4줄씩, 1줄에 4개의 수
    # 1번줄 : 현재가 위 / 2번줄 : 현재가 아래 / 3번줄 : 현재가 왼쪽 / 4번줄 : 현재가 오른쪽
# 출력 : 1번 상어만 격자에 남게되기까지 걸리는 시간 (1000초 넘으면 -1 출력)

import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())
graph = []
loc = [0]*(m+1)    # 상어의 위치
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        # 버전1
        # graph[i][j] = [graph[i][j]] + [0]
        # if graph[i][j][0] != 0:
        #     loc[graph[i][j][0]] = (i,j)
        #     graph[i][j][1] = 1  # 현재 위치 방문했다고 체크
        # 버전2
        if graph[i][j] != 0:
            graph[i][j] = [graph[i][j]] + [1]
            loc[graph[i][j][0]] = (i,j)
        else:
            graph[i][j] = [graph[i][j]] + [0]
dir = [0] + list(map(int,sys.stdin.readline().split()))
priority = [[] for _ in range(1+m)]
for i in range(1,m+1):
    for _ in range(4):
        priority[i].append(list(map(int,sys.stdin.readline().split())))

print(*graph,sep="\n")

dx = [9,-1,1,0,0]   # 위,아래,왼쪽,오른쪽
dy = [9,0,0,-1,1]   # 인덱스 0은 제외

queue = deque([])       # 냄새 큐
time = 0
while True:
    smell = []      # 현재 시간에 생성된 냄새 배열
    time += 1
    if time > 1000:     # 1000 이상인 경우 -1 출력
        time = -1
        break
    # 상어 별로 실행
    for i in range(1,m+1):   # i번째 상어
        if loc[i] == 0:
            continue
        # 현재 상어 위치 방문 처리
        x,y = loc[i]
        graph[x][y][0] *= -1
        smell.append((x,y))
        # 상어 이동
        for j in range(8):      # 우선순위 인덱스 j
            # (1) j가 0~3 -> 냄새 없는 칸으로 상어가 이동
            if 0 <= j < 4:
                d = priority[i][dir[i]-1][j]  # 이동할 방향
                nx = x + dx[d]
                ny = y + dy[d]
                # 위치 밖이거나 다음칸이 냄새만 있는 칸일 경우
                if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny][0] < 0:
                    continue
                # 냄새가 없는 위치로 이동
                if graph[nx][ny][0] == 0:
                    graph[nx][ny][0] = i
                    graph[nx][ny][1] += 1     # 몇번째 방문인지
                    loc[i] = (nx,ny)
                    dir[i] = d
                    break
                # 냄새가 없지만 상어가 있는 위치로 이동, 더 작은 번호의 상어를 만났을 때 => 쫒겨남
                elif graph[nx][ny][0] > 0 and graph[nx][ny][1] == 1 and graph[nx][ny][0] < i:
                    loc[i] = 0  
                    dir[i] = 0
                    break
            # (2) j가 4~7 -> 자신의 냄새가 있는 곳으로 이동
            else:
                d = priority[i][dir[i]-1][j-4]  # 이동할 방향
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny][0] == i*(-1):
                    graph[nx][ny][0] = i
                    graph[nx][ny][1] += 1     # 몇번째 방문인지
                    loc[i] = (nx,ny)
                    dir[i] = d
                    break
    
    # 1번 상어만 남았다면 break
    if loc.count(0) == m:
        break
    # 냄새 배열 queue에 추가
    queue.append(smell)
    # 시간이 k이상(상어가 k번 이상 움직임) -> 매번 smell을 큐에 넣어줬으므로 k이상일때부터 매번 pop해줌
    if time >= k:
        smell = queue.popleft()
        for (x,y) in smell:
            graph[x][y][1] -= 1
            if graph[x][y][1] <= 0:
                graph[x][y][0] = 0

print(time)

# 5 4 4
# 0 0 0 0 3
# 0 2 0 0 0
# 1 0 0 0 4
# 0 0 0 0 0
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3             # 14

# 4 2 6
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 2
# 4 3
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3             # 26

# 5 4 1
# 0 0 0 0 3
# 0 2 0 0 0
# 1 0 0 0 4
# 0 0 0 0 0
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3             # -1

# 5 4 10
# 0 0 0 0 3
# 0 0 0 0 0
# 1 2 0 0 0
# 0 0 0 0 4
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3             # -1