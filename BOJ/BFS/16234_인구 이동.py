# 인구 이동
# n*n 크기의 땅, 각각의 땅에 나라가 하나씩 존재
# 인구 이동 하루 진행
    # 이웃하는 두 나라의 인구 차이가 l이상 r이하면 공유하는 국경선을 하루동안 엶
    # 국경선들이 모두 열렸다면 인구이동 시작
    # 인접한 칸으로만 이동가능 -> 연합
    # 연합을 이루고 있는 각 칸의 인구수 : (연합인구수) // (연합을 이루는 칸수)
    # 연합을 해체하고 모든 국경선 닫음
# 각 나라의 인구수 -> 인구 이동이 며칠동안 발생하는지 구하는 프로그램

# 입력 : n,l,r (n:1~50 / 1<=l<=r<=100)
# n개의 줄에 각 나라의 인구수 (0~100)  (인구이동이 발생하는 일수가 2000번아하인 입력만)
# 출력 : 인구이동이 며칠동안 발생하는지 첫째 줄에 출력

import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# bfs 함수 + 인구 배치
def bfs(graph,x,y):
    queue = deque([])
    popSum = graph[x][y]
    coor = [(x,y)]
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and l <= abs(graph[x][y]-graph[nx][ny]) <= r:
                popSum += graph[nx][ny]
                coor.append((nx,ny))
                visited[nx][ny] = True
                queue.append((nx,ny))
    # 국경선이 열리지 않았다면
    if len(coor) == 1:
        return
    # 인구 배치
    value = popSum // len(coor)
    for (x,y) in coor:
        graph[x][y] = value

# main 코드
days = 0
while True:
    visited = [[False]*n for _ in range(n)]
    bfsCount = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(graph,i,j)
                bfsCount += 1
    # 인구이동이 더이상 없다면(국경선이 열리지 않는다면)
    if bfsCount == n*n:
        break
    # 1일 증가
    days += 1

print(days)

# 2 20 50
# 50 30
# 20 40           # 1

# 2 40 50
# 50 30
# 20 40           # 0

# 2 20 50
# 50 30
# 30 40           # 1

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10        # 2

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10    # 3