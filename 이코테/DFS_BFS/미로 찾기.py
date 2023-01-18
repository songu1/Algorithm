# N *M 크기의 직사각형 미로
# 동빈 위치 (1,1) , 출구는 (N,M) 위치하며 한번에 한칸씩 이동가능
# 괴물O : 0 / 괴물X : 1
# 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수 (시작칸과 마지막 칸을 포함해서 계산)
# 시작칸과 마지막칸은 항상 1

# 두 정수 N,M
# N개의 줄에 각가 M개의 정수(0/1) - 공백X

# 최소 이동 칸의 개수

# BFS 사용 -> 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색

# 강의 교재 조금 참고함

import sys
from collections import deque

# 입력
N,M=map(int,sys.stdin.readline().split())

maze=[]

for i in range(N):
    maze.append(list(map(int,sys.stdin.readline().rstrip())))

# 이동할 방향 (상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# BFS 구현
def bfs(maze,x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue=deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        x,y=queue.popleft()
        # 현재 위치에서 4 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            # 괴물있는 경우 무시
            if maze[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))
    return maze[N-1][M-1]

# main코드
print(bfs(maze,0,0))

# 3 3
# 110
# 010
# 011

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111      # 10