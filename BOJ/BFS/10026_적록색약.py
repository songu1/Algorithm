# 크기 n*n인 그리디에 RGB 중 하나 색칠
# 구역은 같은색 - 몇개의 구역
# 같은 색상이 상하좌우로 인접 -> 같은 구역
# 적록색약이아닌 사람 인접한 R,G,B로 구역의 수
# 적록색약인 사람 인접한 RG,B로 구역의 수
# 적록색약인 사람이 봤을 때 ,아닌 사람이 봣을 때 구역의 수

# 입력 : n
# n개의 줄에 그림이 주어짐

# 출력 : 적록색약이 아닌 경우 구역의 수 / 적록색약인 사람 구역의 수

import sys
from collections import deque

# bfs 함수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y,color):
    queue=deque()
    if graph[x][y]=='O':
        return False
    queue.append((x,y))
    graph[x][y]='O'
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==color:
                queue.append((nx,ny))
                graph[nx][ny]='O'
    return True

# 입력
n=int(sys.stdin.readline())
normal=[]
colorX=[[] for _ in range(n)]
for i in range(n):
    normal.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(n):
        if normal[i][j]=='G':
            colorX[i].append('R')
        else:
            colorX[i].append(normal[i][j])

nor=0
col=0
for i in range(n):
    for j in range(n):
        if bfs(normal,i,j,normal[i][j])==True:
            nor+=1
        if bfs(colorX,i,j,colorX[i][j])==True:
            col+=1
print(nor, col)
        





# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR       # 4 3