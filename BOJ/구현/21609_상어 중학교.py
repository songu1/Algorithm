# 상어 중학교
# n*n 격자 : 모든 칸에 검은색(-1), 무지개(0), 일반 블록(m가지 색상-자연수)
# 상하좌우 인접한 칸
# 블록 그룹 : 연결된 블록의 집합
    # 일반블록 1개 이상, 일반블록의 색은 모두 같아야함
    # 검은 블록 포함 X , 무지개 블록 상관없음
    # 기준 블록 : 일반 블록 중 행의 번호가 가장 작은 블록, 열의 번호가 가장 작은 블록
# 오토 플레이 기능
    # 1) 크기가 가장 큰, 무지개 수가 가장 많은, 기준 블록의 행이 가장 큰, 열이 가장 큰 블록
    # 2) 1의 블록그룹 제거하고 (해당 블록 그룹 블록 수)^2점을 획득
    # 3) 격자에 중력 작용(무지개블록, 일반블록 밑으로 떨어짐)
    # 4) 격자 90도 반시계 회전
    # 5) 격자 중력 작용(무지개 블록, 일반블록 밑으로 떨어짐)
# 오토 플레이가 모두 끝났을 때 획득한 점수의 합

# 입력 : 격자 한변의 크기 n, 색상의 개수 m
# n개의 줄에 블록의 정보 1행~n행
# 획득한 점수의 합

# 문제를 제대로 안읽어서 틀림!!!

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 함수 - 블록 그룹 찾기
def bfs(graph,x,y,visited):
    queue = deque([])
    group1 = []     # 블록 그룹(일반)
    group2 = []     # 블록 그룹(무지개)
    # 방문처리 - 일반 블록일 때만
    color = graph[x][y]
    visited[x][y] = True
    group1.append((x,y))
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        # 위치 찾기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 격자 밖이거나 검은 블록이면 pass
            if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny] == -1:
                continue
            # 아직 방문하지 않은 일반/무지개 블록인 경우
            if not visited[nx][ny] and graph[nx][ny] in (color,0):
                visited[nx][ny] = True
                queue.append((nx,ny))
                # 같은 색의 일반블록인 경우
                if graph[nx][ny] == color:
                    group1.append((nx,ny))
                # 무지개 블록인 경우
                elif graph[nx][ny] == 0:
                    group2.append((nx,ny))  
    return group1, group2

# 중력 함수
def gravity(graph,maxGroup):
    for (x,y) in maxGroup:
        if x > 0:
            for i in range(x,0,-1):
                if graph[i-1][y] == -1:
                    break
                graph[i][y] = graph[i-1][y]
                graph[i-1][y] = -2

# 반시계 90도 회전 함수
def rotate(graph):
    new = [[-2]*n for _ in range(n)]
    maxGroup = []
    for i in range(n):
        for j in range(n):
            new[i][j] = graph[j][n-i-1]
            if new[i][j] == -2:
                maxGroup.append((i,j))
    return new, maxGroup

# main
score = 0
while True:
    # 블록 그룹 탐색 & 제거할 블록 그룹 찾기
    visited = [[False]*n for _ in range(n)]
    maxSize, maxRainbow = 1, -1     # 블록 그룹 크기는 최소 2, 무지개수는 최소 0
    maxGroup = []
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 일반 블록을 bfs 탐색
            if not visited[i][j] and graph[i][j] > 0:
                group1, group2 = bfs(graph,i,j,visited)
                size = len(group1+group2)
                # 크기가 1이면 pass
                if size < 2:
                    continue
                # 크기가 큰 블록 그룹 / 크기가 같고 무지개수가 많은 블록그룹일 경우
                if size > maxSize:
                    maxSize = size
                    maxRainbow = len(group2)
                    maxGroup = group1 + group2
                elif size == maxSize and len(group2) >= maxRainbow:
                    maxRainbow = len(group2)
                    maxGroup = group1 + group2
                # visited 배열 무지개 초기화
                for (x,y) in group2:
                    visited[x][y] = False
    if maxSize == 1:    # 찾은 그룹이 없음
        break
    # 블록 그룹 제거
    for (x,y) in maxGroup:
        graph[x][y] = -2    # 빈칸
    score += maxSize**2 
    maxGroup.sort()
    gravity(graph,maxGroup)
    graph, maxGroup = rotate(graph)
    gravity(graph,maxGroup)

print(score)


# 5 3
# 2 2 -1 3 1
# 3 3 2 0 -1
# 0 0 0 1 2
# -1 3 1 3 2
# 0 3 2 2 1       # 77

# 6 4
# 2 3 1 0 -1 2
# 2 -1 4 1 3 3
# 3 0 4 2 2 1
# -1 4 -1 2 3 4
# 3 -1 4 2 0 3
# 1 2 2 2 2 1     # 125

# 4 3
# 1 1 1 3
# 3 2 3 3
# 1 2 -1 3
# -1 -1 1 1       # 33