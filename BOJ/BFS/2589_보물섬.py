# 보물섬
# 육지L, 바다 W / 상하좌우 이웃 육지로만 이동(1시간 소요)
# 보물 : 서로 간 최단거리로 이동할 때 가장 긴 시간이 걸리는 육지 2곳
    # 같은 곳 여러번 이동, 멀리 돌아가기X
# 보물 지도 -> 보물이 뭍혀있는 2곳 간의 최단거리 이동 시간

# 입력 : 보물 지도의 세로, 가로 크기 (1~50)
# 보물 지도(빈칸X)
# 출력 : 보물이 묻혀 있는 두 곳 사이의 최단 거리로 이동하는 시간


import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))

# 1차시도 : 57%에서 시간초과(python3) , 통과(pypy3)

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# def bfs(graph,x,y):
#     queue = deque([])
#     dist = [[0]*m for _ in range(n)]
#     dist[x][y] += 1
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 'L' and not dist[nx][ny]:
#                 dist[nx][ny] = dist[x][y] + 1
#                 queue.append((nx,ny))
    
#     return dist[x][y]-1 # 가장 큰 값 - 1하기

# maxTime = -1
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'L':
#             maxTime = max(maxTime,bfs(graph,i,j))
            
# print(maxTime)

# 2차 시도 (힌트참고 : 가로 or 세로에서 끝일 때만 계산) 통과
    # 가장자리에 있는 경우에만 계산하기!!!
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(graph,x,y):
    queue = deque([])
    dist = [[0]*m for _ in range(n)]
    dist[x][y] += 1
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'L' and not dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx,ny))
    return dist[x][y]-1

maxTime = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            if (i>0 and graph[i-1][j]=='L') and (i<n-1 and graph[i+1][j]=='L'):
                continue
            if (j>0 and graph[i][j-1]=='L') and (j<m-1 and graph[i][j+1]=='L'):
                continue
            maxTime = max(maxTime,bfs(graph,i,j))
            
print(maxTime)

# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW         # 8