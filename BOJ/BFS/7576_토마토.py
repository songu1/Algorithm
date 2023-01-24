# 토마토 - 최단거리와 비슷
# 익은 토마토, 안익은 토마토 -> 하루 뒤 익은 토마토 인접 토마토도 익게 됨
# 격자 모양 상자, 토마토 정보 -> 며칠이 지나면 다 익게 되는지 최소 일수
# 토마토가 없는 칸도 있음

# 상자 가로칸의 수 m, 상자 세로칸의 수 n
# 하나의 상자에 저장된 토마토들으리 정보(n개의 줄)
    # 익은 토마토 1 / 익지않은 토마토 0 / 토마토X -1

# 토마토가 모두 익을 때 까지의 최소 날짜 출력 (다 못익으면 -1)

import sys
from collections import deque

# bfs 함수
def bfs(box,queue):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m or box[nx][ny]==-1:
                continue
            if box[nx][ny]==0 or box[nx][ny]>(box[x][y]+1):
                box[nx][ny]=box[x][y]+1
                queue.append((nx,ny))
            

# 입력
m,n=map(int, sys.stdin.readline().split())
box=[]
queue=deque()
for i in range(n):
    box.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if box[i][j]==1:
            queue.append((i,j))

# main 코드
bfs(box,queue)

# 출력
result=max(map(max,box))-1
for i in range(n):
    if box[i].count(0)!=0:
        result=-1

print(result)

# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1     # 8

# 6 4
# 0 -1 0 0 0 0
# -1 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1     # -1

# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1    # 6

# 5 5
# -1 1 0 0 0
# 0 -1 -1 -1 0
# 0 -1 -1 -1 0
# 0 -1 -1 -1 0
# 0 0 0 0 0       # 14

# 2 2
# 1 -1
# -1 1            # 0

# 6 4
# 0 0 1 0 -1 1
# 0 -1 0 0 -1 0
# 0 -1 -1 0 0 0
# 0 1 0 0 0 0     # 3