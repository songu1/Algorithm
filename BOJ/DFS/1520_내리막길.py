# 내리막길 - 목표 40분~60분
# 각 지점에 그 지점의 높이가 쓰여있음, 각 지점 사이의 이동은 상하좌우만 가능
# (0,0) -> (m-1,n-1)로
# 항상 높이가 너 낮은 지점으로만 이동하여 목표 지점으로 이동
# 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수

# 입력 : 지도의 세로 m, 가로 n (1~500)
# m개의 줄에걸쳐 각 지점의 높이 (1~10000)
# 출력 : 이동가능한 경로의 수 H (0~10억)

# 1번째 풀이 : 일반 DFS처럼 -> 시간 초과
# 2번째 풀이 : DFS+DP(메모리제이션) -> Top-down 방식(200ms 정도)
# 3번째 풀이 : DFS+DP -> Bottom-up 방식 (140ms 정도)

import sys
sys.setrecursionlimit(100000000)
# 입력
m,n = map(int, sys.stdin.readline().split())
graph=[]
d=[[-1]*n for _ in range(m)]
for i in range(m):
    graph.append(list(map(int,sys.stdin.readline().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 2번풀이 - Top-down 방식
# dfs 함수
def dfs(x,y):
    global d
    # 이미 처리한 위치
    if d[x][y]!=-1:
        return d[x][y]
    # 현재 위치가 출발지
    if x==0 and y==0:
        d[x][y]=1
        return d[x][y]
    # 출발지가 아닐 경우
    d[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        # 주어진 범위 밖
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        # 1단계 이전 위치가 현재위치보다 크고, 출발위치보다 작을때
        if graph[nx][ny]>graph[x][y] and graph[nx][ny]<=graph[0][0]:
            d[x][y] += dfs(nx,ny)
    return d[x][y]

# main 코드
print(dfs(m-1,n-1))

# 3번 풀이 - Bottom-up
d=[[-1]*n for _ in range(m)]
# dfs함수
def dfs3(x,y):
    if x==m-1 and y==n-1:
        return 1
    if d[x][y]==-1:
        d[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 주어진 범위 밖
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny]<graph[x][y] and graph[nx][ny]>=graph[m-1][n-1]:
                d[x][y] += dfs3(nx,ny)
    return d[x][y]
print(dfs3(0,0))



# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10      # 3

# 2 2
# 50 30
# 20 15               # 2

# 1 1
# 30                  # 1

# 2 3
# 50 40 10000
# 20 20 10            # 1