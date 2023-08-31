# 탈출
# 티떱숲 : r행 c열 / 비어있는 곳:. , 물이 차있는지역:* , 돌:X , 비버의 굴:D , 고슴도치: S
# 매 분마다 고슴도치는 현재 있는 칸과 인접한 칸으로 이동가능
# 물 : 매분마다 비어있는 칸으로 확장 - 물이 있는 칸의 인접칸
# 고슴도치 : 돌, 물 통과 불가 , 물이 찰 예정인 칸으로 이동할 수 없음
# 물 : 돌, 비버굴 통과 불가
# 숲의 지도 -> 고슴도치가 안전하게 비버의 굴로 이동하기 위한 최소 시간

# 입력 : r,c (1~50)
# r줄에 숲의 지도 : . * X D S (D,S는 1개만)
# 출력 : 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간 (없다면 KAKTUS 출력)

import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
graph = []
water = []
visited = [[0]*c for _ in range(r)]     # 고슴도치 방문
for i in range(r):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(c):
        if graph[i][j] == 'S':
            start = (i,j)
        if graph[i][j] == '*':
            water.append((i,j))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(graph,x,y,water):
    queue = deque([])
    # 방문 처리
    graph[x][y] = '.'
    visited[x][y] = True
    queue.append((0,x,y))
    preTime = -1
    while queue:
        time,x,y = queue.popleft()
        if time > preTime:
            water = moveWater(water,[])
        # 고슴도치 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                continue
            if not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((time+1,nx,ny))
            elif graph[nx][ny] == 'D':
                return time+1
        preTime = time
    return "KAKTUS"

def moveWater(water,q):
    # 물 이동
    while water:
        a,b = water.pop()  
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na<0 or na>=r or nb<0 or nb>=c:
                continue
            if graph[na][nb] == '.':
                graph[na][nb] = '*'
                q.append((na,nb))
    return q

print(bfs(graph,start[0],start[1],water))

# 3 3
# D.*
# ...
# .S.         # 3

# 3 3
# D.*
# ...
# ..S         # KAKTUS

# 3 6
# D...*.
# .X.X..
# ....S.      # 6

# 5 4
# .D.*
# ....
# ..X.
# S.*.
# ....        # 4