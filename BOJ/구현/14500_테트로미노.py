# 테트로미노
# 정사각형 4개를 이어붙인 폴리오미노 5가지
# n*m인 종이 위에 테트로미노 하나 놓아서 칸에 적힌 수의 합이 최대가 되는 프로그램

# 입력 : 세로 n, 가로 m (4~500)
# 종이에 쓰인 수 (1000이하의 자연수)
# 출력 : 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값

import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited=[[False]*m for _ in range(n)]

# 시계방향 (12-3-6-9시)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def tetromino(graph,x,y):   # 1번 block (x, y)
    sum = -1
    # 2번 block (nx, ny) - i방향
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        # 3번 block (nxx, nyy) - j방향
        for j in range(4):
            if j == i+2 or j == i-2 : continue
            nxx = nx + dx[j]
            nyy = ny + dy[j]
            if nxx<0 or nxx>=n or nyy<0 or nyy>=m: continue
            # 4번 block (nxxx, nyyy) - k방향
            mx = -1
            # 2번 block에 추가(3번 block 위치 제외)
            for k in range(4):
                if k == i+2 or k == i-2 or k == j: continue
                nxxx = nx + dx[k]
                nyyy = ny + dy[k]
                if nxxx<0 or nxxx>=n or nyyy<0 or nyyy>=m: continue
                mx = max(mx, graph[nxxx][nyyy])
            # 3번 block에 추가
            for k in (j,j-1,j-3):
                nxxx = nxx + dx[k]
                nyyy = nyy + dy[k]
                if nxxx<0 or nxxx>=n or nyyy<0 or nyyy>=m: continue
                mx = max(mx, graph[nxxx][nyyy])
            sum = max(sum, graph[x][y] + graph[nx][ny] + graph[nxx][nyy] + mx)
    return sum



sum=-1
for i in range(n):
    for j in range(m):
        sum = max(tetromino(graph,i,j),sum)

print(sum)


# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1               # 19

# 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5               # 20

# 4 10
# 1 2 1 2 1 2 1 2 1 2
# 2 1 2 1 2 1 2 1 2 1
# 1 2 1 2 1 2 1 2 1 2
# 2 1 2 1 2 1 2 1 2 1     # 7