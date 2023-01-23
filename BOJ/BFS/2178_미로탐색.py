# 미로탐색
# N*M 크기의 배열로 표현되는 미로
# 1 : 이동할 수 있는 칸, 0 : 이동할 수 없는 칸
# (1,1)->(n,m)으로 이동할 때 지나야하는 최소의 칸수 (인접칸으로 이동)

# 입력 : n,m
# n개의 줄에 m개의 정수로 미로

# 지나야하는 최소의 칸 수

import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# bfs 함수
def bfs(maze,x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        # 큐에서 원소 하나 뽑기
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))
    return maze[n-1][m-1]


# main 코드
print(bfs(maze,0,0))

# 4 6
# 101111
# 101010
# 101011
# 111011      # 15

# 4 6
# 110110
# 110110
# 111111
# 111101      # 9

# 2 25
# 1011101110111011101110111
# 1110111011101110111011101       # 38

# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111     # 13