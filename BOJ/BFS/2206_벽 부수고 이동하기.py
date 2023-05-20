# 벽 부수고 이동하기 - 알고리즘 풀이 참고 **** 어려움
# n*m 맵 : 0(이동가능), 1(벽)
# (1,1) -> (n,m) 최단경로로 이동
    # 맵에서 가장 적은 개수의 칸을 지나는 경로(시작칸과 끝칸 포함하여 계산)
# 이동하는 도중에 1개의 벽을 부수고 이동가능

# 입력 : n(1~1000), m(1~1000)
# n개의 줄에 m개의 숫자 / (1,1)과 (n,m)은 항상 0이라 가정
# 출력 : 최단거리 출력 / 불가능시 -1 출력

# 1,2번 시도(브루트포스) : 시간초과
# 주의! : 파이썬 and / 자바 &

import sys
from collections import deque

# 입력
n,m = map(int,sys.stdin.readline().split())
graph=[]    # 맵
wall=[[[0]*2 for _ in range(m)] for _ in range(n)]     
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

# 임시 출력 함수
# def printWall(wall):
#     for i in range(n):
#         for j in range(m):
#             print(str(wall[i][j][0]).zfill(2),end=" ")
#         print(" ",end=" ")
#         for j in range(m):
#             print(str(wall[i][j][1]).zfill(2),end=" ")
#         print()
#     print()

# bfs 함수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(wall,x,y):
    # 큐에 출발 위치 삽입
    queue=deque()
    queue.append((x,y,0))
    # 출발 위치 방문 처리
    wall[x][y][0]=1
    # 탐색
    while queue:
        x,y,z=queue.popleft()
        if x==n-1 and y==m-1:
            return wall[x][y][z]
        # 상하좌우 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 다음 위치가 벽이 아닐 경우 ( __ -> 0 )
            if graph[nx][ny]==0 and wall[nx][ny][z]==0:
                wall[nx][ny][z] = wall[x][y][z]+1
                queue.append((nx,ny,z))
            # 위치가 0 -> 1로, 벽부수기 기록 없을 때
            elif graph[nx][ny]==1 and z==0 and wall[nx][ny][1]==0:
                wall[nx][ny][1] = wall[x][y][z]+1
                queue.append((nx,ny,1))
            # 위치 1 -> 1은 불가능
        # printWall(wall)

    # 도달하지 못했을 경우
    return -1

# main코드
print(bfs(wall,0,0))



# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000        # 15

# 4 4
# 0111
# 1111
# 1111
# 1110        # -1

# 6 4
# 0000
# 1110
# 1000
# 0000
# 0111
# 0000        # 9

# 5 4
# 0000
# 1110
# 1000
# 1011
# 1000        # 8

# 5 6
# 000000
# 011110
# 010000
# 010111
# 100000      # 10

# 10 2
# 01
# 00
# 10
# 00
# 01
# 00
# 10
# 00
# 01
# 00          # 13

# 8 4
# 0000
# 0110
# 1110
# 0000
# 0111
# 0000
# 1110
# 0000        # 11

# 1 1
# 0           # 1