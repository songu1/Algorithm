# 토마토 : 3차원 토마토
# 토마토가 격자 모양 상자의 칸게 하나씩 들어있고 상자들을 수직으로 쌓음
# 보관 후 하루가 지나면 익은 토마토에 인접한 익지 않은 토마토가 익음
# 인접 토마토 -> 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯방향
# 토마토를 창고에 보관하는 상자들의 크기, 토마토 정보 -> 며칠이 지나면 토마토가 모두 익는지의 최소 일수
# 토마토가 없는 칸도 있음
# 익은 토마토 : 1 / 익지않은 토마토 : 0 / 토마토X : -1

# 입력 : 상자의 크기를 나타내는 두 정수 m(가로),n(세로)과 상자의 수 h(높이) (n,m : 2~100 / h : 1~100)
# (n개의 줄에 하나의 상자에 담긴 토마토의 정보) * h번 반복됨
    # 각 줄에 m개의 정수
    # 토마토가 하나 이상 있는 경우만 입력으로 주어짐
# 출력 : 토마토가 모두 익을 때까지 최소 며칠이 걸리는지
    # 저장될 때부터 모든 토마토가 익음 : 0
    # 토마토가 모두 익지 못하는 상황 : -1

# 토마토 문제 : queue에 미리 익은 토마토 정보를 넣어두기 : 반복을 줄이기 위해

# 문제점 해결 찾기
    # bfs함수에 nx,ny,nz 크기를 if 0<=nx<h and 0<=ny<n and 0<=nz<m and box[nx][ny][nz]==0 이렇게 지정 => 상관 없음
    # box[nx][ny][nx]>box[x][y][z]+1 조건 -> 가능하지만 bfs라서 없어도 되는 조건!!
    # 출력 시 result=max(map(max,map(max,box)))-1 사용하지 않기 => 틀림!!
        # max(result,max(map(max,box))-1)도 사용할 수 없음
# 결론 : 출력시 map, max를 활용한 출력을 오류가 생길 수 있기때문에 비추


import sys
from collections import deque

# BFS함수
# 아래 위 (상 하 좌 우)
dx=[-1,1,0,0,0,0]   # i h
dy=[0,0,-1,1,0,0]   # j n
dz=[0,0,0,0,-1,1]   # k m
def bfs(box,queue):
    while queue:
        x,y,z=queue.popleft()   # 큐에서 익은 토마토의 인덱스를 꺼냄
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if nx<0 or nx>=h or ny<0 or ny>=n or nz<0 or nz>=m:
                continue
            if box[nx][ny][nz]==0:
                box[nx][ny][nz]=box[x][y][z]+1
                queue.append((nx,ny,nz))


# 입력
m,n,h=map(int,sys.stdin.readline().split())
box=[[0]*n for _ in range(h)]
queue=deque()
for i in range(h):
    for j in range(n):
        box[i][j]=list(map(int,sys.stdin.readline().split()))
        # 큐에 익은 토마토의 인덱스 정보를 추가함
        for k in range(m):
            if box[i][j][k]==1:
                queue.append((i,j,k))

# main 코드
bfs(box,queue)
result=-1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==0:  
                print(-1)
                exit(0)
        result=max(result,max(box[i][j])-1)

print(result)


# 임시 출력(보기 편하기 위해)
# print()
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             print(box[i][j][k],end=' ')
#         print()
#     print()

# 2 2 1
# -1 -1
# -1 -1             # 0

# 5 3 1
# 0 -1 0 0 0
# -1 -1 0 1 1
# 0 0 0 1 1       # -1

# 5 3 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0       # 4

# 4 3 2
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# -1 -1 -1 -1
# 1 1 1 -1        # 0

# 5 3 2
# 0 -1 0 1 -1
# 1 -1 -1 -1 1
# 0 0 0 0 0
# 0 -1 1 -1 1
# -1 1 -1 1 0
# 0 -1 0 0 0      # 3

# 1 1 1
# 1               # 0

# 10 1 1
# 1 0 0 0 0 0 0 0 0 1     # 4

# 3 3 2
# 0 0 1
# 0 -1 0
# 1 0 0
# 0 1 0
# -1 0 0
# 0 0 0           # 3

# 2 2 3
# 1 -1
# -1 0
# -1 0
# 0 0
# 0 0
# 0 0             # -1

# 3 3 2
# 0 0 1
# 0 -1 0
# 1 0 0
# 0 1 0
# -1 0 0
# 0 0 0           # 3